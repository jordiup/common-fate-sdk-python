# jhc_cf_sdk_test.model.grant.Grant

A temporary assignment of a user to a principal.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A temporary assignment of a user to a principal. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**provider** | str,  | str,  | The ID of the provider to grant access to. | 
**subject** | str,  | str,  | The email address of the user to grant access to. | 
**start** | str, datetime,  | str,  | The start time of the grant. | value must conform to RFC-3339 date-time
**end** | str, datetime,  | str,  | The end time of the grant. | value must conform to RFC-3339 date-time
**status** | str,  | str,  | The current state of the grant. | must be one of ["PENDING", "ACTIVE", "ERROR", "REVOKED", "EXPIRED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

