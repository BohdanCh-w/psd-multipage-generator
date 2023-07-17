'''Photoshop Layer COMobject'''
from typing import Protocol, Self


class Layer(Protocol):
    '''Photoshop layer'''
    Name: str
    name: str
    Visible: bool
    Layers: list[Self]

    def Duplicate(self) -> Self:
        '''Duplicate layer and return new'''
        ...

    def Delete(self) -> None:
        '''Delete current layer'''
        ...

    def Copy(self) -> None:
        '''Copy content of current layer to clipboard'''
        ...
