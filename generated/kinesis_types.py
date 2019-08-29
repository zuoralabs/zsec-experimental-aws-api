
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AddTagsToStreamInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    Tags: Map

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('AddTagsToStream')
    members = operation_model.input_shape.members


class CreateStreamInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    ShardCount: int

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('CreateStream')
    members = operation_model.input_shape.members


class DecreaseStreamRetentionPeriodInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    RetentionPeriodHours: int

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DecreaseStreamRetentionPeriod')
    members = operation_model.input_shape.members


class DeleteStreamInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    EnforceConsumerDeletion: bool = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DeleteStream')
    members = operation_model.input_shape.members


class DeregisterStreamConsumerInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamARN: str = None
    ConsumerName: str = None
    ConsumerARN: str = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DeregisterStreamConsumer')
    members = operation_model.input_shape.members


class DescribeLimitsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DescribeLimits')
    members = operation_model.input_shape.members


class DescribeStreamInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    Limit: int = None
    ExclusiveStartShardId: str = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DescribeStream')
    members = operation_model.input_shape.members


class DescribeStreamConsumerInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamARN: str = None
    ConsumerName: str = None
    ConsumerARN: str = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DescribeStreamConsumer')
    members = operation_model.input_shape.members


class DescribeStreamSummaryInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DescribeStreamSummary')
    members = operation_model.input_shape.members


class DisableEnhancedMonitoringInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    ShardLevelMetrics: list

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('DisableEnhancedMonitoring')
    members = operation_model.input_shape.members


class EnableEnhancedMonitoringInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    ShardLevelMetrics: list

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('EnableEnhancedMonitoring')
    members = operation_model.input_shape.members


class GetRecordsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ShardIterator: str
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('GetRecords')
    members = operation_model.input_shape.members


class GetShardIteratorInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    ShardId: str
    ShardIteratorType: str
    StartingSequenceNumber: str = None
    Timestamp: TimeStamp = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('GetShardIterator')
    members = operation_model.input_shape.members


class IncreaseStreamRetentionPeriodInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    RetentionPeriodHours: int

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('IncreaseStreamRetentionPeriod')
    members = operation_model.input_shape.members


class ListShardsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str = None
    NextToken: str = None
    ExclusiveStartShardId: str = None
    MaxResults: int = None
    StreamCreationTimestamp: TimeStamp = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('ListShards')
    members = operation_model.input_shape.members


class ListStreamConsumersInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamARN: str
    NextToken: str = None
    MaxResults: int = None
    StreamCreationTimestamp: TimeStamp = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('ListStreamConsumers')
    members = operation_model.input_shape.members


class ListStreamsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Limit: int = None
    ExclusiveStartStreamName: str = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('ListStreams')
    members = operation_model.input_shape.members


class ListTagsForStreamInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    ExclusiveStartTagKey: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('ListTagsForStream')
    members = operation_model.input_shape.members


class MergeShardsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    ShardToMerge: str
    AdjacentShardToMerge: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('MergeShards')
    members = operation_model.input_shape.members


class PutRecordInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    Data: bytes
    PartitionKey: str
    ExplicitHashKey: str = None
    SequenceNumberForOrdering: str = None

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('PutRecord')
    members = operation_model.input_shape.members


class PutRecordsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Records: list
    StreamName: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('PutRecords')
    members = operation_model.input_shape.members


class RegisterStreamConsumerInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamARN: str
    ConsumerName: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('RegisterStreamConsumer')
    members = operation_model.input_shape.members


class RemoveTagsFromStreamInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    TagKeys: list

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('RemoveTagsFromStream')
    members = operation_model.input_shape.members


class SplitShardInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    ShardToSplit: str
    NewStartingHashKey: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('SplitShard')
    members = operation_model.input_shape.members


class StartStreamEncryptionInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    EncryptionType: str
    KeyId: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('StartStreamEncryption')
    members = operation_model.input_shape.members


class StopStreamEncryptionInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    EncryptionType: str
    KeyId: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('StopStreamEncryption')
    members = operation_model.input_shape.members


class SubscribeToShardInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConsumerARN: str
    ShardId: str
    StartingPosition: dict

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('SubscribeToShard')
    members = operation_model.input_shape.members


class UpdateShardCountInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    StreamName: str
    TargetShardCount: int
    ScalingType: str

    operation_model = botocore.session.Session().get_service_model('kinesis').operation_model('UpdateShardCount')
    members = operation_model.input_shape.members
