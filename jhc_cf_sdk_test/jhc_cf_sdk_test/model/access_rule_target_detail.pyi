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


class AccessRuleTargetDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A detailed target for an access rule
    """


    class MetaOapg:
        required = {
            "with",
            "provider",
        }
        
        class properties:
        
            @staticmethod
            def provider() -> typing.Type['Provider']:
                return Provider
            
            
            class _with(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['AccessRuleTargetDetailArguments']:
                        return AccessRuleTargetDetailArguments
                
                def __getitem__(self, name: typing.Union[str, ]) -> 'AccessRuleTargetDetailArguments':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> 'AccessRuleTargetDetailArguments':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'AccessRuleTargetDetailArguments',
                ) -> '_with':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "provider": provider,
                "with": _with,
            }
    
    provider: 'Provider'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> 'Provider': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["with"]) -> MetaOapg.properties._with: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["provider", "with", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> 'Provider': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["with"]) -> MetaOapg.properties._with: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["provider", "with", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        provider: 'Provider',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessRuleTargetDetail':
        return super().__new__(
            cls,
            *_args,
            provider=provider,
            _configuration=_configuration,
            **kwargs,
        )

from jhc_cf_sdk_test.model.access_rule_target_detail_arguments import AccessRuleTargetDetailArguments
from jhc_cf_sdk_test.model.provider import Provider
