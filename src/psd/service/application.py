'''Photoshop Application COMobject'''
from typing import Protocol
from pathlib import Path
from .document import Document


class Application(Protocol):
    '''Photoshop application'''
    @property
    def ActiveDocument(self) -> Document:
        '''Active Document'''
        ...

class TypeID:
    '''Command code'''
    ...

class ApplicationWrapper(Protocol):
    '''COM application object'''
    def Open(self, filename: str | Path) -> Document:
        '''Ppen new psd document'''
        ...

    @property
    def Application(self) -> Application:
        '''Inner application object'''
        ...

    def ExecuteAction(self, type_id: TypeID) -> None:
        '''Execute command by code'''
        ...

    def StringIDToTypeID(self, string_id: str) -> TypeID:
        '''Convert string code to inner code type'''
        ...
    