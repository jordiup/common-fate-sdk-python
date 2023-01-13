import typing_extensions

from jhc_cf_sdk_test.apis.tags import TagValues
from jhc_cf_sdk_test.apis.tags.end_user_api import EndUserApi
from jhc_cf_sdk_test.apis.tags.admin_api import AdminApi
from jhc_cf_sdk_test.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.END_USER: EndUserApi,
        TagValues.ADMIN: AdminApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.END_USER: EndUserApi,
        TagValues.ADMIN: AdminApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
