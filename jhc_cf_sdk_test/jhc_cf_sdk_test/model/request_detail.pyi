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


class RequestDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A request to access something made by an end user in Common Fate.
    """


    class MetaOapg:
        required = {
            "canReview",
            "requestedAt",
            "timing",
            "arguments",
            "id",
            "accessRule",
            "requestor",
            "status",
            "updatedAt",
        }
        
        class properties:
            id = schemas.StrSchema
            requestor = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['RequestStatus']:
                return RequestStatus
        
            @staticmethod
            def timing() -> typing.Type['RequestTiming']:
                return RequestTiming
            requestedAt = schemas.StrSchema
        
            @staticmethod
            def accessRule() -> typing.Type['AccessRule']:
                return AccessRule
            updatedAt = schemas.StrSchema
            canReview = schemas.BoolSchema
            
            
            class arguments(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['ModelWith']:
                        return ModelWith
                
                def __getitem__(self, name: typing.Union[str, ]) -> 'ModelWith':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> 'ModelWith':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'ModelWith',
                ) -> 'arguments':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            reason = schemas.StrSchema
        
            @staticmethod
            def grant() -> typing.Type['Grant']:
                return Grant
        
            @staticmethod
            def approvalMethod() -> typing.Type['ApprovalMethod']:
                return ApprovalMethod
            __annotations__ = {
                "id": id,
                "requestor": requestor,
                "status": status,
                "timing": timing,
                "requestedAt": requestedAt,
                "accessRule": accessRule,
                "updatedAt": updatedAt,
                "canReview": canReview,
                "arguments": arguments,
                "reason": reason,
                "grant": grant,
                "approvalMethod": approvalMethod,
            }
    
    canReview: MetaOapg.properties.canReview
    requestedAt: MetaOapg.properties.requestedAt
    timing: 'RequestTiming'
    arguments: MetaOapg.properties.arguments
    id: MetaOapg.properties.id
    accessRule: 'AccessRule'
    requestor: MetaOapg.properties.requestor
    status: 'RequestStatus'
    updatedAt: MetaOapg.properties.updatedAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestor"]) -> MetaOapg.properties.requestor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'RequestStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timing"]) -> 'RequestTiming': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestedAt"]) -> MetaOapg.properties.requestedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessRule"]) -> 'AccessRule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canReview"]) -> MetaOapg.properties.canReview: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arguments"]) -> MetaOapg.properties.arguments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grant"]) -> 'Grant': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalMethod"]) -> 'ApprovalMethod': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "requestor", "status", "timing", "requestedAt", "accessRule", "updatedAt", "canReview", "arguments", "reason", "grant", "approvalMethod", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestor"]) -> MetaOapg.properties.requestor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'RequestStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timing"]) -> 'RequestTiming': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestedAt"]) -> MetaOapg.properties.requestedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessRule"]) -> 'AccessRule': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canReview"]) -> MetaOapg.properties.canReview: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arguments"]) -> MetaOapg.properties.arguments: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grant"]) -> typing.Union['Grant', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalMethod"]) -> typing.Union['ApprovalMethod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "requestor", "status", "timing", "requestedAt", "accessRule", "updatedAt", "canReview", "arguments", "reason", "grant", "approvalMethod", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        canReview: typing.Union[MetaOapg.properties.canReview, bool, ],
        requestedAt: typing.Union[MetaOapg.properties.requestedAt, str, ],
        timing: 'RequestTiming',
        arguments: typing.Union[MetaOapg.properties.arguments, dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        accessRule: 'AccessRule',
        requestor: typing.Union[MetaOapg.properties.requestor, str, ],
        status: 'RequestStatus',
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, ],
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        grant: typing.Union['Grant', schemas.Unset] = schemas.unset,
        approvalMethod: typing.Union['ApprovalMethod', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequestDetail':
        return super().__new__(
            cls,
            *_args,
            canReview=canReview,
            requestedAt=requestedAt,
            timing=timing,
            arguments=arguments,
            id=id,
            accessRule=accessRule,
            requestor=requestor,
            status=status,
            updatedAt=updatedAt,
            reason=reason,
            grant=grant,
            approvalMethod=approvalMethod,
            _configuration=_configuration,
            **kwargs,
        )

from jhc_cf_sdk_test.model.access_rule import AccessRule
from jhc_cf_sdk_test.model.approval_method import ApprovalMethod
from jhc_cf_sdk_test.model.grant import Grant
from jhc_cf_sdk_test.model.model_with import ModelWith
from jhc_cf_sdk_test.model.request_status import RequestStatus
from jhc_cf_sdk_test.model.request_timing import RequestTiming
