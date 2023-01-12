# jhc_cf_sdk_test.model.access_rule_detail.AccessRuleDetail

AccessRuleDetail contains detailed information about a rule and is used in administrative apis.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AccessRuleDetail contains detailed information about a rule and is used in administrative apis. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timeConstraints** | [**TimeConstraints**](TimeConstraints.md) | [**TimeConstraints**](TimeConstraints.md) |  | 
**isCurrent** | bool,  | BoolClass,  |  | 
**metadata** | [**AccessRuleMetadata**](AccessRuleMetadata.md) | [**AccessRuleMetadata**](AccessRuleMetadata.md) |  | 
**approval** | [**ApproverConfig**](ApproverConfig.md) | [**ApproverConfig**](ApproverConfig.md) |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**[groups](#groups)** | list, tuple,  | tuple,  | The group IDs that the access rule applies to. | 
**id** | str,  | str,  |  | 
**version** | str,  | str,  | A unique version identifier for the Access Rule. Updating a rule creates a new version.  When a rule is updated, it&#x27;s ID remains consistent.  | 
**status** | [**AccessRuleStatus**](AccessRuleStatus.md) | [**AccessRuleStatus**](AccessRuleStatus.md) |  | 
**target** | [**AccessRuleTargetDetail**](AccessRuleTargetDetail.md) | [**AccessRuleTargetDetail**](AccessRuleTargetDetail.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# groups

The group IDs that the access rule applies to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The group IDs that the access rule applies to. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

