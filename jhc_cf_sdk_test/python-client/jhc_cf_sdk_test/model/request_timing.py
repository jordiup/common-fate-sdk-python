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


class RequestTiming(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "durationSeconds",
        }
        
        class properties:
            durationSeconds = schemas.IntSchema
            startTime = schemas.StrSchema
            __annotations__ = {
                "durationSeconds": durationSeconds,
                "startTime": startTime,
            }
    
    durationSeconds: MetaOapg.properties.durationSeconds
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["durationSeconds"]) -> MetaOapg.properties.durationSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["durationSeconds", "startTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["durationSeconds"]) -> MetaOapg.properties.durationSeconds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> typing.Union[MetaOapg.properties.startTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["durationSeconds", "startTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        durationSeconds: typing.Union[MetaOapg.properties.durationSeconds, decimal.Decimal, int, ],
        startTime: typing.Union[MetaOapg.properties.startTime, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequestTiming':
        return super().__new__(
            cls,
            *_args,
            durationSeconds=durationSeconds,
            startTime=startTime,
            _configuration=_configuration,
            **kwargs,
        )
