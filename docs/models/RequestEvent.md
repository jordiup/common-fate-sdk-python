# jhc_cf_sdk_test.model.request_event.RequestEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | str,  | str,  |  | 
**requestId** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**actor** | str,  | str,  |  | [optional] 
**fromStatus** | [**RequestStatus**](RequestStatus.md) | [**RequestStatus**](RequestStatus.md) |  | [optional] 
**toStatus** | [**RequestStatus**](RequestStatus.md) | [**RequestStatus**](RequestStatus.md) |  | [optional] 
**fromTiming** | [**RequestTiming**](RequestTiming.md) | [**RequestTiming**](RequestTiming.md) |  | [optional] 
**toTiming** | [**RequestTiming**](RequestTiming.md) | [**RequestTiming**](RequestTiming.md) |  | [optional] 
**fromGrantStatus** | str,  | str,  | The current state of the grant. | [optional] must be one of ["PENDING", "ACTIVE", "ERROR", "REVOKED", "EXPIRED", ] 
**toGrantStatus** | str,  | str,  | The current state of the grant. | [optional] must be one of ["PENDING", "ACTIVE", "ERROR", "REVOKED", "EXPIRED", ] 
**grantCreated** | bool,  | BoolClass,  |  | [optional] 
**requestCreated** | bool,  | BoolClass,  |  | [optional] 
**grantFailureReason** | str,  | str,  |  | [optional] 
**[recordedEvent](#recordedEvent)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An event which was recorded relating to the grant. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# recordedEvent

An event which was recorded relating to the grant.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An event which was recorded relating to the grant. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

