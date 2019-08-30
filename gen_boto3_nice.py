import textwrap
import botocore
import botocore.session
from typing import Iterable
from collections import OrderedDict
from botocore import xform_name
from pathlib import Path
from itertools import chain


def snakecase(ss):
    return '_'.join(ss.split('-'))


core_sess = botocore.session.Session()

#type_names = {k: '''operation_model.input_shape.members['{k}']'''.format(k=k) for k in members}

type_name_mapping = {'string': str.__name__,
                     'structure': dict.__name__,
                     'boolean': bool.__name__,
                     'timestamp': 'datetime',
                     'map': 'Map',
                     'integer': int.__name__,
                     'long': int.__name__,
                     'blob': bytes.__name__,
                     'list': list.__name__,
                     'double': int.__name__,
                     }


header = '''
import typing
import botocore.session
import aws_meta
from botocore.model import *
from botocore.client import BaseClient
from datetime import datetime
import boto3


class Map(dict):
    pass
    
    
# noinspection PyPep8Naming
class {class_name}(BaseClient):
'''

unknown_type_names = set()


def method_def(service_name: str, operation_name: str):
    sm = core_sess.get_service_model(service_name)
    assert operation_name in sm.operation_names
    operation_model = sm.operation_model(operation_name)
    if operation_model.input_shape is None:
        members = {}
        required_members = []
        class_name = operation_name
        print('warning {}; no args'.format(operation_name))
    else:
        members = operation_model.input_shape.members
        required_members = operation_model.input_shape.required_members
        class_name = operation_model.input_shape.name

    method_name = xform_name(operation_model.name)

    type_names = {k: type_name_mapping.get(v.type_name, 'typing.Any') for k, v in members.items()}
    unknown_type_names.update(v.type_name for v in members.values()
                              if v.type_name not in type_name_mapping
                              )

    default_values = {
        k: '' if k in required_members else ' = None'
        for k in members}

    optional_members = [k for k in members if k not in required_members]

    formatted_members = ['{k}: {type_name}{default_value}'.format(
        k=k,
        default_value=default_values[k],
        type_name=type_names.get(k, 'typing.Any')
    )
        for k in required_members + optional_members]

    return textwrap.dedent('''def {method_name}({members}): ...''').format(
        method_name=method_name,
        type_name=class_name,
        members=', '.join(chain(('self',), formatted_members)),
        operation_name=operation_name,
        service_name=service_name,
    )


# example: 'CreateBucket'

def create_module(package_path: Path, service_name: str):
    module_name = '{}_stubs'.format(snakecase(service_name))
    class_name = '{}_client_type'.format(snakecase(service_name))
    client_maker_name = '{}_client'.format(snakecase(service_name))
    sm: botocore.session.ServiceModel = core_sess.get_service_model(service_name)

    client_maker = textwrap.dedent("""
    def {client_maker_name}(self: 'Session', region_name: str = None) -> {class_name}:
        return self.client('{service_name}', region_name=region_name)
    """.format(service_name=service_name, client_maker_name=client_maker_name, class_name=class_name)).strip()

    package_path.joinpath('{}.py'.format(module_name)).write_text(
        header.format(class_name=class_name)
        + '\n'.join(textwrap.indent(method_def(service_name=service_name, operation_name=operation_name), ' '*4)
                    for operation_name in sm.operation_names)
        + '\n    pass\n'
        + '\n'
    )

    return module_name, class_name, client_maker


def create_package(service_names: Iterable[str]):
    package_path = Path('boto3_nice')
    package_path.mkdir(exist_ok=True)

    imports = []
    client_makers = []
    for service_name in service_names:
        module_name, class_name, client_maker = create_module(package_path, service_name)
        imports.append("from .{module_name} import {class_name}".
                       format(module_name=module_name, class_name=class_name))
        client_makers.append(client_maker)

    client_overloads = [
        textwrap.dedent("""
        @overload
        def client(self, service_name: {}_service_name_type,
                   region_name=None, api_version=None, use_ssl=True, verify=None, endpoint_url=None, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, config=None,
                   ) -> BaseClient: ...
        """).strip().format(snakecase(service_name))
        for service_name in service_names
    ]

    text = textwrap.dedent("""
    import boto3 as _boto3
    {imports}
    
    
    class Session(_boto3.Session):
    {members}
    """).format(imports='\n'.join(imports),
                members=textwrap.indent('\n\n'.join(client_makers), ' '*4)).lstrip()
    package_path.joinpath('__init__.py').write_text(text)

    text = textwrap.dedent("""
    import boto3 as _boto3
    from typing import overload
    from botocore.client import BaseClient
    from .service_names import *
    {imports}
    
    
    class Session(_boto3.Session):
    {members}
    """).format(imports='\n'.join(imports),
                members=textwrap.indent('\n\n'.join(client_overloads + client_makers), ' '*4)).lstrip()
    package_path.joinpath('__init__.pyi').write_text(text)

    service_names_template = textwrap.dedent("""
    from typing import NewType
    
    
    {body}
    """).strip()
    service_names_defs = [textwrap.dedent("""
    {ss}_service_name_type = NewType('{ss}_service_name', str)
    {ss}_service_name: {ss}_service_name_type = {ss}_service_name_type('{ss}')
    """).lstrip().format(ss=snakecase(service_name)) for service_name in service_names]
    service_names_text = service_names_template.format(body='\n'.join(service_names_defs))
    package_path.joinpath('service_names.py').write_text(service_names_text)


assert not unknown_type_names, "There are unknown_type_names: {}".format(unknown_type_names)

if __name__ == '__main__':
    # NB: can get all service names via `session.get_available_services()`
    create_package(
        ['s3', 'waf', 'waf-regional', 'dynamodb', 'shield', 'ec2', 'organizations', 'ssm', 'sts', 'config',
         'sns', 'sqs', 'rds', 'cloudwatch', 'kinesis']
    )
