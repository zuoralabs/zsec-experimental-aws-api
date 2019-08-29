import generated.s3_types as aws_types
import generated.config_types
import aws_meta
import boto3

aws_config = boto3.client('config_types', region_name='us-east-1')


def get_by_name(name):
    for xx in aws_config.get_paginator(describe_config_rules).paginate():
        print(xx)




generated.config_types.DescribeConfigRulesRequest(ConfigRuleNames=)
generated.config_types.PutConfigRuleRequest(ConfigRule= )



#print(aws_meta.execute(s3, rr))
print(rr.execute(s3))
