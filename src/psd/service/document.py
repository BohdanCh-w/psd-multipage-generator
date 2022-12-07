'''Photoshop Document COMobject'''
from typing import Protocol
from .layer import Layer
from .close_code import CloseCode


class Document(Protocol):
    '''Photoshop Document'''
    @property
    def width(self) -> float:
        '''Width of document'''
        ...

    @property
    def height(self) -> float:
        '''Height of document'''
        ...

    @property
    def ActiveLayer(self) -> Layer:
        '''Current active Layer'''
        ...

    @property
    def Layers(self) -> list[Layer]:
        '''List of top level Layers'''
        ...

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
