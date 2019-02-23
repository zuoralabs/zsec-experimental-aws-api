import typing
from botocore import xform_name


def to_dict(nt: typing.NamedTuple):
    return {k: v for k, v in nt._asdict().items() if v is not None}


def slow_to_method_name(svc, operation_name):
    for py_name, op_name in svc._PY_TO_OP_NAME:
        if operation_name == py_name:
            return py_name 


def execute(svc, request):
    #ff = getattr(svc, to_method_name(svc, request.operation_model.name))
    method = getattr(svc, xform_name(request.operation_model.name))
    return method(**to_dict(request))


# notes
# search botocore for py_name_to_operation_name
# svc._PY_TO_OP_NAME
# svc._service_model.service_name
