import generated.s3_types as aws_types
import aws_meta

rr = aws_types.CreateBucketRequest(Bucket='abctsstn0347010703456', ACL='private')


aws_types.CreateBucketRequest(Bucket="hi", )
aws_types.CreateBucketRequest


import boto3

s3 = boto3.client('s3', region_name='us-east-1')

#print(aws_meta.execute(s3, rr))
print(rr.execute(s3))
