# jhc_cf_sdk_test.model.provider_config_field.ProviderConfigField

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**isSecret** | bool,  | BoolClass,  | Whether or not the config field is a secret (like an API key or a password) | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**isOptional** | bool,  | BoolClass,  | Whether the config value is optional. | 
**secretPath** | str,  | str,  | the path to where the secret will be stored, in a secrets manager like AWS SSM Parameter Store. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

