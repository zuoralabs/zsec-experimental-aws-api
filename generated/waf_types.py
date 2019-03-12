
import typing
import botocore.session
import aws_meta
from botocore.model import *

class TimeStamp(str):
    pass
    
class Map(dict):
    pass
    

class CreateByteMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateByteMatchSet')
    members = operation_model.input_shape.members


class CreateGeoMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateGeoMatchSet')
    members = operation_model.input_shape.members


class CreateIPSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateIPSet')
    members = operation_model.input_shape.members


class CreateRateBasedRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    MetricName: str
    RateKey: str
    RateLimit: int
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateRateBasedRule')
    members = operation_model.input_shape.members


class CreateRegexMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateRegexMatchSet')
    members = operation_model.input_shape.members


class CreateRegexPatternSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateRegexPatternSet')
    members = operation_model.input_shape.members


class CreateRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    MetricName: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateRule')
    members = operation_model.input_shape.members


class CreateRuleGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    MetricName: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateRuleGroup')
    members = operation_model.input_shape.members


class CreateSizeConstraintSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateSizeConstraintSet')
    members = operation_model.input_shape.members


class CreateSqlInjectionMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateSqlInjectionMatchSet')
    members = operation_model.input_shape.members


class CreateWebACLRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    MetricName: str
    DefaultAction: dict
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateWebACL')
    members = operation_model.input_shape.members


class CreateXssMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    Name: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('CreateXssMatchSet')
    members = operation_model.input_shape.members


class DeleteByteMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ByteMatchSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteByteMatchSet')
    members = operation_model.input_shape.members


class DeleteGeoMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GeoMatchSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteGeoMatchSet')
    members = operation_model.input_shape.members


class DeleteIPSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IPSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteIPSet')
    members = operation_model.input_shape.members


class DeleteLoggingConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteLoggingConfiguration')
    members = operation_model.input_shape.members


class DeletePermissionPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeletePermissionPolicy')
    members = operation_model.input_shape.members


class DeleteRateBasedRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteRateBasedRule')
    members = operation_model.input_shape.members


class DeleteRegexMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RegexMatchSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteRegexMatchSet')
    members = operation_model.input_shape.members


class DeleteRegexPatternSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RegexPatternSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteRegexPatternSet')
    members = operation_model.input_shape.members


class DeleteRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteRule')
    members = operation_model.input_shape.members


class DeleteRuleGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleGroupId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteRuleGroup')
    members = operation_model.input_shape.members


class DeleteSizeConstraintSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SizeConstraintSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteSizeConstraintSet')
    members = operation_model.input_shape.members


class DeleteSqlInjectionMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SqlInjectionMatchSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteSqlInjectionMatchSet')
    members = operation_model.input_shape.members


class DeleteWebACLRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WebACLId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteWebACL')
    members = operation_model.input_shape.members


class DeleteXssMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    XssMatchSetId: str
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('DeleteXssMatchSet')
    members = operation_model.input_shape.members


class GetByteMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ByteMatchSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetByteMatchSet')
    members = operation_model.input_shape.members


class GetChangeTokenRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)



    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetChangeToken')
    members = operation_model.input_shape.members


class GetChangeTokenStatusRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetChangeTokenStatus')
    members = operation_model.input_shape.members


class GetGeoMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GeoMatchSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetGeoMatchSet')
    members = operation_model.input_shape.members


class GetIPSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IPSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetIPSet')
    members = operation_model.input_shape.members


class GetLoggingConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetLoggingConfiguration')
    members = operation_model.input_shape.members


class GetPermissionPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetPermissionPolicy')
    members = operation_model.input_shape.members


class GetRateBasedRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetRateBasedRule')
    members = operation_model.input_shape.members


class GetRateBasedRuleManagedKeysRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleId: str
    NextMarker: str = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetRateBasedRuleManagedKeys')
    members = operation_model.input_shape.members


class GetRegexMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RegexMatchSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetRegexMatchSet')
    members = operation_model.input_shape.members


class GetRegexPatternSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RegexPatternSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetRegexPatternSet')
    members = operation_model.input_shape.members


class GetRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetRule')
    members = operation_model.input_shape.members


class GetRuleGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleGroupId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetRuleGroup')
    members = operation_model.input_shape.members


class GetSampledRequestsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WebAclId: str
    RuleId: str
    TimeWindow: dict
    MaxItems: int

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetSampledRequests')
    members = operation_model.input_shape.members


class GetSizeConstraintSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SizeConstraintSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetSizeConstraintSet')
    members = operation_model.input_shape.members


class GetSqlInjectionMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SqlInjectionMatchSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetSqlInjectionMatchSet')
    members = operation_model.input_shape.members


class GetWebACLRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WebACLId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetWebACL')
    members = operation_model.input_shape.members


class GetXssMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    XssMatchSetId: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('GetXssMatchSet')
    members = operation_model.input_shape.members


class ListActivatedRulesInRuleGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleGroupId: str = None
    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListActivatedRulesInRuleGroup')
    members = operation_model.input_shape.members


class ListByteMatchSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListByteMatchSets')
    members = operation_model.input_shape.members


class ListGeoMatchSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListGeoMatchSets')
    members = operation_model.input_shape.members


class ListIPSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListIPSets')
    members = operation_model.input_shape.members


class ListLoggingConfigurationsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListLoggingConfigurations')
    members = operation_model.input_shape.members


class ListRateBasedRulesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListRateBasedRules')
    members = operation_model.input_shape.members


class ListRegexMatchSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListRegexMatchSets')
    members = operation_model.input_shape.members


class ListRegexPatternSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListRegexPatternSets')
    members = operation_model.input_shape.members


class ListRuleGroupsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListRuleGroups')
    members = operation_model.input_shape.members


class ListRulesRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListRules')
    members = operation_model.input_shape.members


class ListSizeConstraintSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListSizeConstraintSets')
    members = operation_model.input_shape.members


class ListSqlInjectionMatchSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListSqlInjectionMatchSets')
    members = operation_model.input_shape.members


class ListSubscribedRuleGroupsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListSubscribedRuleGroups')
    members = operation_model.input_shape.members


class ListWebACLsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListWebACLs')
    members = operation_model.input_shape.members


class ListXssMatchSetsRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    NextMarker: str = None
    Limit: int = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('ListXssMatchSets')
    members = operation_model.input_shape.members


class PutLoggingConfigurationRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    LoggingConfiguration: dict

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('PutLoggingConfiguration')
    members = operation_model.input_shape.members


class PutPermissionPolicyRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ResourceArn: str
    Policy: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('PutPermissionPolicy')
    members = operation_model.input_shape.members


class UpdateByteMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    ByteMatchSetId: str
    ChangeToken: str
    Updates: list

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateByteMatchSet')
    members = operation_model.input_shape.members


class UpdateGeoMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    GeoMatchSetId: str
    ChangeToken: str
    Updates: list

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateGeoMatchSet')
    members = operation_model.input_shape.members


class UpdateIPSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    IPSetId: str
    ChangeToken: str
    Updates: list

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateIPSet')
    members = operation_model.input_shape.members


class UpdateRateBasedRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleId: str
    ChangeToken: str
    Updates: list
    RateLimit: int

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateRateBasedRule')
    members = operation_model.input_shape.members


class UpdateRegexMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RegexMatchSetId: str
    Updates: list
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateRegexMatchSet')
    members = operation_model.input_shape.members


class UpdateRegexPatternSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RegexPatternSetId: str
    Updates: list
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateRegexPatternSet')
    members = operation_model.input_shape.members


class UpdateRuleRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleId: str
    ChangeToken: str
    Updates: list

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateRule')
    members = operation_model.input_shape.members


class UpdateRuleGroupRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    RuleGroupId: str
    Updates: list
    ChangeToken: str

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateRuleGroup')
    members = operation_model.input_shape.members


class UpdateSizeConstraintSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SizeConstraintSetId: str
    ChangeToken: str
    Updates: list

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateSizeConstraintSet')
    members = operation_model.input_shape.members


class UpdateSqlInjectionMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    SqlInjectionMatchSetId: str
    ChangeToken: str
    Updates: list

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateSqlInjectionMatchSet')
    members = operation_model.input_shape.members


class UpdateWebACLRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    WebACLId: str
    ChangeToken: str
    Updates: list = None
    DefaultAction: dict = None

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateWebACL')
    members = operation_model.input_shape.members


class UpdateXssMatchSetRequest(typing.NamedTuple):

    def execute(self, svc):
        return aws_meta.execute(svc, self)

    XssMatchSetId: str
    ChangeToken: str
    Updates: list

    operation_model = botocore.session.Session().get_service_model('waf').operation_model('UpdateXssMatchSet')
    members = operation_model.input_shape.members
