import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.end_user_api import EndUserApi
from openapi_client.apis.tags.admin_api import AdminApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.END_USER: EndUserApi,
        TagValues.ADMIN: AdminApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.END_USER: EndUserApi,
        TagValues.ADMIN: AdminApi,
    }
)
