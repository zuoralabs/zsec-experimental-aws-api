
import typing
import botocore.session
import aws_meta
from botocore.model import *
from botocore.client import BaseClient
from datetime import datetime
import boto3


class Map(dict):
    pass
    
    
# noinspection PyPep8Naming
class organizations_client_type(BaseClient):
    def accept_handshake(self, HandshakeId: str): ...
    def attach_policy(self, PolicyId: str, TargetId: str): ...
    def cancel_handshake(self, HandshakeId: str): ...
    def create_account(self, Email: str, AccountName: str, RoleName: str = None, IamUserAccessToBilling: str = None): ...
    def create_gov_cloud_account(self, Email: str, AccountName: str, RoleName: str = None, IamUserAccessToBilling: str = None): ...
    def create_organization(self, FeatureSet: str = None): ...
    def create_organizational_unit(self, ParentId: str, Name: str): ...
    def create_policy(self, Content: str, Description: str, Name: str, Type: str): ...
    def decline_handshake(self, HandshakeId: str): ...
    def delete_organization(self): ...
    def delete_organizational_unit(self, OrganizationalUnitId: str): ...
    def delete_policy(self, PolicyId: str): ...
    def describe_account(self, AccountId: str): ...
    def describe_create_account_status(self, CreateAccountRequestId: str): ...
    def describe_handshake(self, HandshakeId: str): ...
    def describe_organization(self): ...
    def describe_organizational_unit(self, OrganizationalUnitId: str): ...
    def describe_policy(self, PolicyId: str): ...
    def detach_policy(self, PolicyId: str, TargetId: str): ...
    def disable_aws_service_access(self, ServicePrincipal: str): ...
    def disable_policy_type(self, RootId: str, PolicyType: str): ...
    def enable_aws_service_access(self, ServicePrincipal: str): ...
    def enable_all_features(self): ...
    def enable_policy_type(self, RootId: str, PolicyType: str): ...
    def invite_account_to_organization(self, Target: dict, Notes: str = None): ...
    def leave_organization(self): ...
    def list_aws_service_access_for_organization(self, NextToken: str = None, MaxResults: int = None): ...
    def list_accounts(self, NextToken: str = None, MaxResults: int = None): ...
    def list_accounts_for_parent(self, ParentId: str, NextToken: str = None, MaxResults: int = None): ...
    def list_children(self, ParentId: str, ChildType: str, NextToken: str = None, MaxResults: int = None): ...
    def list_create_account_status(self, States: list = None, NextToken: str = None, MaxResults: int = None): ...
    def list_handshakes_for_account(self, Filter: dict = None, NextToken: str = None, MaxResults: int = None): ...
    def list_handshakes_for_organization(self, Filter: dict = None, NextToken: str = None, MaxResults: int = None): ...
    def list_organizational_units_for_parent(self, ParentId: str, NextToken: str = None, MaxResults: int = None): ...
    def list_parents(self, ChildId: str, NextToken: str = None, MaxResults: int = None): ...
    def list_policies(self, Filter: str, NextToken: str = None, MaxResults: int = None): ...
    def list_policies_for_target(self, TargetId: str, Filter: str, NextToken: str = None, MaxResults: int = None): ...
    def list_roots(self, NextToken: str = None, MaxResults: int = None): ...
    def list_tags_for_resource(self, ResourceId: str, NextToken: str = None): ...
    def list_targets_for_policy(self, PolicyId: str, NextToken: str = None, MaxResults: int = None): ...
    def move_account(self, AccountId: str, SourceParentId: str, DestinationParentId: str): ...
    def remove_account_from_organization(self, AccountId: str): ...
    def tag_resource(self, ResourceId: str, Tags: list): ...
    def untag_resource(self, ResourceId: str, TagKeys: list): ...
    def update_organizational_unit(self, OrganizationalUnitId: str, Name: str = None): ...
    def update_policy(self, PolicyId: str, Name: str = None, Description: str = None, Content: str = None): ...
    pass

