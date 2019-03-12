
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AddRoleToDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    RoleArn: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('AddRoleToDBCluster')
    members = operation_model.input_shape.members


class AddSourceIdentifierToSubscriptionMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionName: str
    SourceIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('AddSourceIdentifierToSubscription')
    members = operation_model.input_shape.members


class AddTagsToResourceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceName: str
    Tags: list

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('AddTagsToResource')
    members = operation_model.input_shape.members


class ApplyPendingMaintenanceActionMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ApplyPendingMaintenanceAction')
    members = operation_model.input_shape.members


class AuthorizeDBSecurityGroupIngressMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSecurityGroupName: str
    CIDRIP: str = None
    EC2SecurityGroupName: str = None
    EC2SecurityGroupId: str = None
    EC2SecurityGroupOwnerId: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('AuthorizeDBSecurityGroupIngress')
    members = operation_model.input_shape.members


class BacktrackDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    BacktrackTo: TimeStamp
    Force: bool = None
    UseEarliestTimeOnPointInTimeUnavailable: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('BacktrackDBCluster')
    members = operation_model.input_shape.members


class CopyDBClusterParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CopyDBClusterParameterGroup')
    members = operation_model.input_shape.members


class CopyDBClusterSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: str = None
    PreSignedUrl: str = None
    CopyTags: bool = None
    Tags: list = None
    SourceRegion: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CopyDBClusterSnapshot')
    members = operation_model.input_shape.members


class CopyDBParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CopyDBParameterGroup')
    members = operation_model.input_shape.members


class CopyDBSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceDBSnapshotIdentifier: str
    TargetDBSnapshotIdentifier: str
    KmsKeyId: str = None
    Tags: list = None
    CopyTags: bool = None
    PreSignedUrl: str = None
    OptionGroupName: str = None
    SourceRegion: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CopyDBSnapshot')
    members = operation_model.input_shape.members


class CopyOptionGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceOptionGroupIdentifier: str
    TargetOptionGroupIdentifier: str
    TargetOptionGroupDescription: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CopyOptionGroup')
    members = operation_model.input_shape.members


class CreateDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: list = None
    BackupRetentionPeriod: int = None
    CharacterSetName: str = None
    DatabaseName: str = None
    DBClusterParameterGroupName: str = None
    VpcSecurityGroupIds: list = None
    DBSubnetGroupName: str = None
    EngineVersion: str = None
    Port: int = None
    MasterUsername: str = None
    MasterUserPassword: str = None
    OptionGroupName: str = None
    PreferredBackupWindow: str = None
    PreferredMaintenanceWindow: str = None
    ReplicationSourceIdentifier: str = None
    Tags: list = None
    StorageEncrypted: bool = None
    KmsKeyId: str = None
    PreSignedUrl: str = None
    EnableIAMDatabaseAuthentication: bool = None
    BacktrackWindow: int = None
    EnableCloudwatchLogsExports: list = None
    EngineMode: str = None
    ScalingConfiguration: dict = None
    DeletionProtection: bool = None
    GlobalClusterIdentifier: str = None
    SourceRegion: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBCluster')
    members = operation_model.input_shape.members


class CreateDBClusterEndpointMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: list = None
    ExcludedMembers: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBClusterEndpoint')
    members = operation_model.input_shape.members


class CreateDBClusterParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBClusterParameterGroup')
    members = operation_model.input_shape.members


class CreateDBClusterSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBClusterSnapshot')
    members = operation_model.input_shape.members


class CreateDBInstanceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBName: str = None
    AllocatedStorage: int = None
    MasterUsername: str = None
    MasterUserPassword: str = None
    DBSecurityGroups: list = None
    VpcSecurityGroupIds: list = None
    AvailabilityZone: str = None
    DBSubnetGroupName: str = None
    PreferredMaintenanceWindow: str = None
    DBParameterGroupName: str = None
    BackupRetentionPeriod: int = None
    PreferredBackupWindow: str = None
    Port: int = None
    MultiAZ: bool = None
    EngineVersion: str = None
    AutoMinorVersionUpgrade: bool = None
    LicenseModel: str = None
    Iops: int = None
    OptionGroupName: str = None
    CharacterSetName: str = None
    PubliclyAccessible: bool = None
    Tags: list = None
    DBClusterIdentifier: str = None
    StorageType: str = None
    TdeCredentialArn: str = None
    TdeCredentialPassword: str = None
    StorageEncrypted: bool = None
    KmsKeyId: str = None
    Domain: str = None
    CopyTagsToSnapshot: bool = None
    MonitoringInterval: int = None
    MonitoringRoleArn: str = None
    DomainIAMRoleName: str = None
    PromotionTier: int = None
    Timezone: str = None
    EnableIAMDatabaseAuthentication: bool = None
    EnablePerformanceInsights: bool = None
    PerformanceInsightsKMSKeyId: str = None
    PerformanceInsightsRetentionPeriod: int = None
    EnableCloudwatchLogsExports: list = None
    ProcessorFeatures: list = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBInstance')
    members = operation_model.input_shape.members


class CreateDBInstanceReadReplicaMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    SourceDBInstanceIdentifier: str
    DBInstanceClass: str = None
    AvailabilityZone: str = None
    Port: int = None
    MultiAZ: bool = None
    AutoMinorVersionUpgrade: bool = None
    Iops: int = None
    OptionGroupName: str = None
    PubliclyAccessible: bool = None
    Tags: list = None
    DBSubnetGroupName: str = None
    VpcSecurityGroupIds: list = None
    StorageType: str = None
    CopyTagsToSnapshot: bool = None
    MonitoringInterval: int = None
    MonitoringRoleArn: str = None
    KmsKeyId: str = None
    PreSignedUrl: str = None
    EnableIAMDatabaseAuthentication: bool = None
    EnablePerformanceInsights: bool = None
    PerformanceInsightsKMSKeyId: str = None
    PerformanceInsightsRetentionPeriod: int = None
    EnableCloudwatchLogsExports: list = None
    ProcessorFeatures: list = None
    UseDefaultProcessorFeatures: bool = None
    DeletionProtection: bool = None
    SourceRegion: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBInstanceReadReplica')
    members = operation_model.input_shape.members


class CreateDBParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBParameterGroup')
    members = operation_model.input_shape.members


class CreateDBSecurityGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSecurityGroupName: str
    DBSecurityGroupDescription: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBSecurityGroup')
    members = operation_model.input_shape.members


class CreateDBSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSnapshotIdentifier: str
    DBInstanceIdentifier: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBSnapshot')
    members = operation_model.input_shape.members


class CreateDBSubnetGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: list
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateDBSubnetGroup')
    members = operation_model.input_shape.members


class CreateEventSubscriptionMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionName: str
    SnsTopicArn: str
    SourceType: str = None
    EventCategories: list = None
    SourceIds: list = None
    Enabled: bool = None
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateEventSubscription')
    members = operation_model.input_shape.members


class CreateGlobalClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalClusterIdentifier: str = None
    SourceDBClusterIdentifier: str = None
    Engine: str = None
    EngineVersion: str = None
    DeletionProtection: bool = None
    DatabaseName: str = None
    StorageEncrypted: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateGlobalCluster')
    members = operation_model.input_shape.members


class CreateOptionGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OptionGroupName: str
    EngineName: str
    MajorEngineVersion: str
    OptionGroupDescription: str
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('CreateOptionGroup')
    members = operation_model.input_shape.members


class DeleteDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    SkipFinalSnapshot: bool = None
    FinalDBSnapshotIdentifier: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBCluster')
    members = operation_model.input_shape.members


class DeleteDBClusterEndpointMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterEndpointIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBClusterEndpoint')
    members = operation_model.input_shape.members


class DeleteDBClusterParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterParameterGroupName: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBClusterParameterGroup')
    members = operation_model.input_shape.members


class DeleteDBClusterSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterSnapshotIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBClusterSnapshot')
    members = operation_model.input_shape.members


class DeleteDBInstanceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    SkipFinalSnapshot: bool = None
    FinalDBSnapshotIdentifier: str = None
    DeleteAutomatedBackups: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBInstance')
    members = operation_model.input_shape.members


class DeleteDBInstanceAutomatedBackupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DbiResourceId: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBInstanceAutomatedBackup')
    members = operation_model.input_shape.members


class DeleteDBParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupName: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBParameterGroup')
    members = operation_model.input_shape.members


class DeleteDBSecurityGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSecurityGroupName: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBSecurityGroup')
    members = operation_model.input_shape.members


class DeleteDBSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSnapshotIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBSnapshot')
    members = operation_model.input_shape.members


class DeleteDBSubnetGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSubnetGroupName: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteDBSubnetGroup')
    members = operation_model.input_shape.members


class DeleteEventSubscriptionMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionName: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteEventSubscription')
    members = operation_model.input_shape.members


class DeleteGlobalClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalClusterIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteGlobalCluster')
    members = operation_model.input_shape.members


class DeleteOptionGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OptionGroupName: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DeleteOptionGroup')
    members = operation_model.input_shape.members


class DescribeAccountAttributesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeAccountAttributes')
    members = operation_model.input_shape.members


class DescribeCertificatesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CertificateIdentifier: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeCertificates')
    members = operation_model.input_shape.members


class DescribeDBClusterBacktracksMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    BacktrackIdentifier: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBClusterBacktracks')
    members = operation_model.input_shape.members


class DescribeDBClusterEndpointsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str = None
    DBClusterEndpointIdentifier: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBClusterEndpoints')
    members = operation_model.input_shape.members


class DescribeDBClusterParameterGroupsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterParameterGroupName: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBClusterParameterGroups')
    members = operation_model.input_shape.members


class DescribeDBClusterParametersMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterParameterGroupName: str
    Source: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBClusterParameters')
    members = operation_model.input_shape.members


class DescribeDBClusterSnapshotAttributesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterSnapshotIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBClusterSnapshotAttributes')
    members = operation_model.input_shape.members


class DescribeDBClusterSnapshotsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str = None
    DBClusterSnapshotIdentifier: str = None
    SnapshotType: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None
    IncludeShared: bool = None
    IncludePublic: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBClusterSnapshots')
    members = operation_model.input_shape.members


class DescribeDBClustersMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBClusters')
    members = operation_model.input_shape.members


class DescribeDBEngineVersionsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Engine: str = None
    EngineVersion: str = None
    DBParameterGroupFamily: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None
    DefaultOnly: bool = None
    ListSupportedCharacterSets: bool = None
    ListSupportedTimezones: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBEngineVersions')
    members = operation_model.input_shape.members


class DescribeDBInstanceAutomatedBackupsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DbiResourceId: str = None
    DBInstanceIdentifier: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBInstanceAutomatedBackups')
    members = operation_model.input_shape.members


class DescribeDBInstancesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBInstances')
    members = operation_model.input_shape.members


class DescribeDBLogFilesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    FilenameContains: str = None
    FileLastWritten: int = None
    FileSize: int = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBLogFiles')
    members = operation_model.input_shape.members


class DescribeDBParameterGroupsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupName: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBParameterGroups')
    members = operation_model.input_shape.members


class DescribeDBParametersMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupName: str
    Source: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBParameters')
    members = operation_model.input_shape.members


class DescribeDBSecurityGroupsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSecurityGroupName: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBSecurityGroups')
    members = operation_model.input_shape.members


class DescribeDBSnapshotAttributesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSnapshotIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBSnapshotAttributes')
    members = operation_model.input_shape.members


class DescribeDBSnapshotsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str = None
    DBSnapshotIdentifier: str = None
    SnapshotType: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None
    IncludeShared: bool = None
    IncludePublic: bool = None
    DbiResourceId: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBSnapshots')
    members = operation_model.input_shape.members


class DescribeDBSubnetGroupsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSubnetGroupName: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeDBSubnetGroups')
    members = operation_model.input_shape.members


class DescribeEngineDefaultClusterParametersMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupFamily: str
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeEngineDefaultClusterParameters')
    members = operation_model.input_shape.members


class DescribeEngineDefaultParametersMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupFamily: str
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeEngineDefaultParameters')
    members = operation_model.input_shape.members


class DescribeEventCategoriesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceType: str = None
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeEventCategories')
    members = operation_model.input_shape.members


class DescribeEventSubscriptionsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionName: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeEventSubscriptions')
    members = operation_model.input_shape.members


class DescribeEventsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceIdentifier: str = None
    SourceType: str = None
    StartTime: TimeStamp = None
    EndTime: TimeStamp = None
    Duration: int = None
    EventCategories: list = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeEvents')
    members = operation_model.input_shape.members


class DescribeGlobalClustersMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalClusterIdentifier: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeGlobalClusters')
    members = operation_model.input_shape.members


class DescribeOptionGroupOptionsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    EngineName: str
    MajorEngineVersion: str = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeOptionGroupOptions')
    members = operation_model.input_shape.members


class DescribeOptionGroupsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OptionGroupName: str = None
    Filters: list = None
    Marker: str = None
    MaxRecords: int = None
    EngineName: str = None
    MajorEngineVersion: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeOptionGroups')
    members = operation_model.input_shape.members


class DescribeOrderableDBInstanceOptionsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Engine: str
    EngineVersion: str = None
    DBInstanceClass: str = None
    LicenseModel: str = None
    Vpc: bool = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeOrderableDBInstanceOptions')
    members = operation_model.input_shape.members


class DescribePendingMaintenanceActionsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceIdentifier: str = None
    Filters: list = None
    Marker: str = None
    MaxRecords: int = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribePendingMaintenanceActions')
    members = operation_model.input_shape.members


class DescribeReservedDBInstancesMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ReservedDBInstanceId: str = None
    ReservedDBInstancesOfferingId: str = None
    DBInstanceClass: str = None
    Duration: str = None
    ProductDescription: str = None
    OfferingType: str = None
    MultiAZ: bool = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeReservedDBInstances')
    members = operation_model.input_shape.members


class DescribeReservedDBInstancesOfferingsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ReservedDBInstancesOfferingId: str = None
    DBInstanceClass: str = None
    Duration: str = None
    ProductDescription: str = None
    OfferingType: str = None
    MultiAZ: bool = None
    Filters: list = None
    MaxRecords: int = None
    Marker: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeReservedDBInstancesOfferings')
    members = operation_model.input_shape.members


class DescribeSourceRegionsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RegionName: str = None
    MaxRecords: int = None
    Marker: str = None
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeSourceRegions')
    members = operation_model.input_shape.members


class DescribeValidDBInstanceModificationsMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DescribeValidDBInstanceModifications')
    members = operation_model.input_shape.members


class DownloadDBLogFilePortionMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    LogFileName: str
    Marker: str = None
    NumberOfLines: int = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('DownloadDBLogFilePortion')
    members = operation_model.input_shape.members


class FailoverDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    TargetDBInstanceIdentifier: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('FailoverDBCluster')
    members = operation_model.input_shape.members


class ListTagsForResourceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceName: str
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ListTagsForResource')
    members = operation_model.input_shape.members


class ModifyCurrentDBClusterCapacityMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    Capacity: int = None
    SecondsBeforeTimeout: int = None
    TimeoutAction: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyCurrentDBClusterCapacity')
    members = operation_model.input_shape.members


class ModifyDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    NewDBClusterIdentifier: str = None
    ApplyImmediately: bool = None
    BackupRetentionPeriod: int = None
    DBClusterParameterGroupName: str = None
    VpcSecurityGroupIds: list = None
    Port: int = None
    MasterUserPassword: str = None
    OptionGroupName: str = None
    PreferredBackupWindow: str = None
    PreferredMaintenanceWindow: str = None
    EnableIAMDatabaseAuthentication: bool = None
    BacktrackWindow: int = None
    CloudwatchLogsExportConfiguration: dict = None
    EngineVersion: str = None
    ScalingConfiguration: dict = None
    DeletionProtection: bool = None
    EnableHttpEndpoint: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBCluster')
    members = operation_model.input_shape.members


class ModifyDBClusterEndpointMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterEndpointIdentifier: str
    EndpointType: str = None
    StaticMembers: list = None
    ExcludedMembers: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBClusterEndpoint')
    members = operation_model.input_shape.members


class ModifyDBClusterParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterParameterGroupName: str
    Parameters: list

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBClusterParameterGroup')
    members = operation_model.input_shape.members


class ModifyDBClusterSnapshotAttributeMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: list = None
    ValuesToRemove: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBClusterSnapshotAttribute')
    members = operation_model.input_shape.members


class ModifyDBInstanceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    AllocatedStorage: int = None
    DBInstanceClass: str = None
    DBSubnetGroupName: str = None
    DBSecurityGroups: list = None
    VpcSecurityGroupIds: list = None
    ApplyImmediately: bool = None
    MasterUserPassword: str = None
    DBParameterGroupName: str = None
    BackupRetentionPeriod: int = None
    PreferredBackupWindow: str = None
    PreferredMaintenanceWindow: str = None
    MultiAZ: bool = None
    EngineVersion: str = None
    AllowMajorVersionUpgrade: bool = None
    AutoMinorVersionUpgrade: bool = None
    LicenseModel: str = None
    Iops: int = None
    OptionGroupName: str = None
    NewDBInstanceIdentifier: str = None
    StorageType: str = None
    TdeCredentialArn: str = None
    TdeCredentialPassword: str = None
    CACertificateIdentifier: str = None
    Domain: str = None
    CopyTagsToSnapshot: bool = None
    MonitoringInterval: int = None
    DBPortNumber: int = None
    PubliclyAccessible: bool = None
    MonitoringRoleArn: str = None
    DomainIAMRoleName: str = None
    PromotionTier: int = None
    EnableIAMDatabaseAuthentication: bool = None
    EnablePerformanceInsights: bool = None
    PerformanceInsightsKMSKeyId: str = None
    PerformanceInsightsRetentionPeriod: int = None
    CloudwatchLogsExportConfiguration: dict = None
    ProcessorFeatures: list = None
    UseDefaultProcessorFeatures: bool = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBInstance')
    members = operation_model.input_shape.members


class ModifyDBParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupName: str
    Parameters: list

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBParameterGroup')
    members = operation_model.input_shape.members


class ModifyDBSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSnapshotIdentifier: str
    EngineVersion: str = None
    OptionGroupName: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBSnapshot')
    members = operation_model.input_shape.members


class ModifyDBSnapshotAttributeMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: list = None
    ValuesToRemove: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBSnapshotAttribute')
    members = operation_model.input_shape.members


class ModifyDBSubnetGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSubnetGroupName: str
    SubnetIds: list
    DBSubnetGroupDescription: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyDBSubnetGroup')
    members = operation_model.input_shape.members


class ModifyEventSubscriptionMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionName: str
    SnsTopicArn: str = None
    SourceType: str = None
    EventCategories: list = None
    Enabled: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyEventSubscription')
    members = operation_model.input_shape.members


class ModifyGlobalClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalClusterIdentifier: str = None
    NewGlobalClusterIdentifier: str = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyGlobalCluster')
    members = operation_model.input_shape.members


class ModifyOptionGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OptionGroupName: str
    OptionsToInclude: list = None
    OptionsToRemove: list = None
    ApplyImmediately: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ModifyOptionGroup')
    members = operation_model.input_shape.members


class PromoteReadReplicaMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    BackupRetentionPeriod: int = None
    PreferredBackupWindow: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('PromoteReadReplica')
    members = operation_model.input_shape.members


class PromoteReadReplicaDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('PromoteReadReplicaDBCluster')
    members = operation_model.input_shape.members


class PurchaseReservedDBInstancesOfferingMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ReservedDBInstancesOfferingId: str
    ReservedDBInstanceId: str = None
    DBInstanceCount: int = None
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('PurchaseReservedDBInstancesOffering')
    members = operation_model.input_shape.members


class RebootDBInstanceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    ForceFailover: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RebootDBInstance')
    members = operation_model.input_shape.members


class RemoveFromGlobalClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GlobalClusterIdentifier: str = None
    DbClusterIdentifier: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RemoveFromGlobalCluster')
    members = operation_model.input_shape.members


class RemoveRoleFromDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    RoleArn: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RemoveRoleFromDBCluster')
    members = operation_model.input_shape.members


class RemoveSourceIdentifierFromSubscriptionMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubscriptionName: str
    SourceIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RemoveSourceIdentifierFromSubscription')
    members = operation_model.input_shape.members


class RemoveTagsFromResourceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceName: str
    TagKeys: list

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RemoveTagsFromResource')
    members = operation_model.input_shape.members


class ResetDBClusterParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterParameterGroupName: str
    ResetAllParameters: bool = None
    Parameters: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ResetDBClusterParameterGroup')
    members = operation_model.input_shape.members


class ResetDBParameterGroupMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBParameterGroupName: str
    ResetAllParameters: bool = None
    Parameters: list = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('ResetDBParameterGroup')
    members = operation_model.input_shape.members


class RestoreDBClusterFromS3Message(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    Engine: str
    MasterUsername: str
    MasterUserPassword: str
    SourceEngine: str
    SourceEngineVersion: str
    S3BucketName: str
    S3IngestionRoleArn: str
    AvailabilityZones: list = None
    BackupRetentionPeriod: int = None
    CharacterSetName: str = None
    DatabaseName: str = None
    DBClusterParameterGroupName: str = None
    VpcSecurityGroupIds: list = None
    DBSubnetGroupName: str = None
    EngineVersion: str = None
    Port: int = None
    OptionGroupName: str = None
    PreferredBackupWindow: str = None
    PreferredMaintenanceWindow: str = None
    Tags: list = None
    StorageEncrypted: bool = None
    KmsKeyId: str = None
    EnableIAMDatabaseAuthentication: bool = None
    S3Prefix: str = None
    BacktrackWindow: int = None
    EnableCloudwatchLogsExports: list = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RestoreDBClusterFromS3')
    members = operation_model.input_shape.members


class RestoreDBClusterFromSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: list = None
    EngineVersion: str = None
    Port: int = None
    DBSubnetGroupName: str = None
    DatabaseName: str = None
    OptionGroupName: str = None
    VpcSecurityGroupIds: list = None
    Tags: list = None
    KmsKeyId: str = None
    EnableIAMDatabaseAuthentication: bool = None
    BacktrackWindow: int = None
    EnableCloudwatchLogsExports: list = None
    EngineMode: str = None
    ScalingConfiguration: dict = None
    DBClusterParameterGroupName: str = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RestoreDBClusterFromSnapshot')
    members = operation_model.input_shape.members


class RestoreDBClusterToPointInTimeMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str
    SourceDBClusterIdentifier: str
    RestoreType: str = None
    RestoreToTime: TimeStamp = None
    UseLatestRestorableTime: bool = None
    Port: int = None
    DBSubnetGroupName: str = None
    OptionGroupName: str = None
    VpcSecurityGroupIds: list = None
    Tags: list = None
    KmsKeyId: str = None
    EnableIAMDatabaseAuthentication: bool = None
    BacktrackWindow: int = None
    EnableCloudwatchLogsExports: list = None
    DBClusterParameterGroupName: str = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RestoreDBClusterToPointInTime')
    members = operation_model.input_shape.members


class RestoreDBInstanceFromDBSnapshotMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    DBSnapshotIdentifier: str
    DBInstanceClass: str = None
    Port: int = None
    AvailabilityZone: str = None
    DBSubnetGroupName: str = None
    MultiAZ: bool = None
    PubliclyAccessible: bool = None
    AutoMinorVersionUpgrade: bool = None
    LicenseModel: str = None
    DBName: str = None
    Engine: str = None
    Iops: int = None
    OptionGroupName: str = None
    Tags: list = None
    StorageType: str = None
    TdeCredentialArn: str = None
    TdeCredentialPassword: str = None
    VpcSecurityGroupIds: list = None
    Domain: str = None
    CopyTagsToSnapshot: bool = None
    DomainIAMRoleName: str = None
    EnableIAMDatabaseAuthentication: bool = None
    EnableCloudwatchLogsExports: list = None
    ProcessorFeatures: list = None
    UseDefaultProcessorFeatures: bool = None
    DBParameterGroupName: str = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RestoreDBInstanceFromDBSnapshot')
    members = operation_model.input_shape.members


class RestoreDBInstanceFromS3Message(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    SourceEngine: str
    SourceEngineVersion: str
    S3BucketName: str
    S3IngestionRoleArn: str
    DBName: str = None
    AllocatedStorage: int = None
    MasterUsername: str = None
    MasterUserPassword: str = None
    DBSecurityGroups: list = None
    VpcSecurityGroupIds: list = None
    AvailabilityZone: str = None
    DBSubnetGroupName: str = None
    PreferredMaintenanceWindow: str = None
    DBParameterGroupName: str = None
    BackupRetentionPeriod: int = None
    PreferredBackupWindow: str = None
    Port: int = None
    MultiAZ: bool = None
    EngineVersion: str = None
    AutoMinorVersionUpgrade: bool = None
    LicenseModel: str = None
    Iops: int = None
    OptionGroupName: str = None
    PubliclyAccessible: bool = None
    Tags: list = None
    StorageType: str = None
    StorageEncrypted: bool = None
    KmsKeyId: str = None
    CopyTagsToSnapshot: bool = None
    MonitoringInterval: int = None
    MonitoringRoleArn: str = None
    EnableIAMDatabaseAuthentication: bool = None
    S3Prefix: str = None
    EnablePerformanceInsights: bool = None
    PerformanceInsightsKMSKeyId: str = None
    PerformanceInsightsRetentionPeriod: int = None
    EnableCloudwatchLogsExports: list = None
    ProcessorFeatures: list = None
    UseDefaultProcessorFeatures: bool = None
    DeletionProtection: bool = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RestoreDBInstanceFromS3')
    members = operation_model.input_shape.members


class RestoreDBInstanceToPointInTimeMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TargetDBInstanceIdentifier: str
    SourceDBInstanceIdentifier: str = None
    RestoreTime: TimeStamp = None
    UseLatestRestorableTime: bool = None
    DBInstanceClass: str = None
    Port: int = None
    AvailabilityZone: str = None
    DBSubnetGroupName: str = None
    MultiAZ: bool = None
    PubliclyAccessible: bool = None
    AutoMinorVersionUpgrade: bool = None
    LicenseModel: str = None
    DBName: str = None
    Engine: str = None
    Iops: int = None
    OptionGroupName: str = None
    CopyTagsToSnapshot: bool = None
    Tags: list = None
    StorageType: str = None
    TdeCredentialArn: str = None
    TdeCredentialPassword: str = None
    VpcSecurityGroupIds: list = None
    Domain: str = None
    DomainIAMRoleName: str = None
    EnableIAMDatabaseAuthentication: bool = None
    EnableCloudwatchLogsExports: list = None
    ProcessorFeatures: list = None
    UseDefaultProcessorFeatures: bool = None
    DBParameterGroupName: str = None
    DeletionProtection: bool = None
    SourceDbiResourceId: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RestoreDBInstanceToPointInTime')
    members = operation_model.input_shape.members


class RevokeDBSecurityGroupIngressMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBSecurityGroupName: str
    CIDRIP: str = None
    EC2SecurityGroupName: str = None
    EC2SecurityGroupId: str = None
    EC2SecurityGroupOwnerId: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('RevokeDBSecurityGroupIngress')
    members = operation_model.input_shape.members


class StartDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('StartDBCluster')
    members = operation_model.input_shape.members


class StartDBInstanceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('StartDBInstance')
    members = operation_model.input_shape.members


class StopDBClusterMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBClusterIdentifier: str

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('StopDBCluster')
    members = operation_model.input_shape.members


class StopDBInstanceMessage(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DBInstanceIdentifier: str
    DBSnapshotIdentifier: str = None

    operation_model = botocore.session.Session().get_service_model('rds').operation_model('StopDBInstance')
    members = operation_model.input_shape.members
