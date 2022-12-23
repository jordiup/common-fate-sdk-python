# commonfate.model.request_detail.RequestDetail

A request to access something made by an end user in Common Fate.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A request to access something made by an end user in Common Fate. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**canReview** | bool,  | BoolClass,  | true if the requesting user is a reviewer of this request. | 
**requestedAt** | str,  | str,  |  | 
**timing** | [**RequestTiming**](RequestTiming.md) | [**RequestTiming**](RequestTiming.md) |  | 
**[arguments](#arguments)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**id** | str,  | str,  |  | 
**accessRule** | [**AccessRule**](AccessRule.md) | [**AccessRule**](AccessRule.md) |  | 
**requestor** | str,  | str,  |  | 
**status** | [**RequestStatus**](RequestStatus.md) | [**RequestStatus**](RequestStatus.md) |  | 
**updatedAt** | str,  | str,  |  | 
**reason** | str,  | str,  |  | [optional] 
**grant** | [**Grant**](Grant.md) | [**Grant**](Grant.md) |  | [optional] 
**approvalMethod** | [**ApprovalMethod**](ApprovalMethod.md) | [**ApprovalMethod**](ApprovalMethod.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# arguments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelWith**](ModelWith.md) | [**ModelWith**](ModelWith.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

