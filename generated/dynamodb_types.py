
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class BatchGetItemInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RequestItems: Map
    ReturnConsumedCapacity: str = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('BatchGetItem')
    members = operation_model.input_shape.members


class BatchWriteItemInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RequestItems: Map
    ReturnConsumedCapacity: str = None
    ReturnItemCollectionMetrics: str = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('BatchWriteItem')
    members = operation_model.input_shape.members


class CreateBackupInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    BackupName: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('CreateBackup')
    members = operation_model.input_shape.members


class CreateGlobalTableInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalTableName: str
    ReplicationGroup: list

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('CreateGlobalTable')
    members = operation_model.input_shape.members


class CreateTableInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AttributeDefinitions: list
    TableName: str
    KeySchema: list
    LocalSecondaryIndexes: list = None
    GlobalSecondaryIndexes: list = None
    BillingMode: str = None
    ProvisionedThroughput: dict = None
    StreamSpecification: dict = None
    SSESpecification: dict = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('CreateTable')
    members = operation_model.input_shape.members


class DeleteBackupInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BackupArn: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DeleteBackup')
    members = operation_model.input_shape.members


class DeleteItemInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    Key: Map
    Expected: Map = None
    ConditionalOperator: str = None
    ReturnValues: str = None
    ReturnConsumedCapacity: str = None
    ReturnItemCollectionMetrics: str = None
    ConditionExpression: str = None
    ExpressionAttributeNames: Map = None
    ExpressionAttributeValues: Map = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DeleteItem')
    members = operation_model.input_shape.members


class DeleteTableInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DeleteTable')
    members = operation_model.input_shape.members


class DescribeBackupInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BackupArn: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeBackup')
    members = operation_model.input_shape.members


class DescribeContinuousBackupsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeContinuousBackups')
    members = operation_model.input_shape.members


class DescribeEndpointsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeEndpoints')
    members = operation_model.input_shape.members


class DescribeGlobalTableInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalTableName: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeGlobalTable')
    members = operation_model.input_shape.members


class DescribeGlobalTableSettingsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalTableName: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeGlobalTableSettings')
    members = operation_model.input_shape.members


class DescribeLimitsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeLimits')
    members = operation_model.input_shape.members


class DescribeTableInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeTable')
    members = operation_model.input_shape.members


class DescribeTimeToLiveInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('DescribeTimeToLive')
    members = operation_model.input_shape.members


class GetItemInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    Key: Map
    AttributesToGet: list = None
    ConsistentRead: bool = None
    ReturnConsumedCapacity: str = None
    ProjectionExpression: str = None
    ExpressionAttributeNames: Map = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('GetItem')
    members = operation_model.input_shape.members


class ListBackupsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str = None
    Limit: int = None
    TimeRangeLowerBound: TimeStamp = None
    TimeRangeUpperBound: TimeStamp = None
    ExclusiveStartBackupArn: str = None
    BackupType: str = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('ListBackups')
    members = operation_model.input_shape.members


class ListGlobalTablesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ExclusiveStartGlobalTableName: str = None
    Limit: int = None
    RegionName: str = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('ListGlobalTables')
    members = operation_model.input_shape.members


class ListTablesInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ExclusiveStartTableName: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('ListTables')
    members = operation_model.input_shape.members


class ListTagsOfResourceInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('ListTagsOfResource')
    members = operation_model.input_shape.members


class PutItemInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    Item: Map
    Expected: Map = None
    ReturnValues: str = None
    ReturnConsumedCapacity: str = None
    ReturnItemCollectionMetrics: str = None
    ConditionalOperator: str = None
    ConditionExpression: str = None
    ExpressionAttributeNames: Map = None
    ExpressionAttributeValues: Map = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('PutItem')
    members = operation_model.input_shape.members


class QueryInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    IndexName: str = None
    Select: str = None
    AttributesToGet: list = None
    Limit: int = None
    ConsistentRead: bool = None
    KeyConditions: Map = None
    QueryFilter: Map = None
    ConditionalOperator: str = None
    ScanIndexForward: bool = None
    ExclusiveStartKey: Map = None
    ReturnConsumedCapacity: str = None
    ProjectionExpression: str = None
    FilterExpression: str = None
    KeyConditionExpression: str = None
    ExpressionAttributeNames: Map = None
    ExpressionAttributeValues: Map = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('Query')
    members = operation_model.input_shape.members


class RestoreTableFromBackupInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TargetTableName: str
    BackupArn: str

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('RestoreTableFromBackup')
    members = operation_model.input_shape.members


class RestoreTableToPointInTimeInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceTableName: str
    TargetTableName: str
    UseLatestRestorableTime: bool = None
    RestoreDateTime: TimeStamp = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('RestoreTableToPointInTime')
    members = operation_model.input_shape.members


class ScanInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    IndexName: str = None
    AttributesToGet: list = None
    Limit: int = None
    Select: str = None
    ScanFilter: Map = None
    ConditionalOperator: str = None
    ExclusiveStartKey: Map = None
    ReturnConsumedCapacity: str = None
    TotalSegments: int = None
    Segment: int = None
    ProjectionExpression: str = None
    FilterExpression: str = None
    ExpressionAttributeNames: Map = None
    ExpressionAttributeValues: Map = None
    ConsistentRead: bool = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('Scan')
    members = operation_model.input_shape.members


class TagResourceInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str
    Tags: list

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('TagResource')
    members = operation_model.input_shape.members


class TransactGetItemsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransactItems: list
    ReturnConsumedCapacity: str = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('TransactGetItems')
    members = operation_model.input_shape.members


class TransactWriteItemsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransactItems: list
    ReturnConsumedCapacity: str = None
    ReturnItemCollectionMetrics: str = None
    ClientRequestToken: str = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('TransactWriteItems')
    members = operation_model.input_shape.members


class UntagResourceInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str
    TagKeys: list

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('UntagResource')
    members = operation_model.input_shape.members


class UpdateContinuousBackupsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    PointInTimeRecoverySpecification: dict

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('UpdateContinuousBackups')
    members = operation_model.input_shape.members


class UpdateGlobalTableInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalTableName: str
    ReplicaUpdates: list

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('UpdateGlobalTable')
    members = operation_model.input_shape.members


class UpdateGlobalTableSettingsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalTableName: str
    GlobalTableBillingMode: str = None
    GlobalTableProvisionedWriteCapacityUnits: int = None
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: dict = None
    GlobalTableGlobalSecondaryIndexSettingsUpdate: list = None
    ReplicaSettingsUpdate: list = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('UpdateGlobalTableSettings')
    members = operation_model.input_shape.members


class UpdateItemInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    Key: Map
    AttributeUpdates: Map = None
    Expected: Map = None
    ConditionalOperator: str = None
    ReturnValues: str = None
    ReturnConsumedCapacity: str = None
    ReturnItemCollectionMetrics: str = None
    UpdateExpression: str = None
    ConditionExpression: str = None
    ExpressionAttributeNames: Map = None
    ExpressionAttributeValues: Map = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('UpdateItem')
    members = operation_model.input_shape.members


class UpdateTableInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    AttributeDefinitions: list = None
    BillingMode: str = None
    ProvisionedThroughput: dict = None
    GlobalSecondaryIndexUpdates: list = None
    StreamSpecification: dict = None
    SSESpecification: dict = None

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('UpdateTable')
    members = operation_model.input_shape.members


class UpdateTimeToLiveInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TableName: str
    TimeToLiveSpecification: dict

    operation_model = botocore.session.Session().get_service_model('dynamodb').operation_model('UpdateTimeToLive')
    members = operation_model.input_shape.members
