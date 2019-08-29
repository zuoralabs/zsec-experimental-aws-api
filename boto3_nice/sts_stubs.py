
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
class sts_client_type(BaseClient):
    def assume_role(self, RoleArn: str, RoleSessionName: str, PolicyArns: list = None, Policy: str = None, DurationSeconds: int = None, ExternalId: str = None, SerialNumber: str = None, TokenCode: str = None): ...
    def assume_role_with_saml(self, RoleArn: str, PrincipalArn: str, SAMLAssertion: str, PolicyArns: list = None, Policy: str = None, DurationSeconds: int = None): ...
    def assume_role_with_web_identity(self, RoleArn: str, RoleSessionName: str, WebIdentityToken: str, ProviderId: str = None, PolicyArns: list = None, Policy: str = None, DurationSeconds: int = None): ...
    def decode_authorization_message(self, EncodedMessage: str): ...
    def get_caller_identity(self): ...
    def get_federation_token(self, Name: str, Policy: str = None, PolicyArns: list = None, DurationSeconds: int = None): ...
    def get_session_token(self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None): ...
    pass

