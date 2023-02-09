# jhc_cf_sdk_test.model.access_rule.AccessRule

Access Rule contains information for an end user to make a request for access.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Access Rule contains information for an end user to make a request for access. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timeConstraints** | [**TimeConstraints**](TimeConstraints.md) | [**TimeConstraints**](TimeConstraints.md) |  | 
**createdAt** | str,  | str,  |  | 
**isCurrent** | bool,  | BoolClass,  |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**version** | str,  | str,  | A unique version identifier for the Access Rule. Updating a rule creates a new version.  When a rule is updated, it&#x27;s ID remains consistent.  | 
**target** | [**AccessRuleTarget**](AccessRuleTarget.md) | [**AccessRuleTarget**](AccessRuleTarget.md) |  | 
**updatedAt** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

