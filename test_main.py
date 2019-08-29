# test generated_2
from typing import NewType

try:
    import boto3_nice as boto3
    raise ImportError
except ImportError:
    import boto3

config_service_name = NewType('config_service_name', str)('config')
s3_service_name = NewType('s3_service_name', str)('s3')


s3 = boto3.Session().client(s3_service_name)
xx = boto3.Session().client(config_service_name)
ans = xx.describe_compliance_by_config_rule(
    ConfigRuleNames=['SecEc2RuleConfigRule']
)
