"""Adobe Photoshop Service"""

from os import listdir
import win32com.client
from photoshop import Session


class PsdService:
    """Implement Adobe Photoshop API"""

    SILENT_CLOSE = 2

    def __init__(self):
        self.app = win32com.client.Dispatch("Photoshop.Application")

    def populate(self, file: str, sourse: str, flexible: bool) -> None:
        """Generate psd"""

        if not flexible:
            self.__populate_easy_mode(file, sourse)
        else:
            self.__populate_precise(file, sourse)

    def __copy_file_contents_to_clipboard(self, path):
        doc = self.app.Open(path)
        doc.Layers[0].Copy()
        doc.Close(self.SILENT_CLOSE)

    def __create_layer_from_file(self, doc, layer, path):
        self.__copy_file_contents_to_clipboard(path)

        doc.ActiveLayer = layer
        doc.Paste()

    def __populate_easy_mode(self, file: str, sourse: str):
        self.app.Open(file)
        doc = self.app.Application.ActiveDocument
        images = listdir(sourse)
        doc.ActiveLayer = doc.Layers[0]

        for _ in range(1, len(images)):
            doc.ActiveLayer.Duplicate()

        for i, img in enumerate(images):
            layer = doc.Layers[i]
            imgname = "".join(img.split(".")[:-1])
            layer.Name = imgname

            layer.Layers[0].Name = "text"
            layer.Layers[1].Name = "clean"
            layer.Layers[2].Name = imgname

            self.__create_layer_from_file(doc, layer.Layers[2], (sourse / img).resolve())
            layer.Visible = False

        doc.Layers[0].Visible = True
        self.app.ExecuteAction(self.app.StringIDToTypeID("collapseAllGroupsEvent"))

        doc.Save()
        doc.Close(self.SILENT_CLOSE)

    def __generate_layers(self, file: str, sourse: str):
        images = listdir(sourse)

        with Session(file, action="open") as psd:
            doc = psd.active_document
            for i in range(0, len(images)):
                doc.layers[0].duplicate()

            for i, img in enumerate(images):
                doc.layers[i].name = "".join(img.split(".")[:-1])
                for obj in doc.layers[i].layers:
                    obj.name = " ".join(obj.name.split(" ")[:-1])

            doc.saveAs(file, psd.PhotoshopSaveOptions(), True)
            doc.close()

    def __populate_precise(self, file: str, sourse: str):
        raise NotImplementedError
