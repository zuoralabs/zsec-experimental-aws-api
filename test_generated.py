import generated_module
import aws_meta

rr = generated_module.CreateBucketRequest(Bucket='abctsstn0347010703456', ACL='private')

def to_dict(nt):
    return {k:v for k,v in nt._asdict().items() if v is not None}

import boto3

s3 = boto3.client('s3', region_name='us-east-1')
#print(s3.create_bucket(**to_dict(rr)))

#print(aws_meta.execute(s3, rr))
print(rr.execute(s3))
