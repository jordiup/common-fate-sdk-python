# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from jhc_cf_sdk_test.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_ACCESSRULES = "/api/v1/access-rules"
    API_V1_ACCESSRULES_RULE_ID = "/api/v1/access-rules/{ruleId}"
    API_V1_ACCESSRULES_RULE_ID_APPROVERS = "/api/v1/access-rules/{ruleId}/approvers"
    API_V1_REQUESTS = "/api/v1/requests"
    API_V1_REQUESTS_UPCOMING = "/api/v1/requests/upcoming"
    API_V1_REQUESTS_PAST = "/api/v1/requests/past"
    API_V1_REQUESTS_REQUEST_ID = "/api/v1/requests/{requestId}"
    API_V1_REQUESTS_REQUEST_ID_EVENTS = "/api/v1/requests/{requestId}/events"
    API_V1_REQUESTS_REQUEST_ID_REVIEW = "/api/v1/requests/{requestId}/review"
    API_V1_REQUESTS_REQUEST_ID_CANCEL = "/api/v1/requests/{requestId}/cancel"
    API_V1_REQUESTS_REQUESTID_REVOKE = "/api/v1/requests/{requestid}/revoke"
    API_V1_REQUESTS_REQUEST_ID_ACCESSINSTRUCTIONS = "/api/v1/requests/{requestId}/access-instructions"
    API_V1_REQUESTS_REQUEST_ID_ACCESSTOKEN = "/api/v1/requests/{requestId}/access-token"
    API_V1_USERS_USER_ID = "/api/v1/users/{userId}"
    API_V1_USERS_ME = "/api/v1/users/me"
    API_V1_ADMIN_ACCESSRULES = "/api/v1/admin/access-rules"
    API_V1_ADMIN_ACCESSRULES_RULE_ID = "/api/v1/admin/access-rules/{ruleId}"
    API_V1_ADMIN_ACCESSRULES_RULE_ID_ARCHIVE = "/api/v1/admin/access-rules/{ruleId}/archive"
    API_V1_ADMIN_ACCESSRULES_RULE_ID_VERSIONS = "/api/v1/admin/access-rules/{ruleId}/versions"
    API_V1_ADMIN_ACCESSRULES_RULE_ID_VERSIONS_VERSION = "/api/v1/admin/access-rules/{ruleId}/versions/{version}"
    API_V1_ADMIN_DEPLOYMENT_VERSION = "/api/v1/admin/deployment/version"
    API_V1_ADMIN_REQUESTS = "/api/v1/admin/requests"
    API_V1_ADMIN_REQUESTS_REQUEST_ID = "/api/v1/admin/requests/{requestId}"
    API_V1_ADMIN_USERS_USER_ID = "/api/v1/admin/users/{userId}"
    API_V1_ADMIN_USERS = "/api/v1/admin/users"
    API_V1_ADMIN_GROUPS = "/api/v1/admin/groups"
    API_V1_ADMIN_GROUPS_GROUP_ID = "/api/v1/admin/groups/{groupId}"
    API_V1_ADMIN_PROVIDERS = "/api/v1/admin/providers"
    API_V1_ADMIN_PROVIDERS_PROVIDER_ID = "/api/v1/admin/providers/{providerId}"
    API_V1_ADMIN_PROVIDERS_PROVIDER_ID_ARGS = "/api/v1/admin/providers/{providerId}/args"
    API_V1_ADMIN_PROVIDERS_PROVIDER_ID_ARGS_ARG_ID_OPTIONS = "/api/v1/admin/providers/{providerId}/args/{argId}/options"
    API_V1_ADMIN_PROVIDERSETUPS = "/api/v1/admin/providersetups"
    API_V1_ADMIN_PROVIDERSETUPS_PROVIDERSETUP_ID = "/api/v1/admin/providersetups/{providersetupId}"
    API_V1_ADMIN_PROVIDERSETUPS_PROVIDERSETUP_ID_INSTRUCTIONS = "/api/v1/admin/providersetups/{providersetupId}/instructions"
    API_V1_ADMIN_PROVIDERSETUPS_PROVIDERSETUP_ID_VALIDATE = "/api/v1/admin/providersetups/{providersetupId}/validate"
    API_V1_ADMIN_PROVIDERSETUPS_PROVIDERSETUP_ID_COMPLETE = "/api/v1/admin/providersetups/{providersetupId}/complete"
    API_V1_ADMIN_PROVIDERSETUPS_PROVIDERSETUP_ID_STEPS_STEP_INDEX_COMPLETE = "/api/v1/admin/providersetups/{providersetupId}/steps/{stepIndex}/complete"
    API_V1_ADMIN_IDENTITY_SYNC = "/api/v1/admin/identity/sync"
    API_V1_ADMIN_IDENTITY = "/api/v1/admin/identity"
    API_V1_ACCESSRULES_LOOKUP = "/api/v1/access-rules/lookup"
    API_V1_FAVORITES = "/api/v1/favorites"
    API_V1_FAVORITES_ID = "/api/v1/favorites/{id}"
