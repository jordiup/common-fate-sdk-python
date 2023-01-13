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


class FavoriteDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "with",
            "timing",
            "name",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def _with() -> typing.Type['CreateRequestWithSubRequest']:
                return CreateRequestWithSubRequest
        
            @staticmethod
            def timing() -> typing.Type['RequestTiming']:
                return RequestTiming
            reason = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "with": _with,
                "timing": timing,
                "reason": reason,
            }
    
    timing: 'RequestTiming'
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["with"]) -> 'CreateRequestWithSubRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timing"]) -> 'RequestTiming': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "with", "timing", "reason", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["with"]) -> 'CreateRequestWithSubRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timing"]) -> 'RequestTiming': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "with", "timing", "reason", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timing: 'RequestTiming',
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FavoriteDetail':
        return super().__new__(
            cls,
            *_args,
            timing=timing,
            name=name,
            id=id,
            reason=reason,
            _configuration=_configuration,
            **kwargs,
        )

from jhc_cf_sdk_test.model.create_request_with_sub_request import CreateRequestWithSubRequest
from jhc_cf_sdk_test.model.request_timing import RequestTiming
