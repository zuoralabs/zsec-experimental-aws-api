
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AcceptReservedInstancesExchangeQuoteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ReservedInstanceIds: list
    DryRun: bool = None
    TargetConfigurations: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AcceptReservedInstancesExchangeQuote')
    members = operation_model.input_shape.members


class AcceptTransitGatewayVpcAttachmentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayAttachmentId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AcceptTransitGatewayVpcAttachment')
    members = operation_model.input_shape.members


class AcceptVpcEndpointConnectionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServiceId: str
    VpcEndpointIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AcceptVpcEndpointConnections')
    members = operation_model.input_shape.members


class AcceptVpcPeeringConnectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    VpcPeeringConnectionId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AcceptVpcPeeringConnection')
    members = operation_model.input_shape.members


class AdvertiseByoipCidrRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Cidr: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AdvertiseByoipCidr')
    members = operation_model.input_shape.members


class AllocateAddressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Domain: str = None
    Address: str = None
    PublicIpv4Pool: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AllocateAddress')
    members = operation_model.input_shape.members


class AllocateHostsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AvailabilityZone: str
    InstanceType: str
    Quantity: int
    AutoPlacement: str = None
    ClientToken: str = None
    TagSpecifications: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AllocateHosts')
    members = operation_model.input_shape.members


class AssignIpv6AddressesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    Ipv6AddressCount: int = None
    Ipv6Addresses: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssignIpv6Addresses')
    members = operation_model.input_shape.members


class AssignPrivateIpAddressesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    AllowReassignment: bool = None
    PrivateIpAddresses: list = None
    SecondaryPrivateIpAddressCount: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssignPrivateIpAddresses')
    members = operation_model.input_shape.members


class AssociateAddressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AllocationId: str = None
    InstanceId: str = None
    PublicIp: str = None
    AllowReassociation: bool = None
    DryRun: bool = None
    NetworkInterfaceId: str = None
    PrivateIpAddress: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssociateAddress')
    members = operation_model.input_shape.members


class AssociateDhcpOptionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DhcpOptionsId: str
    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssociateDhcpOptions')
    members = operation_model.input_shape.members


class AssociateIamInstanceProfileRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IamInstanceProfile: dict
    InstanceId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssociateIamInstanceProfile')
    members = operation_model.input_shape.members


class AssociateRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RouteTableId: str
    SubnetId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssociateRouteTable')
    members = operation_model.input_shape.members


class AssociateSubnetCidrBlockRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Ipv6CidrBlock: str
    SubnetId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssociateSubnetCidrBlock')
    members = operation_model.input_shape.members


class AssociateTransitGatewayRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssociateTransitGatewayRouteTable')
    members = operation_model.input_shape.members


class AssociateVpcCidrBlockRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    AmazonProvidedIpv6CidrBlock: bool = None
    CidrBlock: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AssociateVpcCidrBlock')
    members = operation_model.input_shape.members


class AttachClassicLinkVpcRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Groups: list
    InstanceId: str
    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AttachClassicLinkVpc')
    members = operation_model.input_shape.members


class AttachInternetGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InternetGatewayId: str
    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AttachInternetGateway')
    members = operation_model.input_shape.members


class AttachNetworkInterfaceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DeviceIndex: int
    InstanceId: str
    NetworkInterfaceId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AttachNetworkInterface')
    members = operation_model.input_shape.members


class AttachVolumeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Device: str
    InstanceId: str
    VolumeId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AttachVolume')
    members = operation_model.input_shape.members


class AttachVpnGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    VpnGatewayId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AttachVpnGateway')
    members = operation_model.input_shape.members


class AuthorizeSecurityGroupEgressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GroupId: str
    DryRun: bool = None
    IpPermissions: list = None
    CidrIp: str = None
    FromPort: int = None
    IpProtocol: str = None
    ToPort: int = None
    SourceSecurityGroupName: str = None
    SourceSecurityGroupOwnerId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AuthorizeSecurityGroupEgress')
    members = operation_model.input_shape.members


class AuthorizeSecurityGroupIngressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CidrIp: str = None
    FromPort: int = None
    GroupId: str = None
    GroupName: str = None
    IpPermissions: list = None
    IpProtocol: str = None
    SourceSecurityGroupName: str = None
    SourceSecurityGroupOwnerId: str = None
    ToPort: int = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('AuthorizeSecurityGroupIngress')
    members = operation_model.input_shape.members


class BundleInstanceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    Storage: dict
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('BundleInstance')
    members = operation_model.input_shape.members


class CancelBundleTaskRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BundleId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelBundleTask')
    members = operation_model.input_shape.members


class CancelCapacityReservationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CapacityReservationId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelCapacityReservation')
    members = operation_model.input_shape.members


class CancelConversionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConversionTaskId: str
    DryRun: bool = None
    ReasonMessage: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelConversionTask')
    members = operation_model.input_shape.members


class CancelExportTaskRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ExportTaskId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelExportTask')
    members = operation_model.input_shape.members


class CancelImportTaskRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CancelReason: str = None
    DryRun: bool = None
    ImportTaskId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelImportTask')
    members = operation_model.input_shape.members


class CancelReservedInstancesListingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ReservedInstancesListingId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelReservedInstancesListing')
    members = operation_model.input_shape.members


class CancelSpotFleetRequestsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SpotFleetRequestIds: list
    TerminateInstances: bool
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelSpotFleetRequests')
    members = operation_model.input_shape.members


class CancelSpotInstanceRequestsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SpotInstanceRequestIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CancelSpotInstanceRequests')
    members = operation_model.input_shape.members


class ConfirmProductInstanceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    ProductCode: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ConfirmProductInstance')
    members = operation_model.input_shape.members


class CopyFpgaImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceFpgaImageId: str
    SourceRegion: str
    DryRun: bool = None
    Description: str = None
    Name: str = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CopyFpgaImage')
    members = operation_model.input_shape.members


class CopyImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    SourceImageId: str
    SourceRegion: str
    ClientToken: str = None
    Description: str = None
    Encrypted: bool = None
    KmsKeyId: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CopyImage')
    members = operation_model.input_shape.members


class CopySnapshotRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SourceRegion: str
    SourceSnapshotId: str
    Description: str = None
    DestinationRegion: str = None
    Encrypted: bool = None
    KmsKeyId: str = None
    PresignedUrl: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CopySnapshot')
    members = operation_model.input_shape.members


class CreateCapacityReservationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceType: str
    InstancePlatform: str
    AvailabilityZone: str
    InstanceCount: int
    ClientToken: str = None
    Tenancy: str = None
    EbsOptimized: bool = None
    EphemeralStorage: bool = None
    EndDate: TimeStamp = None
    EndDateType: str = None
    InstanceMatchCriteria: str = None
    TagSpecifications: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateCapacityReservation')
    members = operation_model.input_shape.members


class CreateCustomerGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BgpAsn: int
    PublicIp: str
    Type: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateCustomerGateway')
    members = operation_model.input_shape.members


class CreateDefaultSubnetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AvailabilityZone: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateDefaultSubnet')
    members = operation_model.input_shape.members


class CreateDefaultVpcRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateDefaultVpc')
    members = operation_model.input_shape.members


class CreateDhcpOptionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DhcpConfigurations: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateDhcpOptions')
    members = operation_model.input_shape.members


class CreateEgressOnlyInternetGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    ClientToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateEgressOnlyInternetGateway')
    members = operation_model.input_shape.members


class CreateFleetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    LaunchTemplateConfigs: list
    TargetCapacitySpecification: dict
    DryRun: bool = None
    ClientToken: str = None
    SpotOptions: dict = None
    OnDemandOptions: dict = None
    ExcessCapacityTerminationPolicy: str = None
    TerminateInstancesWithExpiration: bool = None
    Type: str = None
    ValidFrom: TimeStamp = None
    ValidUntil: TimeStamp = None
    ReplaceUnhealthyInstances: bool = None
    TagSpecifications: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateFleet')
    members = operation_model.input_shape.members


class CreateFlowLogsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceIds: list
    ResourceType: str
    TrafficType: str
    DryRun: bool = None
    ClientToken: str = None
    DeliverLogsPermissionArn: str = None
    LogGroupName: str = None
    LogDestinationType: str = None
    LogDestination: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateFlowLogs')
    members = operation_model.input_shape.members


class CreateFpgaImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InputStorageLocation: dict
    DryRun: bool = None
    LogsStorageLocation: dict = None
    Description: str = None
    Name: str = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateFpgaImage')
    members = operation_model.input_shape.members


class CreateImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    Name: str
    BlockDeviceMappings: list = None
    Description: str = None
    DryRun: bool = None
    NoReboot: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateImage')
    members = operation_model.input_shape.members


class CreateInstanceExportTaskRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    Description: str = None
    ExportToS3Task: dict = None
    TargetEnvironment: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateInstanceExportTask')
    members = operation_model.input_shape.members


class CreateInternetGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateInternetGateway')
    members = operation_model.input_shape.members


class CreateKeyPairRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    KeyName: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateKeyPair')
    members = operation_model.input_shape.members


class CreateLaunchTemplateRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    LaunchTemplateName: str
    LaunchTemplateData: dict
    DryRun: bool = None
    ClientToken: str = None
    VersionDescription: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateLaunchTemplate')
    members = operation_model.input_shape.members


class CreateLaunchTemplateVersionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    LaunchTemplateData: dict
    DryRun: bool = None
    ClientToken: str = None
    LaunchTemplateId: str = None
    LaunchTemplateName: str = None
    SourceVersion: str = None
    VersionDescription: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateLaunchTemplateVersion')
    members = operation_model.input_shape.members


class CreateNatGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AllocationId: str
    SubnetId: str
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateNatGateway')
    members = operation_model.input_shape.members


class CreateNetworkAclRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateNetworkAcl')
    members = operation_model.input_shape.members


class CreateNetworkAclEntryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Egress: bool
    NetworkAclId: str
    Protocol: str
    RuleAction: str
    RuleNumber: int
    CidrBlock: str = None
    DryRun: bool = None
    IcmpTypeCode: dict = None
    Ipv6CidrBlock: str = None
    PortRange: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateNetworkAclEntry')
    members = operation_model.input_shape.members


class CreateNetworkInterfaceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubnetId: str
    Description: str = None
    DryRun: bool = None
    Groups: list = None
    Ipv6AddressCount: int = None
    Ipv6Addresses: list = None
    PrivateIpAddress: str = None
    PrivateIpAddresses: list = None
    SecondaryPrivateIpAddressCount: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateNetworkInterface')
    members = operation_model.input_shape.members


class CreateNetworkInterfacePermissionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    Permission: str
    AwsAccountId: str = None
    AwsService: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateNetworkInterfacePermission')
    members = operation_model.input_shape.members


class CreatePlacementGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GroupName: str
    Strategy: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreatePlacementGroup')
    members = operation_model.input_shape.members


class CreateReservedInstancesListingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ClientToken: str
    InstanceCount: int
    PriceSchedules: list
    ReservedInstancesId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateReservedInstancesListing')
    members = operation_model.input_shape.members


class CreateRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RouteTableId: str
    DestinationCidrBlock: str = None
    DestinationIpv6CidrBlock: str = None
    DryRun: bool = None
    EgressOnlyInternetGatewayId: str = None
    GatewayId: str = None
    InstanceId: str = None
    NatGatewayId: str = None
    TransitGatewayId: str = None
    NetworkInterfaceId: str = None
    VpcPeeringConnectionId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateRoute')
    members = operation_model.input_shape.members


class CreateRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateRouteTable')
    members = operation_model.input_shape.members


class CreateSecurityGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Description: str
    GroupName: str
    VpcId: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateSecurityGroup')
    members = operation_model.input_shape.members


class CreateSnapshotRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VolumeId: str
    Description: str = None
    TagSpecifications: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateSnapshot')
    members = operation_model.input_shape.members


class CreateSpotDatafeedSubscriptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    DryRun: bool = None
    Prefix: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateSpotDatafeedSubscription')
    members = operation_model.input_shape.members


class CreateSubnetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CidrBlock: str
    VpcId: str
    AvailabilityZone: str = None
    AvailabilityZoneId: str = None
    Ipv6CidrBlock: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateSubnet')
    members = operation_model.input_shape.members


class CreateTagsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Resources: list
    Tags: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateTags')
    members = operation_model.input_shape.members


class CreateTransitGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Description: str = None
    Options: dict = None
    TagSpecifications: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateTransitGateway')
    members = operation_model.input_shape.members


class CreateTransitGatewayRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str = None
    Blackhole: bool = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateTransitGatewayRoute')
    members = operation_model.input_shape.members


class CreateTransitGatewayRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayId: str
    TagSpecifications: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateTransitGatewayRouteTable')
    members = operation_model.input_shape.members


class CreateTransitGatewayVpcAttachmentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayId: str
    VpcId: str
    SubnetIds: list
    Options: dict = None
    TagSpecifications: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateTransitGatewayVpcAttachment')
    members = operation_model.input_shape.members


class CreateVolumeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AvailabilityZone: str
    Encrypted: bool = None
    Iops: int = None
    KmsKeyId: str = None
    Size: int = None
    SnapshotId: str = None
    VolumeType: str = None
    DryRun: bool = None
    TagSpecifications: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVolume')
    members = operation_model.input_shape.members


class CreateVpcRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CidrBlock: str
    AmazonProvidedIpv6CidrBlock: bool = None
    DryRun: bool = None
    InstanceTenancy: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpc')
    members = operation_model.input_shape.members


class CreateVpcEndpointRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    ServiceName: str
    DryRun: bool = None
    VpcEndpointType: str = None
    PolicyDocument: str = None
    RouteTableIds: list = None
    SubnetIds: list = None
    SecurityGroupIds: list = None
    ClientToken: str = None
    PrivateDnsEnabled: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpcEndpoint')
    members = operation_model.input_shape.members


class CreateVpcEndpointConnectionNotificationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConnectionNotificationArn: str
    ConnectionEvents: list
    DryRun: bool = None
    ServiceId: str = None
    VpcEndpointId: str = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpcEndpointConnectionNotification')
    members = operation_model.input_shape.members


class CreateVpcEndpointServiceConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkLoadBalancerArns: list
    DryRun: bool = None
    AcceptanceRequired: bool = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpcEndpointServiceConfiguration')
    members = operation_model.input_shape.members


class CreateVpcPeeringConnectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    PeerOwnerId: str = None
    PeerVpcId: str = None
    VpcId: str = None
    PeerRegion: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpcPeeringConnection')
    members = operation_model.input_shape.members


class CreateVpnConnectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CustomerGatewayId: str
    Type: str
    VpnGatewayId: str = None
    TransitGatewayId: str = None
    DryRun: bool = None
    Options: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpnConnection')
    members = operation_model.input_shape.members


class CreateVpnConnectionRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DestinationCidrBlock: str
    VpnConnectionId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpnConnectionRoute')
    members = operation_model.input_shape.members


class CreateVpnGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Type: str
    AvailabilityZone: str = None
    AmazonSideAsn: int = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('CreateVpnGateway')
    members = operation_model.input_shape.members


class DeleteCustomerGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CustomerGatewayId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteCustomerGateway')
    members = operation_model.input_shape.members


class DeleteDhcpOptionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DhcpOptionsId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteDhcpOptions')
    members = operation_model.input_shape.members


class DeleteEgressOnlyInternetGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    EgressOnlyInternetGatewayId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteEgressOnlyInternetGateway')
    members = operation_model.input_shape.members


class DeleteFleetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FleetIds: list
    TerminateInstances: bool
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteFleets')
    members = operation_model.input_shape.members


class DeleteFlowLogsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FlowLogIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteFlowLogs')
    members = operation_model.input_shape.members


class DeleteFpgaImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FpgaImageId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteFpgaImage')
    members = operation_model.input_shape.members


class DeleteInternetGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InternetGatewayId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteInternetGateway')
    members = operation_model.input_shape.members


class DeleteKeyPairRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    KeyName: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteKeyPair')
    members = operation_model.input_shape.members


class DeleteLaunchTemplateRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    LaunchTemplateId: str = None
    LaunchTemplateName: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteLaunchTemplate')
    members = operation_model.input_shape.members


class DeleteLaunchTemplateVersionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Versions: list
    DryRun: bool = None
    LaunchTemplateId: str = None
    LaunchTemplateName: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteLaunchTemplateVersions')
    members = operation_model.input_shape.members


class DeleteNatGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NatGatewayId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteNatGateway')
    members = operation_model.input_shape.members


class DeleteNetworkAclRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkAclId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteNetworkAcl')
    members = operation_model.input_shape.members


class DeleteNetworkAclEntryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Egress: bool
    NetworkAclId: str
    RuleNumber: int
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteNetworkAclEntry')
    members = operation_model.input_shape.members


class DeleteNetworkInterfaceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteNetworkInterface')
    members = operation_model.input_shape.members


class DeleteNetworkInterfacePermissionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfacePermissionId: str
    Force: bool = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteNetworkInterfacePermission')
    members = operation_model.input_shape.members


class DeletePlacementGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GroupName: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeletePlacementGroup')
    members = operation_model.input_shape.members


class DeleteRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RouteTableId: str
    DestinationCidrBlock: str = None
    DestinationIpv6CidrBlock: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteRoute')
    members = operation_model.input_shape.members


class DeleteRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RouteTableId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteRouteTable')
    members = operation_model.input_shape.members


class DeleteSecurityGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GroupId: str = None
    GroupName: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteSecurityGroup')
    members = operation_model.input_shape.members


class DeleteSnapshotRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SnapshotId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteSnapshot')
    members = operation_model.input_shape.members


class DeleteSpotDatafeedSubscriptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteSpotDatafeedSubscription')
    members = operation_model.input_shape.members


class DeleteSubnetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubnetId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteSubnet')
    members = operation_model.input_shape.members


class DeleteTagsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Resources: list
    DryRun: bool = None
    Tags: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteTags')
    members = operation_model.input_shape.members


class DeleteTransitGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteTransitGateway')
    members = operation_model.input_shape.members


class DeleteTransitGatewayRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    DestinationCidrBlock: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteTransitGatewayRoute')
    members = operation_model.input_shape.members


class DeleteTransitGatewayRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteTransitGatewayRouteTable')
    members = operation_model.input_shape.members


class DeleteTransitGatewayVpcAttachmentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayAttachmentId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteTransitGatewayVpcAttachment')
    members = operation_model.input_shape.members


class DeleteVolumeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VolumeId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVolume')
    members = operation_model.input_shape.members


class DeleteVpcRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpc')
    members = operation_model.input_shape.members


class DeleteVpcEndpointConnectionNotificationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConnectionNotificationIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpcEndpointConnectionNotifications')
    members = operation_model.input_shape.members


class DeleteVpcEndpointServiceConfigurationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServiceIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpcEndpointServiceConfigurations')
    members = operation_model.input_shape.members


class DeleteVpcEndpointsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcEndpointIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpcEndpoints')
    members = operation_model.input_shape.members


class DeleteVpcPeeringConnectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcPeeringConnectionId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpcPeeringConnection')
    members = operation_model.input_shape.members


class DeleteVpnConnectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpnConnectionId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpnConnection')
    members = operation_model.input_shape.members


class DeleteVpnConnectionRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DestinationCidrBlock: str
    VpnConnectionId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpnConnectionRoute')
    members = operation_model.input_shape.members


class DeleteVpnGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpnGatewayId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeleteVpnGateway')
    members = operation_model.input_shape.members


class DeprovisionByoipCidrRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Cidr: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeprovisionByoipCidr')
    members = operation_model.input_shape.members


class DeregisterImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ImageId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DeregisterImage')
    members = operation_model.input_shape.members


class DescribeAccountAttributesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AttributeNames: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeAccountAttributes')
    members = operation_model.input_shape.members


class DescribeAddressesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    PublicIps: list = None
    AllocationIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeAddresses')
    members = operation_model.input_shape.members


class DescribeAggregateIdFormatRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeAggregateIdFormat')
    members = operation_model.input_shape.members


class DescribeAvailabilityZonesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    ZoneNames: list = None
    ZoneIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeAvailabilityZones')
    members = operation_model.input_shape.members


class DescribeBundleTasksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    BundleIds: list = None
    Filters: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeBundleTasks')
    members = operation_model.input_shape.members


class DescribeByoipCidrsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    MaxResults: int
    DryRun: bool = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeByoipCidrs')
    members = operation_model.input_shape.members


class DescribeCapacityReservationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CapacityReservationIds: list = None
    NextToken: str = None
    MaxResults: int = None
    Filters: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeCapacityReservations')
    members = operation_model.input_shape.members


class DescribeClassicLinkInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    InstanceIds: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeClassicLinkInstances')
    members = operation_model.input_shape.members


class DescribeConversionTasksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConversionTaskIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeConversionTasks')
    members = operation_model.input_shape.members


class DescribeCustomerGatewaysRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CustomerGatewayIds: list = None
    Filters: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeCustomerGateways')
    members = operation_model.input_shape.members


class DescribeDhcpOptionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DhcpOptionsIds: list = None
    Filters: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeDhcpOptions')
    members = operation_model.input_shape.members


class DescribeEgressOnlyInternetGatewaysRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    EgressOnlyInternetGatewayIds: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeEgressOnlyInternetGateways')
    members = operation_model.input_shape.members


class DescribeElasticGpusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ElasticGpuIds: list = None
    DryRun: bool = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeElasticGpus')
    members = operation_model.input_shape.members


class DescribeExportTasksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ExportTaskIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeExportTasks')
    members = operation_model.input_shape.members


class DescribeFleetHistoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FleetId: str
    StartTime: TimeStamp
    DryRun: bool = None
    EventType: str = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeFleetHistory')
    members = operation_model.input_shape.members


class DescribeFleetInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FleetId: str
    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeFleetInstances')
    members = operation_model.input_shape.members


class DescribeFleetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None
    FleetIds: list = None
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeFleets')
    members = operation_model.input_shape.members


class DescribeFlowLogsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filter: list = None
    FlowLogIds: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeFlowLogs')
    members = operation_model.input_shape.members


class DescribeFpgaImageAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FpgaImageId: str
    Attribute: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeFpgaImageAttribute')
    members = operation_model.input_shape.members


class DescribeFpgaImagesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    FpgaImageIds: list = None
    Owners: list = None
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeFpgaImages')
    members = operation_model.input_shape.members


class DescribeHostReservationOfferingsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filter: list = None
    MaxDuration: int = None
    MaxResults: int = None
    MinDuration: int = None
    NextToken: str = None
    OfferingId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeHostReservationOfferings')
    members = operation_model.input_shape.members


class DescribeHostReservationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filter: list = None
    HostReservationIdSet: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeHostReservations')
    members = operation_model.input_shape.members


class DescribeHostsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filter: list = None
    HostIds: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeHosts')
    members = operation_model.input_shape.members


class DescribeIamInstanceProfileAssociationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationIds: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeIamInstanceProfileAssociations')
    members = operation_model.input_shape.members


class DescribeIdFormatRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Resource: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeIdFormat')
    members = operation_model.input_shape.members


class DescribeIdentityIdFormatRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PrincipalArn: str
    Resource: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeIdentityIdFormat')
    members = operation_model.input_shape.members


class DescribeImageAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    ImageId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeImageAttribute')
    members = operation_model.input_shape.members


class DescribeImagesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ExecutableUsers: list = None
    Filters: list = None
    ImageIds: list = None
    Owners: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeImages')
    members = operation_model.input_shape.members


class DescribeImportImageTasksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filters: list = None
    ImportTaskIds: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeImportImageTasks')
    members = operation_model.input_shape.members


class DescribeImportSnapshotTasksRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filters: list = None
    ImportTaskIds: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeImportSnapshotTasks')
    members = operation_model.input_shape.members


class DescribeInstanceAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    InstanceId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeInstanceAttribute')
    members = operation_model.input_shape.members


class DescribeInstanceCreditSpecificationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filters: list = None
    InstanceIds: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeInstanceCreditSpecifications')
    members = operation_model.input_shape.members


class DescribeInstanceStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    InstanceIds: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None
    IncludeAllInstances: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeInstanceStatus')
    members = operation_model.input_shape.members


class DescribeInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    InstanceIds: list = None
    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeInstances')
    members = operation_model.input_shape.members


class DescribeInternetGatewaysRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    InternetGatewayIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeInternetGateways')
    members = operation_model.input_shape.members


class DescribeKeyPairsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    KeyNames: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeKeyPairs')
    members = operation_model.input_shape.members


class DescribeLaunchTemplateVersionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    LaunchTemplateId: str = None
    LaunchTemplateName: str = None
    Versions: list = None
    MinVersion: str = None
    MaxVersion: str = None
    NextToken: str = None
    MaxResults: int = None
    Filters: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeLaunchTemplateVersions')
    members = operation_model.input_shape.members


class DescribeLaunchTemplatesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    LaunchTemplateIds: list = None
    LaunchTemplateNames: list = None
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeLaunchTemplates')
    members = operation_model.input_shape.members


class DescribeMovingAddressesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None
    PublicIps: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeMovingAddresses')
    members = operation_model.input_shape.members


class DescribeNatGatewaysRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filter: list = None
    MaxResults: int = None
    NatGatewayIds: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeNatGateways')
    members = operation_model.input_shape.members


class DescribeNetworkAclsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    NetworkAclIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeNetworkAcls')
    members = operation_model.input_shape.members


class DescribeNetworkInterfaceAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    Attribute: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeNetworkInterfaceAttribute')
    members = operation_model.input_shape.members


class DescribeNetworkInterfacePermissionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfacePermissionIds: list = None
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeNetworkInterfacePermissions')
    members = operation_model.input_shape.members


class DescribeNetworkInterfacesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    NetworkInterfaceIds: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeNetworkInterfaces')
    members = operation_model.input_shape.members


class DescribePlacementGroupsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    GroupNames: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribePlacementGroups')
    members = operation_model.input_shape.members


class DescribePrefixListsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    PrefixListIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribePrefixLists')
    members = operation_model.input_shape.members


class DescribePrincipalIdFormatRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Resources: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribePrincipalIdFormat')
    members = operation_model.input_shape.members


class DescribePublicIpv4PoolsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PoolIds: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribePublicIpv4Pools')
    members = operation_model.input_shape.members


class DescribeRegionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    RegionNames: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeRegions')
    members = operation_model.input_shape.members


class DescribeReservedInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    OfferingClass: str = None
    ReservedInstancesIds: list = None
    DryRun: bool = None
    OfferingType: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeReservedInstances')
    members = operation_model.input_shape.members


class DescribeReservedInstancesListingsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    ReservedInstancesId: str = None
    ReservedInstancesListingId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeReservedInstancesListings')
    members = operation_model.input_shape.members


class DescribeReservedInstancesModificationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    ReservedInstancesModificationIds: list = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeReservedInstancesModifications')
    members = operation_model.input_shape.members


class DescribeReservedInstancesOfferingsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AvailabilityZone: str = None
    Filters: list = None
    IncludeMarketplace: bool = None
    InstanceType: str = None
    MaxDuration: int = None
    MaxInstanceCount: int = None
    MinDuration: int = None
    OfferingClass: str = None
    ProductDescription: str = None
    ReservedInstancesOfferingIds: list = None
    DryRun: bool = None
    InstanceTenancy: str = None
    MaxResults: int = None
    NextToken: str = None
    OfferingType: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeReservedInstancesOfferings')
    members = operation_model.input_shape.members


class DescribeRouteTablesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    RouteTableIds: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeRouteTables')
    members = operation_model.input_shape.members


class DescribeScheduledInstanceAvailabilityRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FirstSlotStartTimeRange: dict
    Recurrence: dict
    DryRun: bool = None
    Filters: list = None
    MaxResults: int = None
    MaxSlotDurationInHours: int = None
    MinSlotDurationInHours: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeScheduledInstanceAvailability')
    members = operation_model.input_shape.members


class DescribeScheduledInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    ScheduledInstanceIds: list = None
    SlotStartTimeRange: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeScheduledInstances')
    members = operation_model.input_shape.members


class DescribeSecurityGroupReferencesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GroupId: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSecurityGroupReferences')
    members = operation_model.input_shape.members


class DescribeSecurityGroupsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    GroupIds: list = None
    GroupNames: list = None
    DryRun: bool = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSecurityGroups')
    members = operation_model.input_shape.members


class DescribeSnapshotAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    SnapshotId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSnapshotAttribute')
    members = operation_model.input_shape.members


class DescribeSnapshotsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    OwnerIds: list = None
    RestorableByUserIds: list = None
    SnapshotIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSnapshots')
    members = operation_model.input_shape.members


class DescribeSpotDatafeedSubscriptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSpotDatafeedSubscription')
    members = operation_model.input_shape.members


class DescribeSpotFleetInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SpotFleetRequestId: str
    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSpotFleetInstances')
    members = operation_model.input_shape.members


class DescribeSpotFleetRequestHistoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SpotFleetRequestId: str
    StartTime: TimeStamp
    DryRun: bool = None
    EventType: str = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSpotFleetRequestHistory')
    members = operation_model.input_shape.members


class DescribeSpotFleetRequestsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None
    SpotFleetRequestIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSpotFleetRequests')
    members = operation_model.input_shape.members


class DescribeSpotInstanceRequestsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    SpotInstanceRequestIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSpotInstanceRequests')
    members = operation_model.input_shape.members


class DescribeSpotPriceHistoryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    AvailabilityZone: str = None
    DryRun: bool = None
    EndTime: TimeStamp = None
    InstanceTypes: list = None
    MaxResults: int = None
    NextToken: str = None
    ProductDescriptions: list = None
    StartTime: TimeStamp = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSpotPriceHistory')
    members = operation_model.input_shape.members


class DescribeStaleSecurityGroupsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeStaleSecurityGroups')
    members = operation_model.input_shape.members


class DescribeSubnetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    SubnetIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeSubnets')
    members = operation_model.input_shape.members


class DescribeTagsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeTags')
    members = operation_model.input_shape.members


class DescribeTransitGatewayAttachmentsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayAttachmentIds: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeTransitGatewayAttachments')
    members = operation_model.input_shape.members


class DescribeTransitGatewayRouteTablesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableIds: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeTransitGatewayRouteTables')
    members = operation_model.input_shape.members


class DescribeTransitGatewayVpcAttachmentsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayAttachmentIds: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeTransitGatewayVpcAttachments')
    members = operation_model.input_shape.members


class DescribeTransitGatewaysRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayIds: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeTransitGateways')
    members = operation_model.input_shape.members


class DescribeVolumeAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    VolumeId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVolumeAttribute')
    members = operation_model.input_shape.members


class DescribeVolumeStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    VolumeIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVolumeStatus')
    members = operation_model.input_shape.members


class DescribeVolumesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    VolumeIds: list = None
    DryRun: bool = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVolumes')
    members = operation_model.input_shape.members


class DescribeVolumesModificationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    VolumeIds: list = None
    Filters: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVolumesModifications')
    members = operation_model.input_shape.members


class DescribeVpcAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcAttribute')
    members = operation_model.input_shape.members


class DescribeVpcClassicLinkRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    VpcIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcClassicLink')
    members = operation_model.input_shape.members


class DescribeVpcClassicLinkDnsSupportRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    MaxResults: int = None
    NextToken: str = None
    VpcIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcClassicLinkDnsSupport')
    members = operation_model.input_shape.members


class DescribeVpcEndpointConnectionNotificationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    ConnectionNotificationId: str = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcEndpointConnectionNotifications')
    members = operation_model.input_shape.members


class DescribeVpcEndpointConnectionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcEndpointConnections')
    members = operation_model.input_shape.members


class DescribeVpcEndpointServiceConfigurationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    ServiceIds: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcEndpointServiceConfigurations')
    members = operation_model.input_shape.members


class DescribeVpcEndpointServicePermissionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServiceId: str
    DryRun: bool = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcEndpointServicePermissions')
    members = operation_model.input_shape.members


class DescribeVpcEndpointServicesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    ServiceNames: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcEndpointServices')
    members = operation_model.input_shape.members


class DescribeVpcEndpointsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    VpcEndpointIds: list = None
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcEndpoints')
    members = operation_model.input_shape.members


class DescribeVpcPeeringConnectionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    DryRun: bool = None
    VpcPeeringConnectionIds: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcPeeringConnections')
    members = operation_model.input_shape.members


class DescribeVpcsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    VpcIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpcs')
    members = operation_model.input_shape.members


class DescribeVpnConnectionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    VpnConnectionIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpnConnections')
    members = operation_model.input_shape.members


class DescribeVpnGatewaysRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filters: list = None
    VpnGatewayIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DescribeVpnGateways')
    members = operation_model.input_shape.members


class DetachClassicLinkVpcRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DetachClassicLinkVpc')
    members = operation_model.input_shape.members


class DetachInternetGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InternetGatewayId: str
    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DetachInternetGateway')
    members = operation_model.input_shape.members


class DetachNetworkInterfaceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AttachmentId: str
    DryRun: bool = None
    Force: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DetachNetworkInterface')
    members = operation_model.input_shape.members


class DetachVolumeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VolumeId: str
    Device: str = None
    Force: bool = None
    InstanceId: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DetachVolume')
    members = operation_model.input_shape.members


class DetachVpnGatewayRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    VpnGatewayId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DetachVpnGateway')
    members = operation_model.input_shape.members


class DisableTransitGatewayRouteTablePropagationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisableTransitGatewayRouteTablePropagation')
    members = operation_model.input_shape.members


class DisableVgwRoutePropagationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GatewayId: str
    RouteTableId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisableVgwRoutePropagation')
    members = operation_model.input_shape.members


class DisableVpcClassicLinkRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisableVpcClassicLink')
    members = operation_model.input_shape.members


class DisableVpcClassicLinkDnsSupportRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisableVpcClassicLinkDnsSupport')
    members = operation_model.input_shape.members


class DisassociateAddressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str = None
    PublicIp: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisassociateAddress')
    members = operation_model.input_shape.members


class DisassociateIamInstanceProfileRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisassociateIamInstanceProfile')
    members = operation_model.input_shape.members


class DisassociateRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisassociateRouteTable')
    members = operation_model.input_shape.members


class DisassociateSubnetCidrBlockRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisassociateSubnetCidrBlock')
    members = operation_model.input_shape.members


class DisassociateTransitGatewayRouteTableRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisassociateTransitGatewayRouteTable')
    members = operation_model.input_shape.members


class DisassociateVpcCidrBlockRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('DisassociateVpcCidrBlock')
    members = operation_model.input_shape.members


class EnableTransitGatewayRouteTablePropagationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('EnableTransitGatewayRouteTablePropagation')
    members = operation_model.input_shape.members


class EnableVgwRoutePropagationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GatewayId: str
    RouteTableId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('EnableVgwRoutePropagation')
    members = operation_model.input_shape.members


class EnableVolumeIORequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VolumeId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('EnableVolumeIO')
    members = operation_model.input_shape.members


class EnableVpcClassicLinkRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('EnableVpcClassicLink')
    members = operation_model.input_shape.members


class EnableVpcClassicLinkDnsSupportRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('EnableVpcClassicLinkDnsSupport')
    members = operation_model.input_shape.members


class ExportTransitGatewayRoutesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    S3Bucket: str
    Filters: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ExportTransitGatewayRoutes')
    members = operation_model.input_shape.members


class GetConsoleOutputRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    DryRun: bool = None
    Latest: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetConsoleOutput')
    members = operation_model.input_shape.members


class GetConsoleScreenshotRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    DryRun: bool = None
    WakeUp: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetConsoleScreenshot')
    members = operation_model.input_shape.members


class GetHostReservationPurchasePreviewRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    HostIdSet: list
    OfferingId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetHostReservationPurchasePreview')
    members = operation_model.input_shape.members


class GetLaunchTemplateDataRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetLaunchTemplateData')
    members = operation_model.input_shape.members


class GetPasswordDataRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetPasswordData')
    members = operation_model.input_shape.members


class GetReservedInstancesExchangeQuoteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ReservedInstanceIds: list
    DryRun: bool = None
    TargetConfigurations: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetReservedInstancesExchangeQuote')
    members = operation_model.input_shape.members


class GetTransitGatewayAttachmentPropagationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayAttachmentId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetTransitGatewayAttachmentPropagations')
    members = operation_model.input_shape.members


class GetTransitGatewayRouteTableAssociationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetTransitGatewayRouteTableAssociations')
    members = operation_model.input_shape.members


class GetTransitGatewayRouteTablePropagationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    Filters: list = None
    MaxResults: int = None
    NextToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('GetTransitGatewayRouteTablePropagations')
    members = operation_model.input_shape.members


class ImportImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Architecture: str = None
    ClientData: dict = None
    ClientToken: str = None
    Description: str = None
    DiskContainers: list = None
    DryRun: bool = None
    Encrypted: bool = None
    Hypervisor: str = None
    KmsKeyId: str = None
    LicenseType: str = None
    Platform: str = None
    RoleName: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ImportImage')
    members = operation_model.input_shape.members


class ImportInstanceRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Platform: str
    Description: str = None
    DiskImages: list = None
    DryRun: bool = None
    LaunchSpecification: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ImportInstance')
    members = operation_model.input_shape.members


class ImportKeyPairRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    KeyName: str
    PublicKeyMaterial: bytes
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ImportKeyPair')
    members = operation_model.input_shape.members


class ImportSnapshotRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ClientData: dict = None
    ClientToken: str = None
    Description: str = None
    DiskContainer: dict = None
    DryRun: bool = None
    Encrypted: bool = None
    KmsKeyId: str = None
    RoleName: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ImportSnapshot')
    members = operation_model.input_shape.members


class ImportVolumeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AvailabilityZone: str
    Image: dict
    Volume: dict
    Description: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ImportVolume')
    members = operation_model.input_shape.members


class ModifyCapacityReservationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CapacityReservationId: str
    InstanceCount: int = None
    EndDate: TimeStamp = None
    EndDateType: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyCapacityReservation')
    members = operation_model.input_shape.members


class ModifyFleetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FleetId: str
    TargetCapacitySpecification: dict
    DryRun: bool = None
    ExcessCapacityTerminationPolicy: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyFleet')
    members = operation_model.input_shape.members


class ModifyFpgaImageAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FpgaImageId: str
    DryRun: bool = None
    Attribute: str = None
    OperationType: str = None
    UserIds: list = None
    UserGroups: list = None
    ProductCodes: list = None
    LoadPermission: dict = None
    Description: str = None
    Name: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyFpgaImageAttribute')
    members = operation_model.input_shape.members


class ModifyHostsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AutoPlacement: str
    HostIds: list

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyHosts')
    members = operation_model.input_shape.members


class ModifyIdFormatRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Resource: str
    UseLongIds: bool

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyIdFormat')
    members = operation_model.input_shape.members


class ModifyIdentityIdFormatRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PrincipalArn: str
    Resource: str
    UseLongIds: bool

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyIdentityIdFormat')
    members = operation_model.input_shape.members


class ModifyImageAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ImageId: str
    Attribute: str = None
    Description: dict = None
    LaunchPermission: dict = None
    OperationType: str = None
    ProductCodes: list = None
    UserGroups: list = None
    UserIds: list = None
    Value: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyImageAttribute')
    members = operation_model.input_shape.members


class ModifyInstanceAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    SourceDestCheck: dict = None
    Attribute: str = None
    BlockDeviceMappings: list = None
    DisableApiTermination: dict = None
    DryRun: bool = None
    EbsOptimized: dict = None
    EnaSupport: dict = None
    Groups: list = None
    InstanceInitiatedShutdownBehavior: dict = None
    InstanceType: dict = None
    Kernel: dict = None
    Ramdisk: dict = None
    SriovNetSupport: dict = None
    UserData: dict = None
    Value: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyInstanceAttribute')
    members = operation_model.input_shape.members


class ModifyInstanceCapacityReservationAttributesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    CapacityReservationSpecification: dict
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyInstanceCapacityReservationAttributes')
    members = operation_model.input_shape.members


class ModifyInstanceCreditSpecificationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceCreditSpecifications: list
    DryRun: bool = None
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyInstanceCreditSpecification')
    members = operation_model.input_shape.members


class ModifyInstancePlacementRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceId: str
    Affinity: str = None
    GroupName: str = None
    HostId: str = None
    Tenancy: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyInstancePlacement')
    members = operation_model.input_shape.members


class ModifyLaunchTemplateRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DryRun: bool = None
    ClientToken: str = None
    LaunchTemplateId: str = None
    LaunchTemplateName: str = None
    DefaultVersion: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyLaunchTemplate')
    members = operation_model.input_shape.members


class ModifyNetworkInterfaceAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    Attachment: dict = None
    Description: dict = None
    DryRun: bool = None
    Groups: list = None
    SourceDestCheck: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyNetworkInterfaceAttribute')
    members = operation_model.input_shape.members


class ModifyReservedInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ReservedInstancesIds: list
    TargetConfigurations: list
    ClientToken: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyReservedInstances')
    members = operation_model.input_shape.members


class ModifySnapshotAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SnapshotId: str
    Attribute: str = None
    CreateVolumePermission: dict = None
    GroupNames: list = None
    OperationType: str = None
    UserIds: list = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifySnapshotAttribute')
    members = operation_model.input_shape.members


class ModifySpotFleetRequestRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SpotFleetRequestId: str
    ExcessCapacityTerminationPolicy: str = None
    TargetCapacity: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifySpotFleetRequest')
    members = operation_model.input_shape.members


class ModifySubnetAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SubnetId: str
    AssignIpv6AddressOnCreation: dict = None
    MapPublicIpOnLaunch: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifySubnetAttribute')
    members = operation_model.input_shape.members


class ModifyTransitGatewayVpcAttachmentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayAttachmentId: str
    AddSubnetIds: list = None
    RemoveSubnetIds: list = None
    Options: dict = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyTransitGatewayVpcAttachment')
    members = operation_model.input_shape.members


class ModifyVolumeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VolumeId: str
    DryRun: bool = None
    Size: int = None
    VolumeType: str = None
    Iops: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVolume')
    members = operation_model.input_shape.members


class ModifyVolumeAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VolumeId: str
    AutoEnableIO: dict = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVolumeAttribute')
    members = operation_model.input_shape.members


class ModifyVpcAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    EnableDnsHostnames: dict = None
    EnableDnsSupport: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVpcAttribute')
    members = operation_model.input_shape.members


class ModifyVpcEndpointRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcEndpointId: str
    DryRun: bool = None
    ResetPolicy: bool = None
    PolicyDocument: str = None
    AddRouteTableIds: list = None
    RemoveRouteTableIds: list = None
    AddSubnetIds: list = None
    RemoveSubnetIds: list = None
    AddSecurityGroupIds: list = None
    RemoveSecurityGroupIds: list = None
    PrivateDnsEnabled: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVpcEndpoint')
    members = operation_model.input_shape.members


class ModifyVpcEndpointConnectionNotificationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ConnectionNotificationId: str
    DryRun: bool = None
    ConnectionNotificationArn: str = None
    ConnectionEvents: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVpcEndpointConnectionNotification')
    members = operation_model.input_shape.members


class ModifyVpcEndpointServiceConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServiceId: str
    DryRun: bool = None
    AcceptanceRequired: bool = None
    AddNetworkLoadBalancerArns: list = None
    RemoveNetworkLoadBalancerArns: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVpcEndpointServiceConfiguration')
    members = operation_model.input_shape.members


class ModifyVpcEndpointServicePermissionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServiceId: str
    DryRun: bool = None
    AddAllowedPrincipals: list = None
    RemoveAllowedPrincipals: list = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVpcEndpointServicePermissions')
    members = operation_model.input_shape.members


class ModifyVpcPeeringConnectionOptionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcPeeringConnectionId: str
    AccepterPeeringConnectionOptions: dict = None
    DryRun: bool = None
    RequesterPeeringConnectionOptions: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVpcPeeringConnectionOptions')
    members = operation_model.input_shape.members


class ModifyVpcTenancyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcId: str
    InstanceTenancy: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ModifyVpcTenancy')
    members = operation_model.input_shape.members


class MonitorInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('MonitorInstances')
    members = operation_model.input_shape.members


class MoveAddressToVpcRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PublicIp: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('MoveAddressToVpc')
    members = operation_model.input_shape.members


class ProvisionByoipCidrRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Cidr: str
    CidrAuthorizationContext: dict = None
    Description: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ProvisionByoipCidr')
    members = operation_model.input_shape.members


class PurchaseHostReservationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    HostIdSet: list
    OfferingId: str
    ClientToken: str = None
    CurrencyCode: str = None
    LimitPrice: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('PurchaseHostReservation')
    members = operation_model.input_shape.members


class PurchaseReservedInstancesOfferingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceCount: int
    ReservedInstancesOfferingId: str
    DryRun: bool = None
    LimitPrice: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('PurchaseReservedInstancesOffering')
    members = operation_model.input_shape.members


class PurchaseScheduledInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PurchaseRequests: list
    ClientToken: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('PurchaseScheduledInstances')
    members = operation_model.input_shape.members


class RebootInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RebootInstances')
    members = operation_model.input_shape.members


class RegisterImageRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ImageLocation: str = None
    Architecture: str = None
    BlockDeviceMappings: list = None
    Description: str = None
    DryRun: bool = None
    EnaSupport: bool = None
    KernelId: str = None
    BillingProducts: list = None
    RamdiskId: str = None
    RootDeviceName: str = None
    SriovNetSupport: str = None
    VirtualizationType: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RegisterImage')
    members = operation_model.input_shape.members


class RejectTransitGatewayVpcAttachmentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayAttachmentId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RejectTransitGatewayVpcAttachment')
    members = operation_model.input_shape.members


class RejectVpcEndpointConnectionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServiceId: str
    VpcEndpointIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RejectVpcEndpointConnections')
    members = operation_model.input_shape.members


class RejectVpcPeeringConnectionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    VpcPeeringConnectionId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RejectVpcPeeringConnection')
    members = operation_model.input_shape.members


class ReleaseAddressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AllocationId: str = None
    PublicIp: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReleaseAddress')
    members = operation_model.input_shape.members


class ReleaseHostsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    HostIds: list

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReleaseHosts')
    members = operation_model.input_shape.members


class ReplaceIamInstanceProfileAssociationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IamInstanceProfile: dict
    AssociationId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReplaceIamInstanceProfileAssociation')
    members = operation_model.input_shape.members


class ReplaceNetworkAclAssociationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str
    NetworkAclId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReplaceNetworkAclAssociation')
    members = operation_model.input_shape.members


class ReplaceNetworkAclEntryRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Egress: bool
    NetworkAclId: str
    Protocol: str
    RuleAction: str
    RuleNumber: int
    CidrBlock: str = None
    DryRun: bool = None
    IcmpTypeCode: dict = None
    Ipv6CidrBlock: str = None
    PortRange: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReplaceNetworkAclEntry')
    members = operation_model.input_shape.members


class ReplaceRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RouteTableId: str
    DestinationCidrBlock: str = None
    DestinationIpv6CidrBlock: str = None
    DryRun: bool = None
    EgressOnlyInternetGatewayId: str = None
    GatewayId: str = None
    InstanceId: str = None
    NatGatewayId: str = None
    TransitGatewayId: str = None
    NetworkInterfaceId: str = None
    VpcPeeringConnectionId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReplaceRoute')
    members = operation_model.input_shape.members


class ReplaceRouteTableAssociationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AssociationId: str
    RouteTableId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReplaceRouteTableAssociation')
    members = operation_model.input_shape.members


class ReplaceTransitGatewayRouteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str = None
    Blackhole: bool = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReplaceTransitGatewayRoute')
    members = operation_model.input_shape.members


class ReportInstanceStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Instances: list
    ReasonCodes: list
    Status: str
    Description: str = None
    DryRun: bool = None
    EndTime: TimeStamp = None
    StartTime: TimeStamp = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ReportInstanceStatus')
    members = operation_model.input_shape.members


class RequestSpotFleetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SpotFleetRequestConfig: dict
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RequestSpotFleet')
    members = operation_model.input_shape.members


class RequestSpotInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AvailabilityZoneGroup: str = None
    BlockDurationMinutes: int = None
    ClientToken: str = None
    DryRun: bool = None
    InstanceCount: int = None
    LaunchGroup: str = None
    LaunchSpecification: dict = None
    SpotPrice: str = None
    Type: str = None
    ValidFrom: TimeStamp = None
    ValidUntil: TimeStamp = None
    InstanceInterruptionBehavior: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RequestSpotInstances')
    members = operation_model.input_shape.members


class ResetFpgaImageAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FpgaImageId: str
    DryRun: bool = None
    Attribute: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ResetFpgaImageAttribute')
    members = operation_model.input_shape.members


class ResetImageAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    ImageId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ResetImageAttribute')
    members = operation_model.input_shape.members


class ResetInstanceAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    InstanceId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ResetInstanceAttribute')
    members = operation_model.input_shape.members


class ResetNetworkInterfaceAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    DryRun: bool = None
    SourceDestCheck: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ResetNetworkInterfaceAttribute')
    members = operation_model.input_shape.members


class ResetSnapshotAttributeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Attribute: str
    SnapshotId: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('ResetSnapshotAttribute')
    members = operation_model.input_shape.members


class RestoreAddressToClassicRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PublicIp: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RestoreAddressToClassic')
    members = operation_model.input_shape.members


class RevokeSecurityGroupEgressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GroupId: str
    DryRun: bool = None
    IpPermissions: list = None
    CidrIp: str = None
    FromPort: int = None
    IpProtocol: str = None
    ToPort: int = None
    SourceSecurityGroupName: str = None
    SourceSecurityGroupOwnerId: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RevokeSecurityGroupEgress')
    members = operation_model.input_shape.members


class RevokeSecurityGroupIngressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CidrIp: str = None
    FromPort: int = None
    GroupId: str = None
    GroupName: str = None
    IpPermissions: list = None
    IpProtocol: str = None
    SourceSecurityGroupName: str = None
    SourceSecurityGroupOwnerId: str = None
    ToPort: int = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RevokeSecurityGroupIngress')
    members = operation_model.input_shape.members


class RunInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    MaxCount: int
    MinCount: int
    BlockDeviceMappings: list = None
    ImageId: str = None
    InstanceType: str = None
    Ipv6AddressCount: int = None
    Ipv6Addresses: list = None
    KernelId: str = None
    KeyName: str = None
    Monitoring: dict = None
    Placement: dict = None
    RamdiskId: str = None
    SecurityGroupIds: list = None
    SecurityGroups: list = None
    SubnetId: str = None
    UserData: str = None
    AdditionalInfo: str = None
    ClientToken: str = None
    DisableApiTermination: bool = None
    DryRun: bool = None
    EbsOptimized: bool = None
    IamInstanceProfile: dict = None
    InstanceInitiatedShutdownBehavior: str = None
    NetworkInterfaces: list = None
    PrivateIpAddress: str = None
    ElasticGpuSpecification: list = None
    TagSpecifications: list = None
    LaunchTemplate: dict = None
    InstanceMarketOptions: dict = None
    CreditSpecification: dict = None
    CpuOptions: dict = None
    CapacityReservationSpecification: dict = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RunInstances')
    members = operation_model.input_shape.members


class RunScheduledInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    LaunchSpecification: dict
    ScheduledInstanceId: str
    ClientToken: str = None
    DryRun: bool = None
    InstanceCount: int = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('RunScheduledInstances')
    members = operation_model.input_shape.members


class SearchTransitGatewayRoutesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TransitGatewayRouteTableId: str
    Filters: list
    MaxResults: int = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('SearchTransitGatewayRoutes')
    members = operation_model.input_shape.members


class StartInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceIds: list
    AdditionalInfo: str = None
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('StartInstances')
    members = operation_model.input_shape.members


class StopInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceIds: list
    DryRun: bool = None
    Force: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('StopInstances')
    members = operation_model.input_shape.members


class TerminateInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('TerminateInstances')
    members = operation_model.input_shape.members


class UnassignIpv6AddressesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Ipv6Addresses: list
    NetworkInterfaceId: str

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('UnassignIpv6Addresses')
    members = operation_model.input_shape.members


class UnassignPrivateIpAddressesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NetworkInterfaceId: str
    PrivateIpAddresses: list

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('UnassignPrivateIpAddresses')
    members = operation_model.input_shape.members


class UnmonitorInstancesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    InstanceIds: list
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('UnmonitorInstances')
    members = operation_model.input_shape.members


class UpdateSecurityGroupRuleDescriptionsEgressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IpPermissions: list
    DryRun: bool = None
    GroupId: str = None
    GroupName: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('UpdateSecurityGroupRuleDescriptionsEgress')
    members = operation_model.input_shape.members


class UpdateSecurityGroupRuleDescriptionsIngressRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IpPermissions: list
    DryRun: bool = None
    GroupId: str = None
    GroupName: str = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('UpdateSecurityGroupRuleDescriptionsIngress')
    members = operation_model.input_shape.members


class WithdrawByoipCidrRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Cidr: str
    DryRun: bool = None

    operation_model = botocore.session.Session().get_service_model('ec2').operation_model('WithdrawByoipCidr')
    members = operation_model.input_shape.members
