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


class AccessRule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Access Rule contains information for an end user to make a request for access.
    """


    class MetaOapg:
        required = {
            "timeConstraints",
            "isCurrent",
            "name",
            "description",
            "id",
            "version",
            "target",
        }
        
        class properties:
            id = schemas.StrSchema
            version = schemas.StrSchema
            name = schemas.StrSchema
            description = schemas.StrSchema
        
            @staticmethod
            def target() -> typing.Type['AccessRuleTarget']:
                return AccessRuleTarget
        
            @staticmethod
            def timeConstraints() -> typing.Type['TimeConstraints']:
                return TimeConstraints
            isCurrent = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "version": version,
                "name": name,
                "description": description,
                "target": target,
                "timeConstraints": timeConstraints,
                "isCurrent": isCurrent,
            }
    
    timeConstraints: 'TimeConstraints'
    isCurrent: MetaOapg.properties.isCurrent
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    version: MetaOapg.properties.version
    target: 'AccessRuleTarget'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> 'AccessRuleTarget': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeConstraints"]) -> 'TimeConstraints': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isCurrent"]) -> MetaOapg.properties.isCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "version", "name", "description", "target", "timeConstraints", "isCurrent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> 'AccessRuleTarget': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeConstraints"]) -> 'TimeConstraints': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isCurrent"]) -> MetaOapg.properties.isCurrent: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "version", "name", "description", "target", "timeConstraints", "isCurrent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timeConstraints: 'TimeConstraints',
        isCurrent: typing.Union[MetaOapg.properties.isCurrent, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        target: 'AccessRuleTarget',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessRule':
        return super().__new__(
            cls,
            *_args,
            timeConstraints=timeConstraints,
            isCurrent=isCurrent,
            name=name,
            description=description,
            id=id,
            version=version,
            target=target,
            _configuration=_configuration,
            **kwargs,
        )

from jhc_cf_sdk_test.model.access_rule_target import AccessRuleTarget
from jhc_cf_sdk_test.model.time_constraints import TimeConstraints
