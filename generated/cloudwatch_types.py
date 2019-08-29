
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class DeleteAlarmsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AlarmNames: list

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('DeleteAlarms')
    members = operation_model.input_shape.members


class DeleteDashboardsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DashboardNames: list

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('DeleteDashboards')
    members = operation_model.input_shape.members


class DescribeAlarmHistoryInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AlarmName: str = None
    HistoryItemType: str = None
    StartDate: TimeStamp = None
    EndDate: TimeStamp = None
    MaxRecords: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('DescribeAlarmHistory')
    members = operation_model.input_shape.members


class DescribeAlarmsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AlarmNames: list = None
    AlarmNamePrefix: str = None
    StateValue: str = None
    ActionPrefix: str = None
    MaxRecords: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('DescribeAlarms')
    members = operation_model.input_shape.members


class DescribeAlarmsForMetricInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    MetricName: str
    Namespace: str
    Statistic: str = None
    ExtendedStatistic: str = None
    Dimensions: list = None
    Period: int = None
    Unit: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('DescribeAlarmsForMetric')
    members = operation_model.input_shape.members


class DisableAlarmActionsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AlarmNames: list

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('DisableAlarmActions')
    members = operation_model.input_shape.members


class EnableAlarmActionsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AlarmNames: list

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('EnableAlarmActions')
    members = operation_model.input_shape.members


class GetDashboardInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DashboardName: str

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('GetDashboard')
    members = operation_model.input_shape.members


class GetMetricDataInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    MetricDataQueries: list
    StartTime: TimeStamp
    EndTime: TimeStamp
    NextToken: str = None
    ScanBy: str = None
    MaxDatapoints: int = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('GetMetricData')
    members = operation_model.input_shape.members


class GetMetricStatisticsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Namespace: str
    MetricName: str
    StartTime: TimeStamp
    EndTime: TimeStamp
    Period: int
    Dimensions: list = None
    Statistics: list = None
    ExtendedStatistics: list = None
    Unit: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('GetMetricStatistics')
    members = operation_model.input_shape.members


class GetMetricWidgetImageInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    MetricWidget: str
    OutputFormat: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('GetMetricWidgetImage')
    members = operation_model.input_shape.members


class ListDashboardsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DashboardNamePrefix: str = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('ListDashboards')
    members = operation_model.input_shape.members


class ListMetricsInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Namespace: str = None
    MetricName: str = None
    Dimensions: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('ListMetrics')
    members = operation_model.input_shape.members


class PutDashboardInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DashboardName: str
    DashboardBody: str

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('PutDashboard')
    members = operation_model.input_shape.members


class PutMetricAlarmInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AlarmName: str
    EvaluationPeriods: int
    Threshold: int
    ComparisonOperator: str
    AlarmDescription: str = None
    ActionsEnabled: bool = None
    OKActions: list = None
    AlarmActions: list = None
    InsufficientDataActions: list = None
    MetricName: str = None
    Namespace: str = None
    Statistic: str = None
    ExtendedStatistic: str = None
    Dimensions: list = None
    Period: int = None
    Unit: str = None
    DatapointsToAlarm: int = None
    TreatMissingData: str = None
    EvaluateLowSampleCountPercentile: str = None
    Metrics: list = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('PutMetricAlarm')
    members = operation_model.input_shape.members


class PutMetricDataInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Namespace: str
    MetricData: list

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('PutMetricData')
    members = operation_model.input_shape.members


class SetAlarmStateInput(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AlarmName: str
    StateValue: str
    StateReason: str
    StateReasonData: str = None

    operation_model = botocore.session.Session().get_service_model('cloudwatch').operation_model('SetAlarmState')
    members = operation_model.input_shape.members
