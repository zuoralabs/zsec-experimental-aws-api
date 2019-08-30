from typing import NewType


s3_service_name_type = NewType('s3_service_name', str)
s3_service_name: s3_service_name_type = s3_service_name_type('s3')

waf_service_name_type = NewType('waf_service_name', str)
waf_service_name: waf_service_name_type = waf_service_name_type('waf')

waf_regional_service_name_type = NewType('waf_regional_service_name', str)
waf_regional_service_name: waf_regional_service_name_type = waf_regional_service_name_type('waf_regional')

dynamodb_service_name_type = NewType('dynamodb_service_name', str)
dynamodb_service_name: dynamodb_service_name_type = dynamodb_service_name_type('dynamodb')

shield_service_name_type = NewType('shield_service_name', str)
shield_service_name: shield_service_name_type = shield_service_name_type('shield')

ec2_service_name_type = NewType('ec2_service_name', str)
ec2_service_name: ec2_service_name_type = ec2_service_name_type('ec2')

organizations_service_name_type = NewType('organizations_service_name', str)
organizations_service_name: organizations_service_name_type = organizations_service_name_type('organizations')

ssm_service_name_type = NewType('ssm_service_name', str)
ssm_service_name: ssm_service_name_type = ssm_service_name_type('ssm')

sts_service_name_type = NewType('sts_service_name', str)
sts_service_name: sts_service_name_type = sts_service_name_type('sts')

config_service_name_type = NewType('config_service_name', str)
config_service_name: config_service_name_type = config_service_name_type('config')

sns_service_name_type = NewType('sns_service_name', str)
sns_service_name: sns_service_name_type = sns_service_name_type('sns')

sqs_service_name_type = NewType('sqs_service_name', str)
sqs_service_name: sqs_service_name_type = sqs_service_name_type('sqs')

rds_service_name_type = NewType('rds_service_name', str)
rds_service_name: rds_service_name_type = rds_service_name_type('rds')

cloudwatch_service_name_type = NewType('cloudwatch_service_name', str)
cloudwatch_service_name: cloudwatch_service_name_type = cloudwatch_service_name_type('cloudwatch')

kinesis_service_name_type = NewType('kinesis_service_name', str)
kinesis_service_name: kinesis_service_name_type = kinesis_service_name_type('kinesis')
