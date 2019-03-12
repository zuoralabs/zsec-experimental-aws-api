
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AcceptHandshakeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    HandshakeId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('AcceptHandshake')
    members = operation_model.input_shape.members


class AttachPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PolicyId: str
    TargetId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('AttachPolicy')
    members = operation_model.input_shape.members


class CancelHandshakeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    HandshakeId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('CancelHandshake')
    members = operation_model.input_shape.members


class CreateAccountRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Email: str
    AccountName: str
    RoleName: str = None
    IamUserAccessToBilling: str = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('CreateAccount')
    members = operation_model.input_shape.members


class CreateOrganizationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    FeatureSet: str = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('CreateOrganization')
    members = operation_model.input_shape.members


class CreateOrganizationalUnitRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ParentId: str
    Name: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('CreateOrganizationalUnit')
    members = operation_model.input_shape.members


class CreatePolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Content: str
    Description: str
    Name: str
    Type: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('CreatePolicy')
    members = operation_model.input_shape.members


class DeclineHandshakeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    HandshakeId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DeclineHandshake')
    members = operation_model.input_shape.members



class DeleteOrganizationalUnitRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OrganizationalUnitId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DeleteOrganizationalUnit')
    members = operation_model.input_shape.members


class DeletePolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PolicyId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DeletePolicy')
    members = operation_model.input_shape.members


class DescribeAccountRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AccountId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DescribeAccount')
    members = operation_model.input_shape.members


class DescribeCreateAccountStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    CreateAccountRequestId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DescribeCreateAccountStatus')
    members = operation_model.input_shape.members


class DescribeHandshakeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    HandshakeId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DescribeHandshake')
    members = operation_model.input_shape.members



class DescribeOrganizationalUnitRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OrganizationalUnitId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DescribeOrganizationalUnit')
    members = operation_model.input_shape.members


class DescribePolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PolicyId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DescribePolicy')
    members = operation_model.input_shape.members


class DetachPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PolicyId: str
    TargetId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DetachPolicy')
    members = operation_model.input_shape.members


class DisableAWSServiceAccessRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServicePrincipal: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DisableAWSServiceAccess')
    members = operation_model.input_shape.members


class DisablePolicyTypeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RootId: str
    PolicyType: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('DisablePolicyType')
    members = operation_model.input_shape.members


class EnableAWSServiceAccessRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ServicePrincipal: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('EnableAWSServiceAccess')
    members = operation_model.input_shape.members


class EnableAllFeaturesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('EnableAllFeatures')
    members = operation_model.input_shape.members


class EnablePolicyTypeRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RootId: str
    PolicyType: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('EnablePolicyType')
    members = operation_model.input_shape.members


class InviteAccountToOrganizationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Target: dict
    Notes: str = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('InviteAccountToOrganization')
    members = operation_model.input_shape.members



class ListAWSServiceAccessForOrganizationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListAWSServiceAccessForOrganization')
    members = operation_model.input_shape.members


class ListAccountsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListAccounts')
    members = operation_model.input_shape.members


class ListAccountsForParentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ParentId: str
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListAccountsForParent')
    members = operation_model.input_shape.members


class ListChildrenRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ParentId: str
    ChildType: str
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListChildren')
    members = operation_model.input_shape.members


class ListCreateAccountStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    States: list = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListCreateAccountStatus')
    members = operation_model.input_shape.members


class ListHandshakesForAccountRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filter: dict = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListHandshakesForAccount')
    members = operation_model.input_shape.members


class ListHandshakesForOrganizationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filter: dict = None
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListHandshakesForOrganization')
    members = operation_model.input_shape.members


class ListOrganizationalUnitsForParentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ParentId: str
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListOrganizationalUnitsForParent')
    members = operation_model.input_shape.members


class ListParentsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ChildId: str
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListParents')
    members = operation_model.input_shape.members


class ListPoliciesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Filter: str
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListPolicies')
    members = operation_model.input_shape.members


class ListPoliciesForTargetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    TargetId: str
    Filter: str
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListPoliciesForTarget')
    members = operation_model.input_shape.members


class ListRootsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListRoots')
    members = operation_model.input_shape.members


class ListTargetsForPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PolicyId: str
    NextToken: str = None
    MaxResults: int = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('ListTargetsForPolicy')
    members = operation_model.input_shape.members


class MoveAccountRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AccountId: str
    SourceParentId: str
    DestinationParentId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('MoveAccount')
    members = operation_model.input_shape.members


class RemoveAccountFromOrganizationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    AccountId: str

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('RemoveAccountFromOrganization')
    members = operation_model.input_shape.members


class UpdateOrganizationalUnitRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    OrganizationalUnitId: str
    Name: str = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('UpdateOrganizationalUnit')
    members = operation_model.input_shape.members


class UpdatePolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    PolicyId: str
    Name: str = None
    Description: str = None
    Content: str = None

    operation_model = botocore.session.Session().get_service_model('organizations').operation_model('UpdatePolicy')
    members = operation_model.input_shape.members
