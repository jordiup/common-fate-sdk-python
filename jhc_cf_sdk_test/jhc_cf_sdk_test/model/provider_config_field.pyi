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


class ProviderConfigField(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "isSecret",
            "name",
            "description",
            "id",
            "isOptional",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            description = schemas.StrSchema
            isOptional = schemas.BoolSchema
            isSecret = schemas.BoolSchema
            secretPath = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "description": description,
                "isOptional": isOptional,
                "isSecret": isSecret,
                "secretPath": secretPath,
            }
    
    isSecret: MetaOapg.properties.isSecret
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    isOptional: MetaOapg.properties.isOptional
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isOptional"]) -> MetaOapg.properties.isOptional: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSecret"]) -> MetaOapg.properties.isSecret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secretPath"]) -> MetaOapg.properties.secretPath: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "description", "isOptional", "isSecret", "secretPath", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isOptional"]) -> MetaOapg.properties.isOptional: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSecret"]) -> MetaOapg.properties.isSecret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secretPath"]) -> typing.Union[MetaOapg.properties.secretPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "description", "isOptional", "isSecret", "secretPath", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        isSecret: typing.Union[MetaOapg.properties.isSecret, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        isOptional: typing.Union[MetaOapg.properties.isOptional, bool, ],
        secretPath: typing.Union[MetaOapg.properties.secretPath, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProviderConfigField':
        return super().__new__(
            cls,
            *_args,
            isSecret=isSecret,
            name=name,
            description=description,
            id=id,
            isOptional=isOptional,
            secretPath=secretPath,
            _configuration=_configuration,
            **kwargs,
        )
