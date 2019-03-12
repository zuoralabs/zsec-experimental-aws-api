
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class AbortMultipartUploadRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('AbortMultipartUpload')
    members = operation_model.input_shape.members


class CompleteMultipartUploadRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    UploadId: str
    MultipartUpload: dict = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('CompleteMultipartUpload')
    members = operation_model.input_shape.members


class CopyObjectRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    CopySource: str
    Key: str
    ACL: str = None
    CacheControl: str = None
    ContentDisposition: str = None
    ContentEncoding: str = None
    ContentLanguage: str = None
    ContentType: str = None
    CopySourceIfMatch: str = None
    CopySourceIfModifiedSince: TimeStamp = None
    CopySourceIfNoneMatch: str = None
    CopySourceIfUnmodifiedSince: TimeStamp = None
    Expires: TimeStamp = None
    GrantFullControl: str = None
    GrantRead: str = None
    GrantReadACP: str = None
    GrantWriteACP: str = None
    Metadata: Map = None
    MetadataDirective: str = None
    TaggingDirective: str = None
    ServerSideEncryption: str = None
    StorageClass: str = None
    WebsiteRedirectLocation: str = None
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    SSEKMSKeyId: str = None
    CopySourceSSECustomerAlgorithm: str = None
    CopySourceSSECustomerKey: str = None
    CopySourceSSECustomerKeyMD5: str = None
    RequestPayer: str = None
    Tagging: str = None
    ObjectLockMode: str = None
    ObjectLockRetainUntilDate: TimeStamp = None
    ObjectLockLegalHoldStatus: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('CopyObject')
    members = operation_model.input_shape.members


class CreateBucketRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ACL: str = None
    CreateBucketConfiguration: dict = None
    GrantFullControl: str = None
    GrantRead: str = None
    GrantReadACP: str = None
    GrantWrite: str = None
    GrantWriteACP: str = None
    ObjectLockEnabledForBucket: bool = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('CreateBucket')
    members = operation_model.input_shape.members


class CreateMultipartUploadRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    ACL: str = None
    CacheControl: str = None
    ContentDisposition: str = None
    ContentEncoding: str = None
    ContentLanguage: str = None
    ContentType: str = None
    Expires: TimeStamp = None
    GrantFullControl: str = None
    GrantRead: str = None
    GrantReadACP: str = None
    GrantWriteACP: str = None
    Metadata: Map = None
    ServerSideEncryption: str = None
    StorageClass: str = None
    WebsiteRedirectLocation: str = None
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    SSEKMSKeyId: str = None
    RequestPayer: str = None
    Tagging: str = None
    ObjectLockMode: str = None
    ObjectLockRetainUntilDate: TimeStamp = None
    ObjectLockLegalHoldStatus: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('CreateMultipartUpload')
    members = operation_model.input_shape.members


class DeleteBucketRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucket')
    members = operation_model.input_shape.members


class DeleteBucketAnalyticsConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketAnalyticsConfiguration')
    members = operation_model.input_shape.members


class DeleteBucketCorsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketCors')
    members = operation_model.input_shape.members


class DeleteBucketEncryptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketEncryption')
    members = operation_model.input_shape.members


class DeleteBucketInventoryConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketInventoryConfiguration')
    members = operation_model.input_shape.members


class DeleteBucketLifecycleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketLifecycle')
    members = operation_model.input_shape.members


class DeleteBucketMetricsConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketMetricsConfiguration')
    members = operation_model.input_shape.members


class DeleteBucketPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketPolicy')
    members = operation_model.input_shape.members


class DeleteBucketReplicationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketReplication')
    members = operation_model.input_shape.members


class DeleteBucketTaggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketTagging')
    members = operation_model.input_shape.members


class DeleteBucketWebsiteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteBucketWebsite')
    members = operation_model.input_shape.members


class DeleteObjectRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    MFA: str = None
    VersionId: str = None
    RequestPayer: str = None
    BypassGovernanceRetention: bool = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteObject')
    members = operation_model.input_shape.members


class DeleteObjectTaggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    VersionId: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteObjectTagging')
    members = operation_model.input_shape.members


class DeleteObjectsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Delete: dict
    MFA: str = None
    RequestPayer: str = None
    BypassGovernanceRetention: bool = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeleteObjects')
    members = operation_model.input_shape.members


class DeletePublicAccessBlockRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('DeletePublicAccessBlock')
    members = operation_model.input_shape.members


class GetBucketAccelerateConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketAccelerateConfiguration')
    members = operation_model.input_shape.members


class GetBucketAclRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketAcl')
    members = operation_model.input_shape.members


class GetBucketAnalyticsConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketAnalyticsConfiguration')
    members = operation_model.input_shape.members


class GetBucketCorsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketCors')
    members = operation_model.input_shape.members


class GetBucketEncryptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketEncryption')
    members = operation_model.input_shape.members


class GetBucketInventoryConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketInventoryConfiguration')
    members = operation_model.input_shape.members


class GetBucketLifecycleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketLifecycle')
    members = operation_model.input_shape.members


class GetBucketLifecycleConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketLifecycleConfiguration')
    members = operation_model.input_shape.members


class GetBucketLocationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketLocation')
    members = operation_model.input_shape.members


class GetBucketLoggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketLogging')
    members = operation_model.input_shape.members


class GetBucketMetricsConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketMetricsConfiguration')
    members = operation_model.input_shape.members


class GetBucketNotificationConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketNotification')
    members = operation_model.input_shape.members


class GetBucketNotificationConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketNotificationConfiguration')
    members = operation_model.input_shape.members


class GetBucketPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketPolicy')
    members = operation_model.input_shape.members


class GetBucketPolicyStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketPolicyStatus')
    members = operation_model.input_shape.members


class GetBucketReplicationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketReplication')
    members = operation_model.input_shape.members


class GetBucketRequestPaymentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketRequestPayment')
    members = operation_model.input_shape.members


class GetBucketTaggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketTagging')
    members = operation_model.input_shape.members


class GetBucketVersioningRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketVersioning')
    members = operation_model.input_shape.members


class GetBucketWebsiteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetBucketWebsite')
    members = operation_model.input_shape.members


class GetObjectRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    IfMatch: str = None
    IfModifiedSince: TimeStamp = None
    IfNoneMatch: str = None
    IfUnmodifiedSince: TimeStamp = None
    Range: str = None
    ResponseCacheControl: str = None
    ResponseContentDisposition: str = None
    ResponseContentEncoding: str = None
    ResponseContentLanguage: str = None
    ResponseContentType: str = None
    ResponseExpires: TimeStamp = None
    VersionId: str = None
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    RequestPayer: str = None
    PartNumber: int = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetObject')
    members = operation_model.input_shape.members


class GetObjectAclRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    VersionId: str = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetObjectAcl')
    members = operation_model.input_shape.members


class GetObjectLegalHoldRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    VersionId: str = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetObjectLegalHold')
    members = operation_model.input_shape.members


class GetObjectLockConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetObjectLockConfiguration')
    members = operation_model.input_shape.members


class GetObjectRetentionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    VersionId: str = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetObjectRetention')
    members = operation_model.input_shape.members


class GetObjectTaggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    VersionId: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetObjectTagging')
    members = operation_model.input_shape.members


class GetObjectTorrentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetObjectTorrent')
    members = operation_model.input_shape.members


class GetPublicAccessBlockRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('GetPublicAccessBlock')
    members = operation_model.input_shape.members


class HeadBucketRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('HeadBucket')
    members = operation_model.input_shape.members


class HeadObjectRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    IfMatch: str = None
    IfModifiedSince: TimeStamp = None
    IfNoneMatch: str = None
    IfUnmodifiedSince: TimeStamp = None
    Range: str = None
    VersionId: str = None
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    RequestPayer: str = None
    PartNumber: int = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('HeadObject')
    members = operation_model.input_shape.members


class ListBucketAnalyticsConfigurationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ContinuationToken: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListBucketAnalyticsConfigurations')
    members = operation_model.input_shape.members


class ListBucketInventoryConfigurationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ContinuationToken: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListBucketInventoryConfigurations')
    members = operation_model.input_shape.members


class ListBucketMetricsConfigurationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ContinuationToken: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListBucketMetricsConfigurations')
    members = operation_model.input_shape.members



class ListMultipartUploadsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Delimiter: str = None
    EncodingType: str = None
    KeyMarker: str = None
    MaxUploads: int = None
    Prefix: str = None
    UploadIdMarker: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListMultipartUploads')
    members = operation_model.input_shape.members


class ListObjectVersionsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Delimiter: str = None
    EncodingType: str = None
    KeyMarker: str = None
    MaxKeys: int = None
    Prefix: str = None
    VersionIdMarker: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListObjectVersions')
    members = operation_model.input_shape.members


class ListObjectsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Delimiter: str = None
    EncodingType: str = None
    Marker: str = None
    MaxKeys: int = None
    Prefix: str = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListObjects')
    members = operation_model.input_shape.members


class ListObjectsV2Request(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Delimiter: str = None
    EncodingType: str = None
    MaxKeys: int = None
    Prefix: str = None
    ContinuationToken: str = None
    FetchOwner: bool = None
    StartAfter: str = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListObjectsV2')
    members = operation_model.input_shape.members


class ListPartsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    UploadId: str
    MaxParts: int = None
    PartNumberMarker: int = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('ListParts')
    members = operation_model.input_shape.members


class PutBucketAccelerateConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    AccelerateConfiguration: dict

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketAccelerateConfiguration')
    members = operation_model.input_shape.members


class PutBucketAclRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ACL: str = None
    AccessControlPolicy: dict = None
    ContentMD5: str = None
    GrantFullControl: str = None
    GrantRead: str = None
    GrantReadACP: str = None
    GrantWrite: str = None
    GrantWriteACP: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketAcl')
    members = operation_model.input_shape.members


class PutBucketAnalyticsConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str
    AnalyticsConfiguration: dict

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketAnalyticsConfiguration')
    members = operation_model.input_shape.members


class PutBucketCorsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    CORSConfiguration: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketCors')
    members = operation_model.input_shape.members


class PutBucketEncryptionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ServerSideEncryptionConfiguration: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketEncryption')
    members = operation_model.input_shape.members


class PutBucketInventoryConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str
    InventoryConfiguration: dict

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketInventoryConfiguration')
    members = operation_model.input_shape.members


class PutBucketLifecycleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ContentMD5: str = None
    LifecycleConfiguration: dict = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketLifecycle')
    members = operation_model.input_shape.members


class PutBucketLifecycleConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    LifecycleConfiguration: dict = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketLifecycleConfiguration')
    members = operation_model.input_shape.members


class PutBucketLoggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    BucketLoggingStatus: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketLogging')
    members = operation_model.input_shape.members


class PutBucketMetricsConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Id: str
    MetricsConfiguration: dict

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketMetricsConfiguration')
    members = operation_model.input_shape.members


class PutBucketNotificationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    NotificationConfiguration: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketNotification')
    members = operation_model.input_shape.members


class PutBucketNotificationConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    NotificationConfiguration: dict

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketNotificationConfiguration')
    members = operation_model.input_shape.members


class PutBucketPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Policy: str
    ContentMD5: str = None
    ConfirmRemoveSelfBucketAccess: bool = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketPolicy')
    members = operation_model.input_shape.members


class PutBucketReplicationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ReplicationConfiguration: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketReplication')
    members = operation_model.input_shape.members


class PutBucketRequestPaymentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    RequestPaymentConfiguration: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketRequestPayment')
    members = operation_model.input_shape.members


class PutBucketTaggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Tagging: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketTagging')
    members = operation_model.input_shape.members


class PutBucketVersioningRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    VersioningConfiguration: dict
    ContentMD5: str = None
    MFA: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketVersioning')
    members = operation_model.input_shape.members


class PutBucketWebsiteRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    WebsiteConfiguration: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutBucketWebsite')
    members = operation_model.input_shape.members


class PutObjectRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    ACL: str = None
    Body: bytes = None
    CacheControl: str = None
    ContentDisposition: str = None
    ContentEncoding: str = None
    ContentLanguage: str = None
    ContentLength: int = None
    ContentMD5: str = None
    ContentType: str = None
    Expires: TimeStamp = None
    GrantFullControl: str = None
    GrantRead: str = None
    GrantReadACP: str = None
    GrantWriteACP: str = None
    Metadata: Map = None
    ServerSideEncryption: str = None
    StorageClass: str = None
    WebsiteRedirectLocation: str = None
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    SSEKMSKeyId: str = None
    RequestPayer: str = None
    Tagging: str = None
    ObjectLockMode: str = None
    ObjectLockRetainUntilDate: TimeStamp = None
    ObjectLockLegalHoldStatus: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutObject')
    members = operation_model.input_shape.members


class PutObjectAclRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    ACL: str = None
    AccessControlPolicy: dict = None
    ContentMD5: str = None
    GrantFullControl: str = None
    GrantRead: str = None
    GrantReadACP: str = None
    GrantWrite: str = None
    GrantWriteACP: str = None
    RequestPayer: str = None
    VersionId: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutObjectAcl')
    members = operation_model.input_shape.members


class PutObjectLegalHoldRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    LegalHold: dict = None
    RequestPayer: str = None
    VersionId: str = None
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutObjectLegalHold')
    members = operation_model.input_shape.members


class PutObjectLockConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    ObjectLockConfiguration: dict = None
    RequestPayer: str = None
    Token: str = None
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutObjectLockConfiguration')
    members = operation_model.input_shape.members


class PutObjectRetentionRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    Retention: dict = None
    RequestPayer: str = None
    VersionId: str = None
    BypassGovernanceRetention: bool = None
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutObjectRetention')
    members = operation_model.input_shape.members


class PutObjectTaggingRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    Tagging: dict
    VersionId: str = None
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutObjectTagging')
    members = operation_model.input_shape.members


class PutPublicAccessBlockRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    PublicAccessBlockConfiguration: dict
    ContentMD5: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('PutPublicAccessBlock')
    members = operation_model.input_shape.members


class RestoreObjectRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    VersionId: str = None
    RestoreRequest: dict = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('RestoreObject')
    members = operation_model.input_shape.members


class SelectObjectContentRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    Expression: str
    ExpressionType: str
    InputSerialization: dict
    OutputSerialization: dict
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    RequestProgress: dict = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('SelectObjectContent')
    members = operation_model.input_shape.members


class UploadPartRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    Key: str
    PartNumber: int
    UploadId: str
    Body: bytes = None
    ContentLength: int = None
    ContentMD5: str = None
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('UploadPart')
    members = operation_model.input_shape.members


class UploadPartCopyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Bucket: str
    CopySource: str
    Key: str
    PartNumber: int
    UploadId: str
    CopySourceIfMatch: str = None
    CopySourceIfModifiedSince: TimeStamp = None
    CopySourceIfNoneMatch: str = None
    CopySourceIfUnmodifiedSince: TimeStamp = None
    CopySourceRange: str = None
    SSECustomerAlgorithm: str = None
    SSECustomerKey: str = None
    SSECustomerKeyMD5: str = None
    CopySourceSSECustomerAlgorithm: str = None
    CopySourceSSECustomerKey: str = None
    CopySourceSSECustomerKeyMD5: str = None
    RequestPayer: str = None

    operation_model = botocore.session.Session().get_service_model('s3').operation_model('UploadPartCopy')
    members = operation_model.input_shape.members
