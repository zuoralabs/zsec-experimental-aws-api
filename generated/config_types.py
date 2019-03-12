
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class BatchGetAggregateResourceConfigRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    ResourceIdentifiers: list

    operation_model = botocore.session.Session().get_service_model('config').operation_model('BatchGetAggregateResourceConfig')
    members = operation_model.input_shape.members


class BatchGetResourceConfigRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    resourceKeys: list

    operation_model = botocore.session.Session().get_service_model('config').operation_model('BatchGetResourceConfig')
    members = operation_model.input_shape.members


class DeleteAggregationAuthorizationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AuthorizedAccountId: str
    AuthorizedAwsRegion: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeleteAggregationAuthorization')
    members = operation_model.input_shape.members


class DeleteConfigRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRuleName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeleteConfigRule')
    members = operation_model.input_shape.members


class DeleteConfigurationAggregatorRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeleteConfigurationAggregator')
    members = operation_model.input_shape.members


class DeleteConfigurationRecorderRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationRecorderName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeleteConfigurationRecorder')
    members = operation_model.input_shape.members


class DeleteDeliveryChannelRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DeliveryChannelName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeleteDeliveryChannel')
    members = operation_model.input_shape.members


class DeleteEvaluationResultsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRuleName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeleteEvaluationResults')
    members = operation_model.input_shape.members


class DeletePendingAggregationRequestRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RequesterAccountId: str
    RequesterAwsRegion: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeletePendingAggregationRequest')
    members = operation_model.input_shape.members


class DeleteRetentionConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RetentionConfigurationName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeleteRetentionConfiguration')
    members = operation_model.input_shape.members


class DeliverConfigSnapshotRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    deliveryChannelName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DeliverConfigSnapshot')
    members = operation_model.input_shape.members


class DescribeAggregateComplianceByConfigRulesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    Filters: dict = None
    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeAggregateComplianceByConfigRules')
    members = operation_model.input_shape.members


class DescribeAggregationAuthorizationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeAggregationAuthorizations')
    members = operation_model.input_shape.members


class DescribeComplianceByConfigRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRuleNames: list = None
    ComplianceTypes: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeComplianceByConfigRule')
    members = operation_model.input_shape.members


class DescribeComplianceByResourceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceType: str = None
    ResourceId: str = None
    ComplianceTypes: list = None
    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeComplianceByResource')
    members = operation_model.input_shape.members


class DescribeConfigRuleEvaluationStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRuleNames: list = None
    NextToken: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeConfigRuleEvaluationStatus')
    members = operation_model.input_shape.members


class DescribeConfigRulesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRuleNames: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeConfigRules')
    members = operation_model.input_shape.members


class DescribeConfigurationAggregatorSourcesStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    UpdateStatus: list = None
    NextToken: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeConfigurationAggregatorSourcesStatus')
    members = operation_model.input_shape.members


class DescribeConfigurationAggregatorsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorNames: list = None
    NextToken: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeConfigurationAggregators')
    members = operation_model.input_shape.members


class DescribeConfigurationRecorderStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationRecorderNames: list = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeConfigurationRecorderStatus')
    members = operation_model.input_shape.members


class DescribeConfigurationRecordersRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationRecorderNames: list = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeConfigurationRecorders')
    members = operation_model.input_shape.members


class DescribeDeliveryChannelStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DeliveryChannelNames: list = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeDeliveryChannelStatus')
    members = operation_model.input_shape.members


class DescribeDeliveryChannelsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DeliveryChannelNames: list = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeDeliveryChannels')
    members = operation_model.input_shape.members


class DescribePendingAggregationRequestsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribePendingAggregationRequests')
    members = operation_model.input_shape.members


class DescribeRetentionConfigurationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RetentionConfigurationNames: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('DescribeRetentionConfigurations')
    members = operation_model.input_shape.members


class GetAggregateComplianceDetailsByConfigRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: str = None
    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetAggregateComplianceDetailsByConfigRule')
    members = operation_model.input_shape.members


class GetAggregateConfigRuleComplianceSummaryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    Filters: dict = None
    GroupByKey: str = None
    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetAggregateConfigRuleComplianceSummary')
    members = operation_model.input_shape.members


class GetAggregateDiscoveredResourceCountsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    Filters: dict = None
    GroupByKey: str = None
    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetAggregateDiscoveredResourceCounts')
    members = operation_model.input_shape.members


class GetAggregateResourceConfigRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    ResourceIdentifier: dict

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetAggregateResourceConfig')
    members = operation_model.input_shape.members


class GetComplianceDetailsByConfigRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRuleName: str
    ComplianceTypes: list = None
    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetComplianceDetailsByConfigRule')
    members = operation_model.input_shape.members


class GetComplianceDetailsByResourceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceType: str
    ResourceId: str
    ComplianceTypes: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetComplianceDetailsByResource')
    members = operation_model.input_shape.members



class GetComplianceSummaryByResourceTypeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceTypes: list = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetComplianceSummaryByResourceType')
    members = operation_model.input_shape.members


class GetDiscoveredResourceCountsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    resourceTypes: list = None
    limit: int = None
    nextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetDiscoveredResourceCounts')
    members = operation_model.input_shape.members


class GetResourceConfigHistoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    resourceType: str
    resourceId: str
    laterTime: TimeStamp = None
    earlierTime: TimeStamp = None
    chronologicalOrder: str = None
    limit: int = None
    nextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('GetResourceConfigHistory')
    members = operation_model.input_shape.members


class ListAggregateDiscoveredResourcesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    ResourceType: str
    Filters: dict = None
    Limit: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('ListAggregateDiscoveredResources')
    members = operation_model.input_shape.members


class ListDiscoveredResourcesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    resourceType: str
    resourceIds: list = None
    resourceName: str = None
    limit: int = None
    includeDeletedResources: bool = None
    nextToken: str = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('ListDiscoveredResources')
    members = operation_model.input_shape.members


class PutAggregationAuthorizationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AuthorizedAccountId: str
    AuthorizedAwsRegion: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('PutAggregationAuthorization')
    members = operation_model.input_shape.members


class PutConfigRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRule: dict

    operation_model = botocore.session.Session().get_service_model('config').operation_model('PutConfigRule')
    members = operation_model.input_shape.members


class PutConfigurationAggregatorRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationAggregatorName: str
    AccountAggregationSources: list = None
    OrganizationAggregationSource: dict = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('PutConfigurationAggregator')
    members = operation_model.input_shape.members


class PutConfigurationRecorderRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationRecorder: dict

    operation_model = botocore.session.Session().get_service_model('config').operation_model('PutConfigurationRecorder')
    members = operation_model.input_shape.members


class PutDeliveryChannelRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DeliveryChannel: dict

    operation_model = botocore.session.Session().get_service_model('config').operation_model('PutDeliveryChannel')
    members = operation_model.input_shape.members


class PutEvaluationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResultToken: str
    Evaluations: list = None
    TestMode: bool = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('PutEvaluations')
    members = operation_model.input_shape.members


class PutRetentionConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RetentionPeriodInDays: int

    operation_model = botocore.session.Session().get_service_model('config').operation_model('PutRetentionConfiguration')
    members = operation_model.input_shape.members


class StartConfigRulesEvaluationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigRuleNames: list = None

    operation_model = botocore.session.Session().get_service_model('config').operation_model('StartConfigRulesEvaluation')
    members = operation_model.input_shape.members


class StartConfigurationRecorderRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationRecorderName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('StartConfigurationRecorder')
    members = operation_model.input_shape.members


class StopConfigurationRecorderRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConfigurationRecorderName: str

    operation_model = botocore.session.Session().get_service_model('config').operation_model('StopConfigurationRecorder')
    members = operation_model.input_shape.members
