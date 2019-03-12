
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AddTagsToResourceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceType: str
    ResourceId: str
    Tags: list

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('AddTagsToResource')
    members = operation_model.input_shape.members


class CancelCommandRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CommandId: str
    InstanceIds: list = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CancelCommand')
    members = operation_model.input_shape.members


class CancelMaintenanceWindowExecutionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowExecutionId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CancelMaintenanceWindowExecution')
    members = operation_model.input_shape.members


class CreateActivationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IamRole: str
    Description: str = None
    DefaultInstanceName: str = None
    RegistrationLimit: int = None
    ExpirationDate: TimeStamp = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CreateActivation')
    members = operation_model.input_shape.members


class CreateAssociationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    DocumentVersion: str = None
    InstanceId: str = None
    Parameters: Map = None
    Targets: list = None
    ScheduleExpression: str = None
    OutputLocation: dict = None
    AssociationName: str = None
    MaxErrors: str = None
    MaxConcurrency: str = None
    ComplianceSeverity: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CreateAssociation')
    members = operation_model.input_shape.members


class CreateAssociationBatchRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Entries: list

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CreateAssociationBatch')
    members = operation_model.input_shape.members


class CreateDocumentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Content: str
    Name: str
    Attachments: list = None
    VersionName: str = None
    DocumentType: str = None
    DocumentFormat: str = None
    TargetType: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CreateDocument')
    members = operation_model.input_shape.members


class CreateMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    Schedule: str
    Duration: int
    Cutoff: int
    AllowUnassociatedTargets: bool
    Description: str = None
    StartDate: str = None
    EndDate: str = None
    ScheduleTimezone: str = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CreateMaintenanceWindow')
    members = operation_model.input_shape.members


class CreatePatchBaselineRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    OperatingSystem: str = None
    GlobalFilters: dict = None
    ApprovalRules: dict = None
    ApprovedPatches: list = None
    ApprovedPatchesComplianceLevel: str = None
    ApprovedPatchesEnableNonSecurity: bool = None
    RejectedPatches: list = None
    RejectedPatchesAction: str = None
    Description: str = None
    Sources: list = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CreatePatchBaseline')
    members = operation_model.input_shape.members


class CreateResourceDataSyncRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SyncName: str
    S3Destination: dict

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('CreateResourceDataSync')
    members = operation_model.input_shape.members


class DeleteActivationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ActivationId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteActivation')
    members = operation_model.input_shape.members


class DeleteAssociationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str = None
    InstanceId: str = None
    AssociationId: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteAssociation')
    members = operation_model.input_shape.members


class DeleteDocumentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteDocument')
    members = operation_model.input_shape.members


class DeleteInventoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TypeName: str
    SchemaDeleteOption: str = None
    DryRun: bool = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteInventory')
    members = operation_model.input_shape.members


class DeleteMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteMaintenanceWindow')
    members = operation_model.input_shape.members


class DeleteParameterRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteParameter')
    members = operation_model.input_shape.members


class DeleteParametersRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Names: list

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteParameters')
    members = operation_model.input_shape.members


class DeletePatchBaselineRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BaselineId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeletePatchBaseline')
    members = operation_model.input_shape.members


class DeleteResourceDataSyncRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SyncName: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeleteResourceDataSync')
    members = operation_model.input_shape.members


class DeregisterManagedInstanceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeregisterManagedInstance')
    members = operation_model.input_shape.members


class DeregisterPatchBaselineForPatchGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BaselineId: str
    PatchGroup: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeregisterPatchBaselineForPatchGroup')
    members = operation_model.input_shape.members


class DeregisterTargetFromMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    WindowTargetId: str
    Safe: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeregisterTargetFromMaintenanceWindow')
    members = operation_model.input_shape.members


class DeregisterTaskFromMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    WindowTaskId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DeregisterTaskFromMaintenanceWindow')
    members = operation_model.input_shape.members


class DescribeActivationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeActivations')
    members = operation_model.input_shape.members


class DescribeAssociationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str = None
    InstanceId: str = None
    AssociationId: str = None
    AssociationVersion: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeAssociation')
    members = operation_model.input_shape.members


class DescribeAssociationExecutionTargetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str
    ExecutionId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeAssociationExecutionTargets')
    members = operation_model.input_shape.members


class DescribeAssociationExecutionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeAssociationExecutions')
    members = operation_model.input_shape.members


class DescribeAutomationExecutionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeAutomationExecutions')
    members = operation_model.input_shape.members


class DescribeAutomationStepExecutionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AutomationExecutionId: str
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None
    ReverseOrder: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeAutomationStepExecutions')
    members = operation_model.input_shape.members


class DescribeAvailablePatchesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeAvailablePatches')
    members = operation_model.input_shape.members


class DescribeDocumentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    DocumentVersion: str = None
    VersionName: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeDocument')
    members = operation_model.input_shape.members


class DescribeDocumentPermissionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    PermissionType: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeDocumentPermission')
    members = operation_model.input_shape.members


class DescribeEffectiveInstanceAssociationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeEffectiveInstanceAssociations')
    members = operation_model.input_shape.members


class DescribeEffectivePatchesForPatchBaselineRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BaselineId: str
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeEffectivePatchesForPatchBaseline')
    members = operation_model.input_shape.members


class DescribeInstanceAssociationsStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeInstanceAssociationsStatus')
    members = operation_model.input_shape.members


class DescribeInstanceInformationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceInformationFilterList: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeInstanceInformation')
    members = operation_model.input_shape.members


class DescribeInstancePatchStatesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceIds: list
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeInstancePatchStates')
    members = operation_model.input_shape.members


class DescribeInstancePatchStatesForPatchGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PatchGroup: str
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeInstancePatchStatesForPatchGroup')
    members = operation_model.input_shape.members


class DescribeInstancePatchesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeInstancePatches')
    members = operation_model.input_shape.members


class DescribeInventoryDeletionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DeletionId: str = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeInventoryDeletions')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowExecutionTaskInvocationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowExecutionId: str
    TaskId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindowExecutionTaskInvocations')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowExecutionTasksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowExecutionId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindowExecutionTasks')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowExecutionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindowExecutions')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowScheduleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str = None
    Targets: list = None
    ResourceType: str = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindowSchedule')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowTargetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindowTargets')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowTasksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindowTasks')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindows')
    members = operation_model.input_shape.members


class DescribeMaintenanceWindowsForTargetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Targets: list
    ResourceType: str
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeMaintenanceWindowsForTarget')
    members = operation_model.input_shape.members


class DescribeParametersRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    ParameterFilters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeParameters')
    members = operation_model.input_shape.members


class DescribePatchBaselinesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribePatchBaselines')
    members = operation_model.input_shape.members


class DescribePatchGroupStateRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PatchGroup: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribePatchGroupState')
    members = operation_model.input_shape.members


class DescribePatchGroupsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    MaxResults: int = None
    Filters: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribePatchGroups')
    members = operation_model.input_shape.members


class DescribeSessionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    State: str
    MaxResults: int = None
    NextToken: str = None
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('DescribeSessions')
    members = operation_model.input_shape.members


class GetAutomationExecutionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AutomationExecutionId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetAutomationExecution')
    members = operation_model.input_shape.members


class GetCommandInvocationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CommandId: str
    InstanceId: str
    PluginName: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetCommandInvocation')
    members = operation_model.input_shape.members


class GetConnectionStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Target: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetConnectionStatus')
    members = operation_model.input_shape.members


class GetDefaultPatchBaselineRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OperatingSystem: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetDefaultPatchBaseline')
    members = operation_model.input_shape.members


class GetDeployablePatchSnapshotForInstanceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    SnapshotId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetDeployablePatchSnapshotForInstance')
    members = operation_model.input_shape.members


class GetDocumentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    VersionName: str = None
    DocumentVersion: str = None
    DocumentFormat: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetDocument')
    members = operation_model.input_shape.members


class GetInventoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    Aggregators: list = None
    ResultAttributes: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetInventory')
    members = operation_model.input_shape.members


class GetInventorySchemaRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TypeName: str = None
    NextToken: str = None
    MaxResults: int = None
    Aggregator: bool = None
    SubType: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetInventorySchema')
    members = operation_model.input_shape.members


class GetMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetMaintenanceWindow')
    members = operation_model.input_shape.members


class GetMaintenanceWindowExecutionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowExecutionId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetMaintenanceWindowExecution')
    members = operation_model.input_shape.members


class GetMaintenanceWindowExecutionTaskRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowExecutionId: str
    TaskId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetMaintenanceWindowExecutionTask')
    members = operation_model.input_shape.members


class GetMaintenanceWindowExecutionTaskInvocationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowExecutionId: str
    TaskId: str
    InvocationId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetMaintenanceWindowExecutionTaskInvocation')
    members = operation_model.input_shape.members


class GetMaintenanceWindowTaskRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    WindowTaskId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetMaintenanceWindowTask')
    members = operation_model.input_shape.members


class GetParameterRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    WithDecryption: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetParameter')
    members = operation_model.input_shape.members


class GetParameterHistoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    WithDecryption: bool = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetParameterHistory')
    members = operation_model.input_shape.members


class GetParametersRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Names: list
    WithDecryption: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetParameters')
    members = operation_model.input_shape.members


class GetParametersByPathRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Path: str
    Recursive: bool = None
    ParameterFilters: list = None
    WithDecryption: bool = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetParametersByPath')
    members = operation_model.input_shape.members


class GetPatchBaselineRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BaselineId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetPatchBaseline')
    members = operation_model.input_shape.members


class GetPatchBaselineForPatchGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PatchGroup: str
    OperatingSystem: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('GetPatchBaselineForPatchGroup')
    members = operation_model.input_shape.members


class LabelParameterVersionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    Labels: list
    ParameterVersion: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('LabelParameterVersion')
    members = operation_model.input_shape.members


class ListAssociationVersionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListAssociationVersions')
    members = operation_model.input_shape.members


class ListAssociationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationFilterList: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListAssociations')
    members = operation_model.input_shape.members


class ListCommandInvocationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CommandId: str = None
    InstanceId: str = None
    MaxResults: int = None
    NextToken: str = None
    Filters: list = None
    Details: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListCommandInvocations')
    members = operation_model.input_shape.members


class ListCommandsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CommandId: str = None
    InstanceId: str = None
    MaxResults: int = None
    NextToken: str = None
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListCommands')
    members = operation_model.input_shape.members


class ListComplianceItemsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    ResourceIds: list = None
    ResourceTypes: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListComplianceItems')
    members = operation_model.input_shape.members


class ListComplianceSummariesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListComplianceSummaries')
    members = operation_model.input_shape.members


class ListDocumentVersionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListDocumentVersions')
    members = operation_model.input_shape.members


class ListDocumentsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DocumentFilterList: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListDocuments')
    members = operation_model.input_shape.members


class ListInventoryEntriesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    TypeName: str
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListInventoryEntries')
    members = operation_model.input_shape.members


class ListResourceComplianceSummariesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListResourceComplianceSummaries')
    members = operation_model.input_shape.members


class ListResourceDataSyncRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListResourceDataSync')
    members = operation_model.input_shape.members


class ListTagsForResourceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceType: str
    ResourceId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ListTagsForResource')
    members = operation_model.input_shape.members


class ModifyDocumentPermissionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    PermissionType: str
    AccountIdsToAdd: list = None
    AccountIdsToRemove: list = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ModifyDocumentPermission')
    members = operation_model.input_shape.members


class PutComplianceItemsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceId: str
    ResourceType: str
    ComplianceType: str
    ExecutionSummary: dict
    Items: list
    ItemContentHash: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('PutComplianceItems')
    members = operation_model.input_shape.members


class PutInventoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    Items: list

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('PutInventory')
    members = operation_model.input_shape.members


class PutParameterRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    Value: str
    Type: str
    Description: str = None
    KeyId: str = None
    Overwrite: bool = None
    AllowedPattern: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('PutParameter')
    members = operation_model.input_shape.members


class RegisterDefaultPatchBaselineRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BaselineId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('RegisterDefaultPatchBaseline')
    members = operation_model.input_shape.members


class RegisterPatchBaselineForPatchGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BaselineId: str
    PatchGroup: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('RegisterPatchBaselineForPatchGroup')
    members = operation_model.input_shape.members


class RegisterTargetWithMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    ResourceType: str
    Targets: list
    OwnerInformation: str = None
    Name: str = None
    Description: str = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('RegisterTargetWithMaintenanceWindow')
    members = operation_model.input_shape.members


class RegisterTaskWithMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    Targets: list
    TaskArn: str
    TaskType: str
    MaxConcurrency: str
    MaxErrors: str
    ServiceRoleArn: str = None
    TaskParameters: Map = None
    TaskInvocationParameters: dict = None
    Priority: int = None
    LoggingInfo: dict = None
    Name: str = None
    Description: str = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('RegisterTaskWithMaintenanceWindow')
    members = operation_model.input_shape.members


class RemoveTagsFromResourceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceType: str
    ResourceId: str
    TagKeys: list

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('RemoveTagsFromResource')
    members = operation_model.input_shape.members


class ResumeSessionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SessionId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('ResumeSession')
    members = operation_model.input_shape.members


class SendAutomationSignalRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AutomationExecutionId: str
    SignalType: str
    Payload: Map = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('SendAutomationSignal')
    members = operation_model.input_shape.members


class SendCommandRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DocumentName: str
    InstanceIds: list = None
    Targets: list = None
    DocumentVersion: str = None
    DocumentHash: str = None
    DocumentHashType: str = None
    TimeoutSeconds: int = None
    Comment: str = None
    Parameters: Map = None
    OutputS3Region: str = None
    OutputS3BucketName: str = None
    OutputS3KeyPrefix: str = None
    MaxConcurrency: str = None
    MaxErrors: str = None
    ServiceRoleArn: str = None
    NotificationConfig: dict = None
    CloudWatchOutputConfig: dict = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('SendCommand')
    members = operation_model.input_shape.members


class StartAssociationsOnceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationIds: list

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('StartAssociationsOnce')
    members = operation_model.input_shape.members


class StartAutomationExecutionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DocumentName: str
    DocumentVersion: str = None
    Parameters: Map = None
    ClientToken: str = None
    Mode: str = None
    TargetParameterName: str = None
    Targets: list = None
    TargetMaps: list = None
    MaxConcurrency: str = None
    MaxErrors: str = None
    TargetLocations: list = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('StartAutomationExecution')
    members = operation_model.input_shape.members


class StartSessionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Target: str
    DocumentName: str = None
    Parameters: Map = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('StartSession')
    members = operation_model.input_shape.members


class StopAutomationExecutionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AutomationExecutionId: str
    Type: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('StopAutomationExecution')
    members = operation_model.input_shape.members


class TerminateSessionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SessionId: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('TerminateSession')
    members = operation_model.input_shape.members


class UpdateAssociationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str
    Parameters: Map = None
    DocumentVersion: str = None
    ScheduleExpression: str = None
    OutputLocation: dict = None
    Name: str = None
    Targets: list = None
    AssociationName: str = None
    AssociationVersion: str = None
    MaxErrors: str = None
    MaxConcurrency: str = None
    ComplianceSeverity: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateAssociation')
    members = operation_model.input_shape.members


class UpdateAssociationStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    InstanceId: str
    AssociationStatus: dict

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateAssociationStatus')
    members = operation_model.input_shape.members


class UpdateDocumentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Content: str
    Name: str
    Attachments: list = None
    VersionName: str = None
    DocumentVersion: str = None
    DocumentFormat: str = None
    TargetType: str = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateDocument')
    members = operation_model.input_shape.members


class UpdateDocumentDefaultVersionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    DocumentVersion: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateDocumentDefaultVersion')
    members = operation_model.input_shape.members


class UpdateMaintenanceWindowRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    Name: str = None
    Description: str = None
    StartDate: str = None
    EndDate: str = None
    Schedule: str = None
    ScheduleTimezone: str = None
    Duration: int = None
    Cutoff: int = None
    AllowUnassociatedTargets: bool = None
    Enabled: bool = None
    Replace: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateMaintenanceWindow')
    members = operation_model.input_shape.members


class UpdateMaintenanceWindowTargetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    WindowTargetId: str
    Targets: list = None
    OwnerInformation: str = None
    Name: str = None
    Description: str = None
    Replace: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateMaintenanceWindowTarget')
    members = operation_model.input_shape.members


class UpdateMaintenanceWindowTaskRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WindowId: str
    WindowTaskId: str
    Targets: list = None
    TaskArn: str = None
    ServiceRoleArn: str = None
    TaskParameters: Map = None
    TaskInvocationParameters: dict = None
    Priority: int = None
    MaxConcurrency: str = None
    MaxErrors: str = None
    LoggingInfo: dict = None
    Name: str = None
    Description: str = None
    Replace: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateMaintenanceWindowTask')
    members = operation_model.input_shape.members


class UpdateManagedInstanceRoleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    IamRole: str

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdateManagedInstanceRole')
    members = operation_model.input_shape.members


class UpdatePatchBaselineRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BaselineId: str
    Name: str = None
    GlobalFilters: dict = None
    ApprovalRules: dict = None
    ApprovedPatches: list = None
    ApprovedPatchesComplianceLevel: str = None
    ApprovedPatchesEnableNonSecurity: bool = None
    RejectedPatches: list = None
    RejectedPatchesAction: str = None
    Description: str = None
    Sources: list = None
    Replace: bool = None

    operation_model = botocore.session.Session().get_service_model('ssm').operation_model('UpdatePatchBaseline')
    members = operation_model.input_shape.members
