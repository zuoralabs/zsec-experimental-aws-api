
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AssociateDRTLogBucketRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    LogBucket: str

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('AssociateDRTLogBucket')
    members = operation_model.input_shape.members


class AssociateDRTRoleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RoleArn: str

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('AssociateDRTRole')
    members = operation_model.input_shape.members


class CreateProtectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ResourceArn: str

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('CreateProtection')
    members = operation_model.input_shape.members


class CreateSubscriptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('shield').operation_model('CreateSubscription')
    members = operation_model.input_shape.members


class DeleteProtectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ProtectionId: str

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DeleteProtection')
    members = operation_model.input_shape.members


class DeleteSubscriptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DeleteSubscription')
    members = operation_model.input_shape.members


class DescribeAttackRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AttackId: str

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DescribeAttack')
    members = operation_model.input_shape.members


class DescribeDRTAccessRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DescribeDRTAccess')
    members = operation_model.input_shape.members


class DescribeEmergencyContactSettingsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DescribeEmergencyContactSettings')
    members = operation_model.input_shape.members


class DescribeProtectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ProtectionId: str

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DescribeProtection')
    members = operation_model.input_shape.members


class DescribeSubscriptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DescribeSubscription')
    members = operation_model.input_shape.members


class DisassociateDRTLogBucketRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    LogBucket: str

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DisassociateDRTLogBucket')
    members = operation_model.input_shape.members


class DisassociateDRTRoleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('shield').operation_model('DisassociateDRTRole')
    members = operation_model.input_shape.members


class GetSubscriptionStateRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('shield').operation_model('GetSubscriptionState')
    members = operation_model.input_shape.members


class ListAttacksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArns: list = None
    StartTime: dict = None
    EndTime: dict = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('ListAttacks')
    members = operation_model.input_shape.members


class ListProtectionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('ListProtections')
    members = operation_model.input_shape.members


class UpdateEmergencyContactSettingsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    EmergencyContactList: list = None

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('UpdateEmergencyContactSettings')
    members = operation_model.input_shape.members


class UpdateSubscriptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AutoRenew: str = None

    operation_model = botocore.session.Session().get_service_model('shield').operation_model('UpdateSubscription')
    members = operation_model.input_shape.members
