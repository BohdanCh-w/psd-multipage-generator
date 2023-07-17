'''Photoshop Document COMobject'''
from typing import Protocol
from .layer import Layer
from .close_code import CloseCode


class Document(Protocol):
    '''Photoshop Document'''
    width: float
    height: float
    ActiveLayer: Layer
    Layers: list[Layer]

    def ResizeCanvas(self, width: int, height: int) -> None:
        '''Change document width and height'''
        ...

    def Paste(self) -> None:
        '''Paste clipboard content into ActiveLayer'''
        ...

    def Save(self) -> None:
        '''Save current document to default location'''
        ...

    def Close(self, code: CloseCode) -> None:
        '''Close document with given code'''
        ...
