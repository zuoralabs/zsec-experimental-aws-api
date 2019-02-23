
import typing
import botocore.session
import aws_meta
from botocore.model import *

class CreateBucketRequest(typing.NamedTuple):
    operation_model = botocore.session.Session().get_service_model('s3').operation_model('CreateBucket')
    members = operation_model.input_shape.members

    def execute(self, svc):
        return aws_meta.execute(svc, self)
    Bucket: str
    ACL: str = None
    CreateBucketConfiguration: typing.Any = None
    GrantFullControl: str = None
    GrantRead: str = None
    GrantReadACP: str = None
    GrantWrite: str = None
    GrantWriteACP: str = None
    ObjectLockEnabledForBucket: typing.Any = None

