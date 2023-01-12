<a name="__pageTop"></a>
# jhc_cf_sdk_test.apis.tags.end_user_api.EndUserApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_get_request**](#admin_get_request) | **get** /api/v1/admin/requests/{requestId} | Get a request
[**user_cancel_request**](#user_cancel_request) | **post** /api/v1/requests/{requestId}/cancel | Cancel a request
[**user_create_favorite**](#user_create_favorite) | **post** /api/v1/favorites | Create Favorite
[**user_create_request**](#user_create_request) | **post** /api/v1/requests | Create a request
[**user_delete_favorite**](#user_delete_favorite) | **delete** /api/v1/favorites/{id} | 
[**user_get_access_instructions**](#user_get_access_instructions) | **get** /api/v1/requests/{requestId}/access-instructions | Get Access Instructions
[**user_get_access_rule**](#user_get_access_rule) | **get** /api/v1/access-rules/{ruleId} | Get Access Rule
[**user_get_access_rule_approvers**](#user_get_access_rule_approvers) | **get** /api/v1/access-rules/{ruleId}/approvers | List Access Rule approvers
[**user_get_access_token**](#user_get_access_token) | **get** /api/v1/requests/{requestId}/access-token | Get Access Token
[**user_get_favorite**](#user_get_favorite) | **get** /api/v1/favorites/{id} | Get Favorite
[**user_get_me**](#user_get_me) | **get** /api/v1/users/me | Get details for the current user
[**user_get_request**](#user_get_request) | **get** /api/v1/requests/{requestId} | Get a request
[**user_get_user**](#user_get_user) | **get** /api/v1/users/{userId} | Get a user
[**user_list_access_rules**](#user_list_access_rules) | **get** /api/v1/access-rules | List Access Rules
[**user_list_favorites**](#user_list_favorites) | **get** /api/v1/favorites | ListFavorites
[**user_list_request_events**](#user_list_request_events) | **get** /api/v1/requests/{requestId}/events | List request events
[**user_list_requests**](#user_list_requests) | **get** /api/v1/requests | List my requests
[**user_list_requests_past**](#user_list_requests_past) | **get** /api/v1/requests/past | Your GET endpoint
[**user_list_requests_upcoming**](#user_list_requests_upcoming) | **get** /api/v1/requests/upcoming | Your GET endpoint
[**user_lookup_access_rule**](#user_lookup_access_rule) | **get** /api/v1/access-rules/lookup | Lookup an access rule based on the target
[**user_review_request**](#user_review_request) | **post** /api/v1/requests/{requestId}/review | Review a request
[**user_revoke_request**](#user_revoke_request) | **post** /api/v1/requests/{requestid}/revoke | Revoke an active request
[**user_update_favorite**](#user_update_favorite) | **put** /api/v1/favorites/{id} | 

# **admin_get_request**
<a name="admin_get_request"></a>
> RequestDetail admin_get_request(request_id)

Get a request

Returns an access request.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request_detail import RequestDetail
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestId': "requestId_example",
    }
    try:
        # Get a request
        api_response = api_instance.admin_get_request(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->admin_get_request: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestId | RequestIdSchema | | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#admin_get_request.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#admin_get_request.ApiResponseFor404) | An error returned from the service.
500 | [ApiResponseFor500](#admin_get_request.ApiResponseFor500) | An error returned from the service.

#### admin_get_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestDetail**](../../models/RequestDetail.md) |  | 


#### admin_get_request.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### admin_get_request.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_cancel_request**
<a name="user_cancel_request"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_cancel_request(request_id)

Cancel a request

Users can cancel an access request that they have created while it is in the PENDING state.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestId': "requestId_example",
    }
    try:
        # Cancel a request
        api_response = api_instance.user_cancel_request(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_cancel_request: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestId | RequestIdSchema | | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_cancel_request.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#user_cancel_request.ApiResponseFor400) | An error returned from the service.
404 | [ApiResponseFor404](#user_cancel_request.ApiResponseFor404) | An error returned from the service.
500 | [ApiResponseFor500](#user_cancel_request.ApiResponseFor500) | An error returned from the service.

#### user_cancel_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### user_cancel_request.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_cancel_request.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_cancel_request.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_create_favorite**
<a name="user_create_favorite"></a>
> FavoriteDetail user_create_favorite()

Create Favorite

Favorites an access request for a given user. This is used for frequent access requests saving time and repeated actions. 

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.favorite_detail import FavoriteDetail
from jhc_cf_sdk_test.model.request_timing import RequestTiming
from jhc_cf_sdk_test.model.create_request_with_sub_request import CreateRequestWithSubRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only optional values
    body = dict(
        access_rule_id="6",
        reason="",
        timing=RequestTiming(
            duration_seconds=1,
            start_time="start_time_example",
        ),
        _with=CreateRequestWithSubRequest([
            CreateRequestWith(
                key=[
                    "key_example"
                ],
            )
        ]),
        name="name_example",
    )
    try:
        # Create Favorite
        api_response = api_instance.user_create_favorite(
            body=body,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_create_favorite: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accessRuleId** | str,  | str,  |  | 
**timing** | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) |  | 
**name** | str,  | str,  |  | 
**reason** | str,  | str,  |  | [optional] 
**with** | [**CreateRequestWithSubRequest**]({{complexTypePrefix}}CreateRequestWithSubRequest.md) | [**CreateRequestWithSubRequest**]({{complexTypePrefix}}CreateRequestWithSubRequest.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#user_create_favorite.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#user_create_favorite.ApiResponseFor400) | An error returned from the service.
500 | [ApiResponseFor500](#user_create_favorite.ApiResponseFor500) | An error returned from the service.

#### user_create_favorite.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FavoriteDetail**](../../models/FavoriteDetail.md) |  | 


#### user_create_favorite.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_create_favorite.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_create_request**
<a name="user_create_request"></a>
> user_create_request()

Create a request

Make a request to access something.  Users must specify an Access Rule when making a request. Users are authorized to make a request if they are in a group that the Access Rule references. Otherwise, a HTTP 404 response will be returned.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request_timing import RequestTiming
from jhc_cf_sdk_test.model.create_request_with_sub_request import CreateRequestWithSubRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only optional values
    body = dict(
        access_rule_id="6",
        reason="reason_example",
        timing=RequestTiming(
            duration_seconds=1,
            start_time="start_time_example",
        ),
        _with=CreateRequestWithSubRequest([
            CreateRequestWith(
                key=[
                    "key_example"
                ],
            )
        ]),
    )
    try:
        # Create a request
        api_response = api_instance.user_create_request(
            body=body,
        )
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_create_request: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accessRuleId** | str,  | str,  |  | 
**timing** | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) |  | 
**reason** | str,  | str,  |  | [optional] 
**with** | [**CreateRequestWithSubRequest**]({{complexTypePrefix}}CreateRequestWithSubRequest.md) | [**CreateRequestWithSubRequest**]({{complexTypePrefix}}CreateRequestWithSubRequest.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_create_request.ApiResponseFor200) | OK

#### user_create_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_delete_favorite**
<a name="user_delete_favorite"></a>
> user_delete_favorite(id)



Delete a saved favorite

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.user_delete_favorite(
            path_params=path_params,
        )
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_delete_favorite: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_delete_favorite.ApiResponseFor200) | OK

#### user_delete_favorite.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_access_instructions**
<a name="user_get_access_instructions"></a>
> AccessInstructions user_get_access_instructions(request_id)

Get Access Instructions

Get access instructions for a request.  Returns information on how to access the role or resource.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.access_instructions import AccessInstructions
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestId': "requestId_example",
    }
    try:
        # Get Access Instructions
        api_response = api_instance.user_get_access_instructions(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_access_instructions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestId | RequestIdSchema | | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_access_instructions.ApiResponseFor200) | OK

#### user_get_access_instructions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AccessInstructions**](../../models/AccessInstructions.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_access_rule**
<a name="user_get_access_rule"></a>
> RequestAccessRule user_get_access_rule(rule_id)

Get Access Rule

Get details for an Access Rule.  End users are only able to view Access Rules if they are a member of the group the rule relates to, or if they are designated as an approver for the Access Rule. If a user doesn't meet these conditions, a HTTP401 unauthorized error is returned.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request_access_rule import RequestAccessRule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ruleId': "ruleId_example",
    }
    try:
        # Get Access Rule
        api_response = api_instance.user_get_access_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_access_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ruleId | RuleIdSchema | | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_access_rule.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#user_get_access_rule.ApiResponseFor401) | An error returned from the service.
404 | [ApiResponseFor404](#user_get_access_rule.ApiResponseFor404) | An error returned from the service.

#### user_get_access_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestAccessRule**](../../models/RequestAccessRule.md) |  | 


#### user_get_access_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_get_access_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_access_rule_approvers**
<a name="user_get_access_rule_approvers"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_get_access_rule_approvers(rule_id)

List Access Rule approvers

Get the approvers for an access rule.  This returns a list of user IDs.  End users are only able to view Access Rules if they are a member of the group the rule relates to, or if they are designated as an approver for the Access Rule. If a user doesn't meet these conditions, a HTTP401 unauthorized error is returned.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ruleId': "ruleId_example",
    }
    try:
        # List Access Rule approvers
        api_response = api_instance.user_get_access_rule_approvers(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_access_rule_approvers: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ruleId | RuleIdSchema | | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_access_rule_approvers.ApiResponseFor200) | A list of user ids who can approver an access rule request
401 | [ApiResponseFor401](#user_get_access_rule_approvers.ApiResponseFor401) | An error returned from the service.
404 | [ApiResponseFor404](#user_get_access_rule_approvers.ApiResponseFor404) | An error returned from the service.

#### user_get_access_rule_approvers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | None, str,  | NoneClass, str,  |  | 
**[users](#users)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### user_get_access_rule_approvers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_get_access_rule_approvers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_access_token**
<a name="user_get_access_token"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_get_access_token(request_id)

Get Access Token

Get access token for a request.  Returns information on how to access the role or resource.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestId': "requestId_example",
    }
    try:
        # Get Access Token
        api_response = api_instance.user_get_access_token(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_access_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestId | RequestIdSchema | | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_access_token.ApiResponseFor200) | If the request has an access token, hasToken will be true
404 | [ApiResponseFor404](#user_get_access_token.ApiResponseFor404) | An error returned from the service.
500 | [ApiResponseFor500](#user_get_access_token.ApiResponseFor500) | An error returned from the service.

#### user_get_access_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hasToken** | bool,  | BoolClass,  |  | 
**token** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_get_access_token.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_get_access_token.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_favorite**
<a name="user_get_favorite"></a>
> FavoriteDetail user_get_favorite(id)

Get Favorite

Returns a detailed favorite response. This is used to display a favorite's details on the frontend. 

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.favorite_detail import FavoriteDetail
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get Favorite
        api_response = api_instance.user_get_favorite(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_favorite: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_favorite.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#user_get_favorite.ApiResponseFor404) | An error returned from the service.
500 | [ApiResponseFor500](#user_get_favorite.ApiResponseFor500) | An error returned from the service.

#### user_get_favorite.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FavoriteDetail**](../../models/FavoriteDetail.md) |  | 


#### user_get_favorite.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_get_favorite.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_me**
<a name="user_get_me"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_get_me()

Get details for the current user

Returns information about the currently logged in user.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get details for the current user
        api_response = api_instance.user_get_me()
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_me: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_me.ApiResponseFor200) | Details about the authenticated user
401 | [ApiResponseFor401](#user_get_me.ApiResponseFor401) | Unauthorized

#### user_get_me.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**isAdmin** | bool,  | BoolClass,  | Whether the user is an administrator of Common Fate. | 
**user** | [**User**]({{complexTypePrefix}}User.md) | [**User**]({{complexTypePrefix}}User.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_get_me.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_request**
<a name="user_get_request"></a>
> RequestDetail user_get_request(request_id)

Get a request

Returns a HTTP401 response if the user is not the requestor or a reviewer.   Use /api/v1/admin/requests/{requestId} as an administrator to view information for requests not made by the current user (note: requires that the user is a Common Fate administrator).

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request_detail import RequestDetail
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestId': "requestId_example",
    }
    try:
        # Get a request
        api_response = api_instance.user_get_request(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_request: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestId | RequestIdSchema | | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_request.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#user_get_request.ApiResponseFor404) | An error returned from the service.
500 | [ApiResponseFor500](#user_get_request.ApiResponseFor500) | An error returned from the service.

#### user_get_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestDetail**](../../models/RequestDetail.md) |  | 


#### user_get_request.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_get_request.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get_user**
<a name="user_get_user"></a>
> User user_get_user(user_id)

Get a user

Returns a Common Fate user.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "userId_example",
    }
    try:
        # Get a user
        api_response = api_instance.user_get_user(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_get_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get_user.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#user_get_user.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#user_get_user.ApiResponseFor404) | Not Found

#### user_get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**User**](../../models/User.md) |  | 


#### user_get_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### user_get_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_list_access_rules**
<a name="user_list_access_rules"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_list_access_rules()

List Access Rules

Get all access rules as an end user.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.access_rule import AccessRule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Access Rules
        api_response = api_instance.user_list_access_rules()
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_list_access_rules: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_list_access_rules.ApiResponseFor200) | A list of Access Rules.

#### user_list_access_rules.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | None, str,  | NoneClass, str,  |  | 
**[accessRules](#accessRules)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accessRules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccessRule**]({{complexTypePrefix}}AccessRule.md) | [**AccessRule**]({{complexTypePrefix}}AccessRule.md) | [**AccessRule**]({{complexTypePrefix}}AccessRule.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_list_favorites**
<a name="user_list_favorites"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_list_favorites()

ListFavorites

Returns a list of the user's favourited access requests. 

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.favorite import Favorite
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ListFavorites
        api_response = api_instance.user_list_favorites()
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_list_favorites: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_list_favorites.ApiResponseFor200) | Returns a list of Favorites
500 | [ApiResponseFor500](#user_list_favorites.ApiResponseFor500) | An error returned from the service.

#### user_list_favorites.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[favorites](#favorites)** | list, tuple,  | tuple,  |  | 
**next** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# favorites

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Favorite**]({{complexTypePrefix}}Favorite.md) | [**Favorite**]({{complexTypePrefix}}Favorite.md) | [**Favorite**]({{complexTypePrefix}}Favorite.md) |  | 

#### user_list_favorites.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_list_request_events**
<a name="user_list_request_events"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_list_request_events(request_id)

List request events

Returns a HTTP401 response if the user is not the requestor or a reviewer. 

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request_event import RequestEvent
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestId': "requestId_example",
    }
    try:
        # List request events
        api_response = api_instance.user_list_request_events(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_list_request_events: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestId | RequestIdSchema | | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_list_request_events.ApiResponseFor200) | Paginated list of RequestEvent
401 | [ApiResponseFor401](#user_list_request_events.ApiResponseFor401) | An error returned from the service.
500 | [ApiResponseFor500](#user_list_request_events.ApiResponseFor500) | An error returned from the service.

#### user_list_request_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | None, str,  | NoneClass, str,  |  | 
**[events](#events)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# events

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RequestEvent**]({{complexTypePrefix}}RequestEvent.md) | [**RequestEvent**]({{complexTypePrefix}}RequestEvent.md) | [**RequestEvent**]({{complexTypePrefix}}RequestEvent.md) |  | 

#### user_list_request_events.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_list_request_events.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_list_requests**
<a name="user_list_requests"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_list_requests()

List my requests

List requests. The reviewer query param allows you to fetch requests which you can review.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request import Request
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only optional values
    query_params = {
        'status': "APPROVED",
        'reviewer': True,
        'nextToken': "nextToken_example",
    }
    try:
        # List my requests
        api_response = api_instance.user_list_requests(
            query_params=query_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_list_requests: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
status | StatusSchema | | optional
reviewer | ReviewerSchema | | optional
nextToken | NextTokenSchema | | optional


# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["APPROVED", "DECLINED", "CANCELLED", "PENDING", ] 

# ReviewerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NextTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_list_requests.ApiResponseFor200) | Paginated list of Requests

#### user_list_requests.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | None, str,  | NoneClass, str,  |  | 
**[requests](#requests)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# requests

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Request**]({{complexTypePrefix}}Request.md) | [**Request**]({{complexTypePrefix}}Request.md) | [**Request**]({{complexTypePrefix}}Request.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_list_requests_past**
<a name="user_list_requests_past"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_list_requests_past()

Your GET endpoint

Display show cancelled, expired, and revoked requests. 

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request import Request
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only optional values
    query_params = {
        'nextToken': "nextToken_example",
    }
    try:
        # Your GET endpoint
        api_response = api_instance.user_list_requests_past(
            query_params=query_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_list_requests_past: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
nextToken | NextTokenSchema | | optional


# NextTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_list_requests_past.ApiResponseFor200) | Paginated list of Requests

#### user_list_requests_past.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | None, str,  | NoneClass, str,  |  | 
**[requests](#requests)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# requests

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Request**]({{complexTypePrefix}}Request.md) | [**Request**]({{complexTypePrefix}}Request.md) | [**Request**]({{complexTypePrefix}}Request.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_list_requests_upcoming**
<a name="user_list_requests_upcoming"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_list_requests_upcoming()

Your GET endpoint

Display pending requests and approved requests that are currently active or scheduled to begin some time in future.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.request import Request
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only optional values
    query_params = {
        'nextToken': "nextToken_example",
    }
    try:
        # Your GET endpoint
        api_response = api_instance.user_list_requests_upcoming(
            query_params=query_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_list_requests_upcoming: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
nextToken | NextTokenSchema | | optional


# NextTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_list_requests_upcoming.ApiResponseFor200) | Paginated list of Requests

#### user_list_requests_upcoming.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | None, str,  | NoneClass, str,  |  | 
**[requests](#requests)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# requests

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Request**]({{complexTypePrefix}}Request.md) | [**Request**]({{complexTypePrefix}}Request.md) | [**Request**]({{complexTypePrefix}}Request.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_lookup_access_rule**
<a name="user_lookup_access_rule"></a>
> [LookupAccessRule] user_lookup_access_rule()

Lookup an access rule based on the target

Endpoint returns an array of relevant access rules (used in combination with granted cli)

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.lookup_access_rule import LookupAccessRule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only optional values
    query_params = {
        'type': "commonfate/aws-sso",
        'permissionSetArn.label': "permissionSetArn.label_example",
        'accountId': "accountId_example",
    }
    try:
        # Lookup an access rule based on the target
        api_response = api_instance.user_lookup_access_rule(
            query_params=query_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_lookup_access_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional
permissionSetArn.label | PermissionSetArnLabelSchema | | optional
accountId | AccountIdSchema | | optional


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["commonfate/aws-sso", ] 

# PermissionSetArnLabelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_lookup_access_rule.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#user_lookup_access_rule.ApiResponseFor404) | An error returned from the service.

#### user_lookup_access_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LookupAccessRule**]({{complexTypePrefix}}LookupAccessRule.md) | [**LookupAccessRule**]({{complexTypePrefix}}LookupAccessRule.md) | [**LookupAccessRule**]({{complexTypePrefix}}LookupAccessRule.md) |  | 

#### user_lookup_access_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_review_request**
<a name="user_review_request"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_review_request(request_id)

Review a request

Review an access request made by a user. The reviewing user must be an approver for a request. Users cannot review their own requests, even if they are an approver for the Access Rule.

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.review_decision import ReviewDecision
from jhc_cf_sdk_test.model.request import Request
from jhc_cf_sdk_test.model.request_timing import RequestTiming
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestId': "requestId_example",
    }
    try:
        # Review a request
        api_response = api_instance.user_review_request(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_review_request: %s\n" % e)

    # example passing only optional values
    path_params = {
        'requestId': "requestId_example",
    }
    body = dict(
        decision=ReviewDecision("APPROVED"),
        comment="comment_example",
        override_timing=RequestTiming(
            duration_seconds=1,
            start_time="start_time_example",
        ),
    )
    try:
        # Review a request
        api_response = api_instance.user_review_request(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_review_request: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**decision** | [**ReviewDecision**]({{complexTypePrefix}}ReviewDecision.md) | [**ReviewDecision**]({{complexTypePrefix}}ReviewDecision.md) |  | 
**comment** | str,  | str,  |  | [optional] 
**overrideTiming** | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestId | RequestIdSchema | | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_review_request.ApiResponseFor200) | Response for reviewing a request.

#### user_review_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request** | [**Request**]({{complexTypePrefix}}Request.md) | [**Request**]({{complexTypePrefix}}Request.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_revoke_request**
<a name="user_revoke_request"></a>
> user_revoke_request(requestid)

Revoke an active request

Admins and approvers can revoke access previously approved. Effective immediately 

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'requestid': "requestid_example",
    }
    try:
        # Revoke an active request
        api_response = api_instance.user_revoke_request(
            path_params=path_params,
        )
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_revoke_request: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
requestid | RequestidSchema | | 

# RequestidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_revoke_request.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#user_revoke_request.ApiResponseFor400) | An error returned from the service.
404 | [ApiResponseFor404](#user_revoke_request.ApiResponseFor404) | An error returned from the service.
500 | [ApiResponseFor500](#user_revoke_request.ApiResponseFor500) | An error returned from the service.

#### user_revoke_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### user_revoke_request.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_revoke_request.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### user_revoke_request.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_update_favorite**
<a name="user_update_favorite"></a>
> FavoriteDetail user_update_favorite(id)



Update a favorite with new FavoriteDetails

### Example

```python
import jhc_cf_sdk_test
from jhc_cf_sdk_test.apis.tags import end_user_api
from jhc_cf_sdk_test.model.favorite_detail import FavoriteDetail
from jhc_cf_sdk_test.model.request_timing import RequestTiming
from jhc_cf_sdk_test.model.create_request_with_sub_request import CreateRequestWithSubRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = jhc_cf_sdk_test.Configuration(
    host = "http://localhost:8080"
)

# Enter a context with an instance of the API client
with jhc_cf_sdk_test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = end_user_api.EndUserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.user_update_favorite(
            path_params=path_params,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_update_favorite: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    body = dict(
        access_rule_id="6",
        reason="",
        timing=RequestTiming(
            duration_seconds=1,
            start_time="start_time_example",
        ),
        _with=CreateRequestWithSubRequest([
            CreateRequestWith(
                key=[
                    "key_example"
                ],
            )
        ]),
        name="name_example",
    )
    try:
        api_response = api_instance.user_update_favorite(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except jhc_cf_sdk_test.ApiException as e:
        print("Exception when calling EndUserApi->user_update_favorite: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accessRuleId** | str,  | str,  |  | 
**timing** | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) | [**RequestTiming**]({{complexTypePrefix}}RequestTiming.md) |  | 
**name** | str,  | str,  |  | 
**reason** | str,  | str,  |  | [optional] 
**with** | [**CreateRequestWithSubRequest**]({{complexTypePrefix}}CreateRequestWithSubRequest.md) | [**CreateRequestWithSubRequest**]({{complexTypePrefix}}CreateRequestWithSubRequest.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_update_favorite.ApiResponseFor200) | OK

#### user_update_favorite.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FavoriteDetail**](../../models/FavoriteDetail.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

