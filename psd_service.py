"""Adobe Photoshop Service"""

from os import listdir
import shutil
import win32com.client


class PsdService:
    """Implement Adobe Photoshop API"""

    SILENT_CLOSE = 2

    def __init__(self, sample="", destination=""):
        self.app = win32com.client.Dispatch("Photoshop.Application")
        self.sample = sample
        self.destination = destination

    def populate(self, file: str, sourse: str, flexible: bool) -> None:
        """Generate psd"""

        if not flexible:
            self.__populate_easy_mode(file, sourse)
        else:
            self.__populate_precise(file, sourse)

    def __copy_file_contents_to_clipboard(self, path, size=None):
        doc = self.app.Open(path)
        doc.Layers[0].Copy()

        ret = True
        if size is not None:
            actual_size = (doc.width, doc.height)
            ret = (size == actual_size, actual_size)

        doc.Close(self.SILENT_CLOSE)
        return ret

    def __create_layer_from_file(self, doc, layer, path):
        self.__copy_file_contents_to_clipboard(path)

        doc.ActiveLayer = layer
        doc.Paste()

    def __create_layer_or_new_doc_from_file(self, doc, layer, path, size):
        ok, size = self.__copy_file_contents_to_clipboard(path, size)
        if ok:
            doc.ActiveLayer = layer
            doc.Paste()
            return True
        else:
            img_name = "".join(path.name.split(".")[:-1])
            new_file = self.destination.parents[0] / (img_name + ".psd")

            shutil.copyfile(self.sample, new_file)
            doc = self.app.Open(new_file.resolve())

            doc.ResizeCanvas(size[0], size[1])
            doc.Layers[0].Name = img_name
            doc.ActiveLayer = doc.Layers[0].Layers[2]
            doc.Paste()

            doc.Save()
            doc.Close(self.SILENT_CLOSE)
            return False

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

    def __populate_precise(self, file: str, sourse: str):
        self.app.Open(file)
        doc = self.app.Application.ActiveDocument
        images = listdir(sourse)
        doc.ActiveLayer = doc.Layers[0]
        size = (doc.width, doc.height)

        for _ in range(1, len(images)):
            doc.ActiveLayer.Duplicate()

        for i, img in enumerate(images):
            layer = doc.Layers[i]
            imgname = "".join(img.split(".")[:-1])
            layer.Name = imgname

            layer.Layers[0].Name = "text"
            layer.Layers[1].Name = "clean"
            layer.Layers[2].Name = imgname

            layer.Visible = False
            if not self.__create_layer_or_new_doc_from_file(doc, layer.Layers[2], (sourse / img).resolve(), size):
                layer.Delete()

        doc.Layers[0].Visible = True
        self.app.ExecuteAction(self.app.StringIDToTypeID("collapseAllGroupsEvent"))

        doc.Save()
        doc.Close(self.SILENT_CLOSE)
