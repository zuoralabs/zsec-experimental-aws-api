
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AssumeRoleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RoleArn: str
    RoleSessionName: str
    Policy: str = None
    DurationSeconds: int = None
    ExternalId: str = None
    SerialNumber: str = None
    TokenCode: str = None

    operation_model = botocore.session.Session().get_service_model('sts').operation_model('AssumeRole')
    members = operation_model.input_shape.members


class AssumeRoleWithSAMLRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RoleArn: str
    PrincipalArn: str
    SAMLAssertion: str
    Policy: str = None
    DurationSeconds: int = None

    operation_model = botocore.session.Session().get_service_model('sts').operation_model('AssumeRoleWithSAML')
    members = operation_model.input_shape.members


class AssumeRoleWithWebIdentityRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RoleArn: str
    RoleSessionName: str
    WebIdentityToken: str
    ProviderId: str = None
    Policy: str = None
    DurationSeconds: int = None

    operation_model = botocore.session.Session().get_service_model('sts').operation_model('AssumeRoleWithWebIdentity')
    members = operation_model.input_shape.members


class DecodeAuthorizationMessageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    EncodedMessage: str

    operation_model = botocore.session.Session().get_service_model('sts').operation_model('DecodeAuthorizationMessage')
    members = operation_model.input_shape.members


class GetCallerIdentityRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('sts').operation_model('GetCallerIdentity')
    members = operation_model.input_shape.members


class GetFederationTokenRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    Policy: str = None
    DurationSeconds: int = None

    operation_model = botocore.session.Session().get_service_model('sts').operation_model('GetFederationToken')
    members = operation_model.input_shape.members


class GetSessionTokenRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DurationSeconds: int = None
    SerialNumber: str = None
    TokenCode: str = None

    operation_model = botocore.session.Session().get_service_model('sts').operation_model('GetSessionToken')
    members = operation_model.input_shape.members
