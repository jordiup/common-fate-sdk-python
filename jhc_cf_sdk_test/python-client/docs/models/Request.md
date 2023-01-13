# jhc_cf_sdk_test.model.request.Request

A request to access something made by an end user in Granted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A request to access something made by an end user in Granted. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accessRuleId** | str,  | str,  |  | 
**requestedAt** | str,  | str,  |  | 
**accessRuleVersion** | str,  | str,  |  | 
**timing** | [**RequestTiming**](RequestTiming.md) | [**RequestTiming**](RequestTiming.md) |  | 
**id** | str,  | str,  |  | 
**requestor** | str,  | str,  |  | 
**status** | [**RequestStatus**](RequestStatus.md) | [**RequestStatus**](RequestStatus.md) |  | 
**updatedAt** | str,  | str,  |  | 
**reason** | str,  | str,  |  | [optional] 
**grant** | [**Grant**](Grant.md) | [**Grant**](Grant.md) |  | [optional] 
**approvalMethod** | [**ApprovalMethod**](ApprovalMethod.md) | [**ApprovalMethod**](ApprovalMethod.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

