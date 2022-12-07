'''Photoshop document wrapper'''
import shutil
from pathlib import Path
from typing import Self
from ..service import ApplicationWrapper, Document, Layer
from .dimensions import Dimensions

class PsdDocument:
    '''extened document class'''
    doc: Document
    sample_layer: Layer
    location: Path
    dimensions: Dimensions

    def __init__(self, doc: Document, sample_layer: Layer = None, location: Path = None):
        self.doc = doc
        self.sample_layer = sample_layer
        self.location = location
        self.dimensions = Dimensions(doc.width, doc.height)

    @staticmethod
    def new_from_sample(app: ApplicationWrapper, sample: Path, destination: Path, dimensions: Dimensions=None) -> Self:
        '''create new document'''
        shutil.copyfile(sample, destination)

        app.Open(str(destination))
        doc = app.Application.ActiveDocument
        doc.ActiveLayer = doc.Layers[0]

        if dimensions is not None:
            doc.ResizeCanvas(dimensions.width, dimensions.height)

        return PsdDocument(doc, doc.ActiveLayer, destination)
