# coding: utf-8

"""
    Common Fate

    Common Fate API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from jhc_cf_sdk_test import schemas  # noqa: F401


class ProviderSetup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A provider in the process of being set up through the guided setup workflow in Common Fate. These providers are **not** yet active.
    """


    class MetaOapg:
        required = {
            "configValues",
            "id",
            "type",
            "configValidation",
            "steps",
            "version",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            type = schemas.StrSchema
            version = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "COMPLETE": "COMPLETE",
                        "VALIDATION_FAILED": "VALIDATION_FAILED",
                        "VALIDATING": "VALIDATING",
                        "INITIAL_CONFIGURATION_IN_PROGRESS": "INITIAL_CONFIGURATION_IN_PROGRESS",
                        "VALIDATION_SUCEEDED": "VALIDATION_SUCEEDED",
                    }
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("COMPLETE")
                
                @schemas.classproperty
                def VALIDATION_FAILED(cls):
                    return cls("VALIDATION_FAILED")
                
                @schemas.classproperty
                def VALIDATING(cls):
                    return cls("VALIDATING")
                
                @schemas.classproperty
                def INITIAL_CONFIGURATION_IN_PROGRESS(cls):
                    return cls("INITIAL_CONFIGURATION_IN_PROGRESS")
                
                @schemas.classproperty
                def VALIDATION_SUCEEDED(cls):
                    return cls("VALIDATION_SUCEEDED")
            
            
            class steps(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ProviderSetupStepOverview']:
                        return ProviderSetupStepOverview
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ProviderSetupStepOverview'], typing.List['ProviderSetupStepOverview']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'steps':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProviderSetupStepOverview':
                    return super().__getitem__(i)
            
            
            class configValues(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.NotAnyTypeSchema
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'configValues':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class configValidation(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ProviderConfigValidation']:
                        return ProviderConfigValidation
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ProviderConfigValidation'], typing.List['ProviderConfigValidation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'configValidation':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProviderConfigValidation':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "type": type,
                "version": version,
                "status": status,
                "steps": steps,
                "configValues": configValues,
                "configValidation": configValidation,
            }
    
    configValues: MetaOapg.properties.configValues
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    configValidation: MetaOapg.properties.configValidation
    steps: MetaOapg.properties.steps
    version: MetaOapg.properties.version
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps"]) -> MetaOapg.properties.steps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configValues"]) -> MetaOapg.properties.configValues: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configValidation"]) -> MetaOapg.properties.configValidation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "version", "status", "steps", "configValues", "configValidation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps"]) -> MetaOapg.properties.steps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configValues"]) -> MetaOapg.properties.configValues: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configValidation"]) -> MetaOapg.properties.configValidation: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "version", "status", "steps", "configValues", "configValidation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        configValues: typing.Union[MetaOapg.properties.configValues, dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        configValidation: typing.Union[MetaOapg.properties.configValidation, list, tuple, ],
        steps: typing.Union[MetaOapg.properties.steps, list, tuple, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProviderSetup':
        return super().__new__(
            cls,
            *_args,
            configValues=configValues,
            id=id,
            type=type,
            configValidation=configValidation,
            steps=steps,
            version=version,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from jhc_cf_sdk_test.model.provider_config_validation import ProviderConfigValidation
from jhc_cf_sdk_test.model.provider_setup_step_overview import ProviderSetupStepOverview
