'''Photoshop Layer COMobject'''
from typing import Protocol, Self


class Layer(Protocol):
    '''Photoshop layer'''
    def Duplicate(self) -> Self:
        '''Duplicate layer and return new'''
        ...

    def Delete(self) -> None:
        '''Delete current layer'''
        ...

    def Copy(self) -> None:
        '''Copy content of current layer to clipboard'''
        ...

    @property
    def Name(self) -> str:
        '''Layer name'''
        ...

    @property
    def Visible(self) -> bool:
        '''Whether layer is visible'''
        ...

    @property
    def Layers(self) -> list[Self]:
        '''List of inner layers'''
        ...
