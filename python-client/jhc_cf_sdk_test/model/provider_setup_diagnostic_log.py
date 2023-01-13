# coding: utf-8

"""
    Approvals

    Granted Approvals API  # noqa: E501

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


class ProviderSetupDiagnosticLog(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A log entry related to a provider setup validation.
    """


    class MetaOapg:
        required = {
            "msg",
            "level",
        }
        
        class properties:
            
            
            class level(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "INFO": "INFO",
                        "WARNING": "WARNING",
                        "ERROR": "ERROR",
                    }
                
                @schemas.classproperty
                def INFO(cls):
                    return cls("INFO")
                
                @schemas.classproperty
                def WARNING(cls):
                    return cls("WARNING")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
            msg = schemas.StrSchema
            __annotations__ = {
                "level": level,
                "msg": msg,
            }
    
    msg: MetaOapg.properties.msg
    level: MetaOapg.properties.level
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["msg"]) -> MetaOapg.properties.msg: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["level", "msg", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["msg"]) -> MetaOapg.properties.msg: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["level", "msg", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        msg: typing.Union[MetaOapg.properties.msg, str, ],
        level: typing.Union[MetaOapg.properties.level, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProviderSetupDiagnosticLog':
        return super().__new__(
            cls,
            *_args,
            msg=msg,
            level=level,
            _configuration=_configuration,
            **kwargs,
        )
