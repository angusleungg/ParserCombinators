from dataclasses import dataclass
from typing import Generic, TypeVar

__all__ = ["Either", "Success", "Error"]

L = TypeVar("L")


@dataclass(frozen=True, slots=True)
class Success(Generic[L]):
    __match_args__ = ("value", "remaining")
    value: L
    remaining: str


@dataclass(frozen=True, slots=True)
class Error:
    __match_args__ = ("message",)
    message: str


Either = Success[L] | Error
