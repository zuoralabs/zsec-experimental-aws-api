
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AddPermissionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    Label: str
    AWSAccountIds: list
    Actions: list

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('AddPermission')
    members = operation_model.input_shape.members


class ChangeMessageVisibilityRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    ReceiptHandle: str
    VisibilityTimeout: int

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('ChangeMessageVisibility')
    members = operation_model.input_shape.members


class ChangeMessageVisibilityBatchRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    Entries: list

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('ChangeMessageVisibilityBatch')
    members = operation_model.input_shape.members


class CreateQueueRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueName: str
    Attributes: Map = None

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('CreateQueue')
    members = operation_model.input_shape.members


class DeleteMessageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    ReceiptHandle: str

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('DeleteMessage')
    members = operation_model.input_shape.members


class DeleteMessageBatchRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    Entries: list

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('DeleteMessageBatch')
    members = operation_model.input_shape.members


class DeleteQueueRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('DeleteQueue')
    members = operation_model.input_shape.members


class GetQueueAttributesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    AttributeNames: list = None

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('GetQueueAttributes')
    members = operation_model.input_shape.members


class GetQueueUrlRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueName: str
    QueueOwnerAWSAccountId: str = None

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('GetQueueUrl')
    members = operation_model.input_shape.members


class ListDeadLetterSourceQueuesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('ListDeadLetterSourceQueues')
    members = operation_model.input_shape.members


class ListQueueTagsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('ListQueueTags')
    members = operation_model.input_shape.members


class ListQueuesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueNamePrefix: str = None

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('ListQueues')
    members = operation_model.input_shape.members


class PurgeQueueRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('PurgeQueue')
    members = operation_model.input_shape.members


class ReceiveMessageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    AttributeNames: list = None
    MessageAttributeNames: list = None
    MaxNumberOfMessages: int = None
    VisibilityTimeout: int = None
    WaitTimeSeconds: int = None
    ReceiveRequestAttemptId: str = None

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('ReceiveMessage')
    members = operation_model.input_shape.members


class RemovePermissionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    Label: str

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('RemovePermission')
    members = operation_model.input_shape.members


class SendMessageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    MessageBody: str
    DelaySeconds: int = None
    MessageAttributes: Map = None
    MessageDeduplicationId: str = None
    MessageGroupId: str = None

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('SendMessage')
    members = operation_model.input_shape.members


class SendMessageBatchRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    Entries: list

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('SendMessageBatch')
    members = operation_model.input_shape.members


class SetQueueAttributesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    Attributes: Map

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('SetQueueAttributes')
    members = operation_model.input_shape.members


class TagQueueRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    Tags: Map

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('TagQueue')
    members = operation_model.input_shape.members


class UntagQueueRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    QueueUrl: str
    TagKeys: list

    operation_model = botocore.session.Session().get_service_model('sqs').operation_model('UntagQueue')
    members = operation_model.input_shape.members
