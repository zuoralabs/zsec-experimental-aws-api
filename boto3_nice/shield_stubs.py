
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
class shield_client_type(BaseClient):
    def associate_drt_log_bucket(self, LogBucket: str): ...
    def associate_drt_role(self, RoleArn: str): ...
    def create_protection(self, Name: str, ResourceArn: str): ...
    def create_subscription(self): ...
    def delete_protection(self, ProtectionId: str): ...
    def delete_subscription(self): ...
    def describe_attack(self, AttackId: str): ...
    def describe_drt_access(self): ...
    def describe_emergency_contact_settings(self): ...
    def describe_protection(self, ProtectionId: str = None, ResourceArn: str = None): ...
    def describe_subscription(self): ...
    def disassociate_drt_log_bucket(self, LogBucket: str): ...
    def disassociate_drt_role(self): ...
    def get_subscription_state(self): ...
    def list_attacks(self, ResourceArns: list = None, StartTime: dict = None, EndTime: dict = None, NextToken: str = None, MaxResults: int = None): ...
    def list_protections(self, NextToken: str = None, MaxResults: int = None): ...
    def update_emergency_contact_settings(self, EmergencyContactList: list = None): ...
    def update_subscription(self, AutoRenew: str = None): ...
    pass

