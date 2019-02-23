import textwrap
import botocore
import botocore.session
import typing
from collections import OrderedDict
from pathlib import Path

core_sess = botocore.session.Session()


operation_name = 'CreateBucket'
service_name = 's3'

sm = core_sess.get_service_model(service_name)
assert operation_name in sm.operation_names
operation_model = sm.operation_model(operation_name)
members = operation_model.input_shape.members

#type_names = {k: '''operation_model.input_shape.members['{k}']'''.format(k=k) for k in members}
type_names = {k: str.__name__ for k,v in members.items()
        if isinstance(v, botocore.model.StringShape)}

default_values = {
        k: '' if k in operation_model.input_shape.required_members else ' = None'
        for k in members}

optional_members = [k for k in members if k not in operation_model.input_shape.required_members]

formatted_members = '\n'.join(
        '    {k}: {type_name}{default_value}'.format(
            k=k, 
            default_value=default_values[k],
            type_name=type_names.get(k, 'typing.Any')
            ) 
        for k in operation_model.input_shape.required_members + optional_members)

formatted_types = '\n'.join('''
class {type_name}:
    shape: {shape_name}
'''.format(type_name=k, shape_name=v)
    for k,v in type_names.items())

Path('generated_module.py').write_text(
        textwrap.dedent('''
        import typing
        import botocore.session
        import aws_meta
        from botocore.model import *

        class {type_name}(typing.NamedTuple):
            operation_model = botocore.session.Session().get_service_model('{service_name}').operation_model('{operation_name}')
            members = operation_model.input_shape.members

            def execute(self, svc):
                return aws_meta.execute(svc, self)
        {members}

        ''').format(
            types=textwrap.indent(formatted_types, prefix=' '*4),
            type_name = operation_model.input_shape.name, 
            members=formatted_members,
            operation_name = operation_name,
            service_name = service_name,
        ))
