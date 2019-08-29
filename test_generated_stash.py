import generated.s3_types as aws_types
import aws_meta
from generated import organizations_types
import boto3


if 0:
    rr = aws_types.CreateBucketRequest(Bucket='abctsstn0347010703456', ACL='private')
    s3 = boto3.client('s3')
    print(rr.execute(s3))





#print(aws_meta.execute(s3, rr))


from generated import ssm_types, sts_types, config_types, sns_types, sqs_types, cloudwatch_types, kinesis_types, s3_types

s3_types.PutObjectRequest(Bucket='zuora-sec-bg', Key='test-cross-account', Body=b"abcd")


# sns_types.SubscribeInput(TopicArn=topic, Protocol='email', Endpoint=endpoint)
# sns_types.DeleteTopicInput(TopicArn=topic)
# sns_types.ListSubscriptionsByTopicInput(TopicArn=topic)

# config_types.StartConfigRulesEvaluationRequest(ConfigRuleNames=['SecWafRule'])


kinesis_types.DescribeStreamInput( )


session = boto3.Session(profile_name='test')
ssm = session.client('ssm', region_name='us-east-1')
sqs = session.client('sqs', region_name='us-west-1')

sqs_types.SendMessageRequest(QueueUrl="https://sqs.us-west-1.amazonaws.com/438453513788/test-queue",
                             MessageBody="abc").execute(sqs)

stream_arn = "arn:aws:kinesis:us-west-2:163366849328:stream/SecS3PublicPermRuleStream"

cloudwatch_types.PutMetricDataInput

#ssm_types.GetParameterRequest(Name="/Sec/JiraPassword").execute(ssm)
#print(ssm_types.GetParameterRequest(Name="/Sec/JiraUsername").execute(ssm))
#ssm_types.GetParameterRequest(Name="/Sec/JiraPassword",WithDecryption=True).execute(ssm)

#print(ssm_types.GetParametersByPathRequest(Path="/Sec/").execute(ssm))

#print(ssm_types.GetParametersByPathRequest(Path="/").execute(ssm))
