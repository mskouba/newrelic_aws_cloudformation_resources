# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]
    typeConfiguration: Optional["TypeConfigurationModel"]


@dataclass
class ResourceModel(BaseModel):
    AccountId: Optional[int]
    ApiKey: Optional[str]
    NotificationChannel: Optional["_NotificationChannel"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccountId=json_data.get("AccountId"),
            ApiKey=json_data.get("ApiKey"),
            NotificationChannel=NotificationChannel._deserialize(json_data.get("NotificationChannel")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NotificationChannel(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Id: Optional[int]
    Config: Optional["_Config"]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationChannel"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Id=json_data.get("Id"),
            Config=Config._deserialize(json_data.get("Config")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationChannel = NotificationChannel


@dataclass
class Config(BaseModel):
    Emails: Optional[Sequence[str]]
    IncludeJson: Optional[bool]
    ApiKey: Optional[str]
    DataCenterRegion: Optional[str]
    Recipients: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    Teams: Optional[Sequence[str]]
    TeamChannel: Optional[str]
    Url: Optional[str]
    Key: Optional[str]
    RouteKey: Optional[str]
    BaseUrl: Optional[str]
    BasicAuth: Optional["_BasicAuth"]
    CustomHttpHeaders: Optional[Sequence["_CustomHttpHeaders"]]
    CustomPayloadBody: Optional[str]
    CustomPayloadType: Optional[str]
    IntegrationUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            Emails=json_data.get("Emails"),
            IncludeJson=json_data.get("IncludeJson"),
            ApiKey=json_data.get("ApiKey"),
            DataCenterRegion=json_data.get("DataCenterRegion"),
            Recipients=json_data.get("Recipients"),
            Tags=json_data.get("Tags"),
            Teams=json_data.get("Teams"),
            TeamChannel=json_data.get("TeamChannel"),
            Url=json_data.get("Url"),
            Key=json_data.get("Key"),
            RouteKey=json_data.get("RouteKey"),
            BaseUrl=json_data.get("BaseUrl"),
            BasicAuth=BasicAuth._deserialize(json_data.get("BasicAuth")),
            CustomHttpHeaders=deserialize_list(json_data.get("CustomHttpHeaders"), CustomHttpHeaders),
            CustomPayloadBody=json_data.get("CustomPayloadBody"),
            CustomPayloadType=json_data.get("CustomPayloadType"),
            IntegrationUrl=json_data.get("IntegrationUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class BasicAuth(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAuth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAuth"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAuth = BasicAuth


@dataclass
class CustomHttpHeaders(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHttpHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHttpHeaders"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHttpHeaders = CustomHttpHeaders


@dataclass
class TypeConfigurationModel(BaseModel):

    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls(
        )


# work around possible type aliasing issues when variable has same name as a model
_TypeConfigurationModel = TypeConfigurationModel


