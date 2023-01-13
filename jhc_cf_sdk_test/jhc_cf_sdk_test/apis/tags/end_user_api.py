# coding: utf-8

"""
    Approvals

    Granted Approvals API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from jhc_cf_sdk_test.paths.api_v1_admin_requests_request_id.get import AdminGetRequest
from jhc_cf_sdk_test.paths.api_v1_requests_request_id_cancel.post import CancelRequest
from jhc_cf_sdk_test.paths.api_v1_requests_request_id_access_instructions.get import GetAccessInstructions
from jhc_cf_sdk_test.paths.api_v1_requests_request_id_access_token.get import GetAccessToken
from jhc_cf_sdk_test.paths.api_v1_users_me.get import GetMe
from jhc_cf_sdk_test.paths.api_v1_users_user_id.get import GetUser
from jhc_cf_sdk_test.paths.api_v1_requests_request_id_events.get import ListRequestEvents
from jhc_cf_sdk_test.paths.api_v1_access_rules.get import ListUserAccessRules
from jhc_cf_sdk_test.paths.api_v1_requests_request_id_review.post import ReviewRequest
from jhc_cf_sdk_test.paths.api_v1_requests_requestid_revoke.post import RevokeRequest
from jhc_cf_sdk_test.paths.api_v1_requests.post import UserCreateRequest
from jhc_cf_sdk_test.paths.api_v1_access_rules_rule_id.get import UserGetAccessRule
from jhc_cf_sdk_test.paths.api_v1_access_rules_rule_id_approvers.get import UserGetAccessRuleApprovers
from jhc_cf_sdk_test.paths.api_v1_requests_request_id.get import UserGetRequest
from jhc_cf_sdk_test.paths.api_v1_requests.get import UserListRequests


class EndUserApi(
    AdminGetRequest,
    CancelRequest,
    GetAccessInstructions,
    GetAccessToken,
    GetMe,
    GetUser,
    ListRequestEvents,
    ListUserAccessRules,
    ReviewRequest,
    RevokeRequest,
    UserCreateRequest,
    UserGetAccessRule,
    UserGetAccessRuleApprovers,
    UserGetRequest,
    UserListRequests,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
