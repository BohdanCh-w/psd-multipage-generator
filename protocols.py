# pylint: disable=missing-function-docstring,invalid-name,missing-class-docstring,missing-module-docstring
from typing import Protocol, Self
from enum import Enum
from pathlib import Path


class CloseCode(Enum):
    SILENT = 2

class Layer(Protocol):
    def Duplicate(self) -> Self:
        ...

    def Delete(self) -> None:
        ...

    def Copy(self) -> None:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Visible(self) -> bool:
        ...

    @property
    def Layers(self) -> list[Self]:
        ...

class Document(Protocol):
    @property
    def width(self) -> float:
        ...

    @property
    def height(self) -> float:
        ...

    @property
    def ActiveLayer(self) -> Layer:
        ...

    @property
    def Layers(self) -> list[Layer]:
        ...

    def ResizeCanvas(self, width: int, height: int) -> None:
        ...

    def Paste(self) -> None:
        ...

    def Save(self) -> None:
        ...

    def Close(self, code: CloseCode) -> None:
        ...

class Application(Protocol):
    @property
    def ActiveDocument(self) -> Document:
        ...

class TypeID:
    ...

class ApplicationWrapper(Protocol):
    def Open(self, filename: str | Path) -> Document:
        ...

    @property
    def Application(self) -> Application:
        ...

    def ExecuteAction(self, type_id: TypeID) -> None:
        ...

    def StringIDToTypeID(self, string_id: str) -> TypeID:
        ...
    