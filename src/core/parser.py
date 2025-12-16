from typing import Generic, Protocol, TypeVar

from src.core.representation import Either

__all__ = ["Parser"]

OutputType = TypeVar("OutputType")


class Parser(Protocol, Generic[OutputType]):
    def parse(self, input: str) -> Either[OutputType]: ...
