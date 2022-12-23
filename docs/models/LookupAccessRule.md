# commonfate.model.lookup_access_rule.LookupAccessRule

A matched access rule with option values if they are required for the access rule request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A matched access rule with option values if they are required for the access rule request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accessRule** | [**AccessRule**](AccessRule.md) | [**AccessRule**](AccessRule.md) |  | 
**[selectableWithOptionValues](#selectableWithOptionValues)** | list, tuple,  | tuple,  | If the matched access rule has selectable fields, this array will contain the matched values to be used to prefill the form when requesting | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# selectableWithOptionValues

If the matched access rule has selectable fields, this array will contain the matched values to be used to prefill the form when requesting

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | If the matched access rule has selectable fields, this array will contain the matched values to be used to prefill the form when requesting | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**KeyValue**](KeyValue.md) | [**KeyValue**](KeyValue.md) | [**KeyValue**](KeyValue.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

