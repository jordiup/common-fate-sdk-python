# jhc_cf_sdk_test.model.provider_setup.ProviderSetup

A provider in the process of being set up through the guided setup workflow in Common Fate. These providers are **not** yet active.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A provider in the process of being set up through the guided setup workflow in Common Fate. These providers are **not** yet active. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[configValues](#configValues)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The current configuration values. | 
**id** | str,  | str,  | A unique ID for the provider setup. This is a random KSUID to avoid potential conflicts with user-specified provider IDs in the &#x60;deployment.yml&#x60; file. | 
**type** | str,  | str,  | The type of the Access Provider being set up. | 
**[configValidation](#configValidation)** | list, tuple,  | tuple,  |  | 
**[steps](#steps)** | list, tuple,  | tuple,  | An overview of the steps indicating whether they are complete. | 
**version** | str,  | str,  | The version of the provider. | 
**status** | str,  | str,  | The status of the setup process. | must be one of ["COMPLETE", "VALIDATION_FAILED", "VALIDATING", "INITIAL_CONFIGURATION_IN_PROGRESS", "VALIDATION_SUCEEDED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# steps

An overview of the steps indicating whether they are complete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An overview of the steps indicating whether they are complete. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProviderSetupStepOverview**](ProviderSetupStepOverview.md) | [**ProviderSetupStepOverview**](ProviderSetupStepOverview.md) | [**ProviderSetupStepOverview**](ProviderSetupStepOverview.md) |  | 

# configValues

The current configuration values.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The current configuration values. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------

# configValidation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProviderConfigValidation**](ProviderConfigValidation.md) | [**ProviderConfigValidation**](ProviderConfigValidation.md) | [**ProviderConfigValidation**](ProviderConfigValidation.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

