
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AddPermissionInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str
    Label: str
    AWSAccountId: list
    ActionName: list

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('AddPermission')
    members = operation_model.input_shape.members


class CheckIfPhoneNumberIsOptedOutInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    phoneNumber: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('CheckIfPhoneNumberIsOptedOut')
    members = operation_model.input_shape.members


class ConfirmSubscriptionInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str
    Token: str
    AuthenticateOnUnsubscribe: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('ConfirmSubscription')
    members = operation_model.input_shape.members


class CreatePlatformApplicationInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    Platform: str
    Attributes: Map

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('CreatePlatformApplication')
    members = operation_model.input_shape.members


class CreatePlatformEndpointInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PlatformApplicationArn: str
    Token: str
    CustomUserData: str = None
    Attributes: Map = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('CreatePlatformEndpoint')
    members = operation_model.input_shape.members


class CreateTopicInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    Attributes: Map = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('CreateTopic')
    members = operation_model.input_shape.members


class DeleteEndpointInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    EndpointArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('DeleteEndpoint')
    members = operation_model.input_shape.members


class DeletePlatformApplicationInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PlatformApplicationArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('DeletePlatformApplication')
    members = operation_model.input_shape.members


class DeleteTopicInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('DeleteTopic')
    members = operation_model.input_shape.members


class GetEndpointAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    EndpointArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('GetEndpointAttributes')
    members = operation_model.input_shape.members


class GetPlatformApplicationAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PlatformApplicationArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('GetPlatformApplicationAttributes')
    members = operation_model.input_shape.members


class GetSMSAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    attributes: list = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('GetSMSAttributes')
    members = operation_model.input_shape.members


class GetSubscriptionAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('GetSubscriptionAttributes')
    members = operation_model.input_shape.members


class GetTopicAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('GetTopicAttributes')
    members = operation_model.input_shape.members


class ListEndpointsByPlatformApplicationInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PlatformApplicationArn: str
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('ListEndpointsByPlatformApplication')
    members = operation_model.input_shape.members


class ListPhoneNumbersOptedOutInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    nextToken: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('ListPhoneNumbersOptedOut')
    members = operation_model.input_shape.members


class ListPlatformApplicationsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('ListPlatformApplications')
    members = operation_model.input_shape.members


class ListSubscriptionsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('ListSubscriptions')
    members = operation_model.input_shape.members


class ListSubscriptionsByTopicInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('ListSubscriptionsByTopic')
    members = operation_model.input_shape.members


class ListTopicsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('ListTopics')
    members = operation_model.input_shape.members


class OptInPhoneNumberInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    phoneNumber: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('OptInPhoneNumber')
    members = operation_model.input_shape.members


class PublishInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Message: str
    TopicArn: str = None
    TargetArn: str = None
    PhoneNumber: str = None
    Subject: str = None
    MessageStructure: str = None
    MessageAttributes: Map = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('Publish')
    members = operation_model.input_shape.members


class RemovePermissionInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str
    Label: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('RemovePermission')
    members = operation_model.input_shape.members


class SetEndpointAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    EndpointArn: str
    Attributes: Map

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('SetEndpointAttributes')
    members = operation_model.input_shape.members


class SetPlatformApplicationAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PlatformApplicationArn: str
    Attributes: Map

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('SetPlatformApplicationAttributes')
    members = operation_model.input_shape.members


class SetSMSAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    attributes: Map

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('SetSMSAttributes')
    members = operation_model.input_shape.members


class SetSubscriptionAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionArn: str
    AttributeName: str
    AttributeValue: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('SetSubscriptionAttributes')
    members = operation_model.input_shape.members


class SetTopicAttributesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str
    AttributeName: str
    AttributeValue: str = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('SetTopicAttributes')
    members = operation_model.input_shape.members


class SubscribeInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TopicArn: str
    Protocol: str
    Endpoint: str = None
    Attributes: Map = None
    ReturnSubscriptionArn: bool = None

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('Subscribe')
    members = operation_model.input_shape.members


class UnsubscribeInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionArn: str

    operation_model = botocore.session.Session().get_service_model('sns').operation_model('Unsubscribe')
    members = operation_model.input_shape.members
