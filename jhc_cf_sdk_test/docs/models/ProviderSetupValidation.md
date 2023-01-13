# jhc_cf_sdk_test.model.provider_setup_validation.ProviderSetupValidation

A validation against the configuration values of the Access Provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A validation against the configuration values of the Access Provider. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[fieldsValidated](#fieldsValidated)** | list, tuple,  | tuple,  | The particular config fields validated, if any. | 
**id** | str,  | str,  | The ID of the validation, such as &#x60;list-sso-users&#x60;. | 
**status** | str,  | str,  | The status of the validation. | must be one of ["IN_PROGRESS", "SUCCESS", "PENDING", "ERROR", ] 
**[logs](#logs)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fieldsValidated

The particular config fields validated, if any.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The particular config fields validated, if any. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# logs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProviderSetupDiagnosticLog**](ProviderSetupDiagnosticLog.md) | [**ProviderSetupDiagnosticLog**](ProviderSetupDiagnosticLog.md) | [**ProviderSetupDiagnosticLog**](ProviderSetupDiagnosticLog.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

