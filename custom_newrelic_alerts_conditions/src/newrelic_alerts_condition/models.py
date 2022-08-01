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
    Condition: Optional["_Condition"]

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
            Condition=Condition._deserialize(json_data.get("Condition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Condition(BaseModel):
    Id: Optional[int]
    PolicyId: Optional[int]
    Enabled: Optional[bool]
    Name: Optional[str]
    Type: Optional[str]
    BaselineDirection: Optional[str]
    Nrql: Optional["_Nrql"]
    RunbookUrl: Optional[str]
    Description: Optional[str]
    Terms: Optional[Sequence["_Term"]]
    Signal: Optional["_Signal"]
    Expiration: Optional["_Expiration"]
    ViolationTimeLimitSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            PolicyId=json_data.get("PolicyId"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            BaselineDirection=json_data.get("BaselineDirection"),
            Nrql=Nrql._deserialize(json_data.get("Nrql")),
            RunbookUrl=json_data.get("RunbookUrl"),
            Description=json_data.get("Description"),
            Terms=deserialize_list(json_data.get("Terms"), Term),
            Signal=Signal._deserialize(json_data.get("Signal")),
            Expiration=Expiration._deserialize(json_data.get("Expiration")),
            ViolationTimeLimitSeconds=json_data.get("ViolationTimeLimitSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class Nrql(BaseModel):
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nrql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nrql"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nrql = Nrql


@dataclass
class Term(BaseModel):
    Operator: Optional[str]
    Priority: Optional[str]
    Threshold: Optional[float]
    ThresholdDuration: Optional[int]
    ThresholdOccurrences: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Term"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Term"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Priority=json_data.get("Priority"),
            Threshold=json_data.get("Threshold"),
            ThresholdDuration=json_data.get("ThresholdDuration"),
            ThresholdOccurrences=json_data.get("ThresholdOccurrences"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Term = Term


@dataclass
class Signal(BaseModel):
    AggregationDelay: Optional[int]
    AggregationMethod: Optional[str]
    AggregationTimer: Optional[int]
    AggregationWindow: Optional[int]
    FillOption: Optional[str]
    FillValue: Optional[int]
    SlideBy: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Signal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Signal"]:
        if not json_data:
            return None
        return cls(
            AggregationDelay=json_data.get("AggregationDelay"),
            AggregationMethod=json_data.get("AggregationMethod"),
            AggregationTimer=json_data.get("AggregationTimer"),
            AggregationWindow=json_data.get("AggregationWindow"),
            FillOption=json_data.get("FillOption"),
            FillValue=json_data.get("FillValue"),
            SlideBy=json_data.get("SlideBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Signal = Signal


@dataclass
class Expiration(BaseModel):
    CloseViolationsOnExpiration: Optional[bool]
    ExpirationDuration: Optional[int]
    OpenViolationsOnExpiration: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Expiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Expiration"]:
        if not json_data:
            return None
        return cls(
            CloseViolationsOnExpiration=json_data.get("CloseViolationsOnExpiration"),
            ExpirationDuration=json_data.get("ExpirationDuration"),
            OpenViolationsOnExpiration=json_data.get("OpenViolationsOnExpiration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Expiration = Expiration


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


