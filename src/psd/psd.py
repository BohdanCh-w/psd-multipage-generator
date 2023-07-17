"""Adobe Photoshop Service"""
import shutil
from pathlib import Path
import win32com.client
from typing import cast
from helpers import get_img_pathes, compact_str_list
from .service import ApplicationWrapper, Document, Layer, CloseCode
from .entities import Dimensions, PsdDocument


def new_photoshop_app() -> ApplicationWrapper:
    '''Opens Photoshop and returns its descriptor'''
    return cast(ApplicationWrapper, win32com.client.Dispatch("Photoshop.Application"))


class PsdService:
    '''Implement Adobe Photoshop API'''

    def __init__(self, app: ApplicationWrapper):
        self.app = app

    def generate_file(self, source: Path, destination: Path, sample: Path, precise: bool) -> None:
        '''Generate psd'''
        main_doc: PsdDocument = PsdDocument.new_from_sample(self.app, sample, destination)
        images = get_img_pathes(source)

        documents: dict[tuple[int, int], PsdDocument] = {}
        documents[main_doc.dimensions.dims] = main_doc

        for img in images:
            dims = self._copy_image(img)
            psd = documents[main_doc.dimensions.dims]

            if precise and dims != main_doc.dimensions:
                if dims.dims not in documents:
                    documents[dims.dims] = PsdDocument.new_from_sample(
                        self.app, sample,
                        destination.parent / f'{source.name}-({dims}).psd',
                        dims)
                psd = documents[dims.dims]

            self.app.Application.ActiveDocument = psd.doc
            layer = self._create_layer_from_clipboard(psd.doc, img.stem, psd.sample_layer)
            layer.Visible = False

        self._save_documents(documents, main_doc.dimensions, destination.stem)

    def _save_documents(self, docs: dict[tuple[int, int], PsdDocument], main_dim: Dimensions, save_name: str) -> None:
        for dim, psd in docs.items():
            self.app.Application.ActiveDocument = psd.doc
            self.app.ExecuteAction(self.app.StringIDToTypeID('collapseAllGroupsEvent'))

            psd.doc.ActiveLayer = psd.doc.Layers[0]
            psd.doc.Layers[0].Visible = True
            psd.sample_layer.Delete()
            layer_names = [layer.name for layer in psd.doc.Layers]

            self.app.ExecuteAction(self.app.StringIDToTypeID('collapseAllGroupsEvent'))
            psd.doc.Save()
            psd.doc.Close(cast(CloseCode, CloseCode.SILENT.value))

            if Dimensions(dim[0], dim[1]) == main_dim:
                continue

            shutil.move(psd.location, psd.location.parent / f'{save_name}-({compact_str_list(*layer_names)}).psd')

    def _create_layer_from_clipboard(self, doc: Document, name: str, sample: Layer) -> Layer:
        struct = self._get_shallow_struct(sample)
        new_layer = sample.Duplicate()
        new_layer.Name = name

        img_placeholder = None
        for i, layer in enumerate(new_layer.Layers):
            if struct[i] == 'img':
                img_placeholder = layer
                layer.Name = name
            else:
                layer.Name = struct[i]

        if img_placeholder is None:
            raise ValueError("no 'img' layer was found in sample group")

        doc.ActiveLayer = img_placeholder
        doc.Paste()

        return new_layer

    def _copy_image(self, path: Path) -> Dimensions:
        doc = self.app.Open(path)
        doc.Layers[0].Copy()
        dims = Dimensions(doc.width, doc.height)

        doc.Close(cast(CloseCode, CloseCode.SILENT.value))
        return dims

    @staticmethod
    def _get_shallow_struct(layer: Layer) -> list[str]:
        return [inner.Name for inner in layer.Layers]
