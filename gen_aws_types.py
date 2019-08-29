import textwrap
import botocore
import botocore.session
import typing
from collections import OrderedDict
from pathlib import Path


def snakecase(ss):
    return '_'.join(ss.split('-'))


core_sess = botocore.session.Session()

#type_names = {k: '''operation_model.input_shape.members['{k}']'''.format(k=k) for k in members}

type_name_mapping = {'string': str.__name__,
                     'structure': dict.__name__,
                     'boolean': bool.__name__,
                     'timestamp': 'TimeStamp',
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

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    
'''

unknown_type_names = set()


def class_def(service_name: str, operation_name: str):
    sm = core_sess.get_service_model(service_name)
    assert operation_name in sm.operation_names
    operation_model = sm.operation_model(operation_name)
    if operation_model.input_shape is None:
        members = {}
        required_members = []
        class_name = operation_name
        print('skipping {}; no args'.format(operation_name))
        return ''
    else:
        members = operation_model.input_shape.members
        required_members = operation_model.input_shape.required_members
        class_name = operation_model.input_shape.name

    type_names = {k: type_name_mapping.get(v.type_name, 'typing.Any') for k, v in members.items()}
    unknown_type_names.update(v.type_name for v in members.values()
                              if v.type_name not in type_name_mapping
                              )

    default_values = {
        k: '' if k in required_members else ' = None'
        for k in members}

    optional_members = [k for k in members if k not in required_members]

    formatted_members = '\n'.join(
        '    {k}: {type_name}{default_value}'.format(
            k=k,
            default_value=default_values[k],
            type_name=type_names.get(k, 'typing.Any')
        )
        for k in required_members + optional_members)

    formatted_types = textwrap.dedent('\n'.join('''
    class {type_name}:
        shape: {shape_name}
    '''.format(type_name=k, shape_name=v) for k, v in type_names.items()))

    return textwrap.dedent(
        '''
        class {type_name}(typing.NamedTuple):
    
            def execute(self, svc):
                return aws_meta.execute(svc, self)
                
        {members}
        
            operation_model = botocore.session.Session().get_service_model('{service_name}').operation_model('{operation_name}')
            members = operation_model.input_shape.members
        ''').format(
        types=textwrap.indent(formatted_types, prefix=' '*4),
        type_name=class_name,
        members=formatted_members,
        operation_name = operation_name,
        service_name = service_name,
    )


# example: 'CreateBucket'

def create_module(service_name: str):
    sm = core_sess.get_service_model(service_name)
    Path('generated/{}_types.py'.format(snakecase(service_name))).write_text(
        header + '\n'.join(class_def(service_name=service_name, operation_name=operation_name)
                           for operation_name in sm.operation_names)
    )


for service_name in ['s3', 'waf', 'waf-regional', 'dynamodb', 'shield', 'ec2', 'organizations', 'ssm', 'sts', 'config',
                     'sns', 'sqs', 'rds', 'cloudwatch', 'kinesis']:
    create_module(service_name)

assert not unknown_type_names, "There are unknown_type_names: {}".format(unknown_type_names)
