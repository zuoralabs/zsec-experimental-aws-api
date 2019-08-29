import boto3 as _boto3
from .s3_stubs import s3_client_type
from .waf_stubs import waf_client_type
from .waf_regional_stubs import waf_regional_client_type
from .dynamodb_stubs import dynamodb_client_type
from .shield_stubs import shield_client_type
from .ec2_stubs import ec2_client_type
from .organizations_stubs import organizations_client_type
from .ssm_stubs import ssm_client_type
from .sts_stubs import sts_client_type
from .config_stubs import config_client_type
from .sns_stubs import sns_client_type
from .sqs_stubs import sqs_client_type
from .rds_stubs import rds_client_type
from .cloudwatch_stubs import cloudwatch_client_type
from .kinesis_stubs import kinesis_client_type
from .service_names import *


class Session(_boto3.Session):
    def s3_client(self: 'Session', region_name: str = None) -> s3_client_type:
        return self.client('s3', region_name=region_name)

    def waf_client(self: 'Session', region_name: str = None) -> waf_client_type:
        return self.client('waf', region_name=region_name)

    def waf_regional_client(self: 'Session', region_name: str = None) -> waf_regional_client_type:
        return self.client('waf-regional', region_name=region_name)

    def dynamodb_client(self: 'Session', region_name: str = None) -> dynamodb_client_type:
        return self.client('dynamodb', region_name=region_name)

    def shield_client(self: 'Session', region_name: str = None) -> shield_client_type:
        return self.client('shield', region_name=region_name)

    def ec2_client(self: 'Session', region_name: str = None) -> ec2_client_type:
        return self.client('ec2', region_name=region_name)

    def organizations_client(self: 'Session', region_name: str = None) -> organizations_client_type:
        return self.client('organizations', region_name=region_name)

    def ssm_client(self: 'Session', region_name: str = None) -> ssm_client_type:
        return self.client('ssm', region_name=region_name)

    def sts_client(self: 'Session', region_name: str = None) -> sts_client_type:
        return self.client('sts', region_name=region_name)

    def config_client(self: 'Session', region_name: str = None) -> config_client_type:
        return self.client('config', region_name=region_name)

    def sns_client(self: 'Session', region_name: str = None) -> sns_client_type:
        return self.client('sns', region_name=region_name)

    def sqs_client(self: 'Session', region_name: str = None) -> sqs_client_type:
        return self.client('sqs', region_name=region_name)

    def rds_client(self: 'Session', region_name: str = None) -> rds_client_type:
        return self.client('rds', region_name=region_name)

    def cloudwatch_client(self: 'Session', region_name: str = None) -> cloudwatch_client_type:
        return self.client('cloudwatch', region_name=region_name)

    def kinesis_client(self: 'Session', region_name: str = None) -> kinesis_client_type:
        return self.client('kinesis', region_name=region_name)
