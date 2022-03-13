"""Adobe Photoshop Service"""

from os import listdir
from photoshop import Session


class PsdService:
    """Implement Adobe Photoshop API"""

    def __init__(self):
        pass

    def populate(self, file: str, sourse: str, flexible: bool) -> None:
        """Generate psd"""

        if not flexible:
            self.__populate_easy_mode(file, sourse)
        else:
            self.__populate_precise(file, sourse)

    def __populate_easy_mode(self, file: str, sourse: str):
        images = listdir(sourse)

        with Session(file, action="open") as psd:
            doc = psd.active_document
            for i in range(0, len(images)):
                doc.layers[0].duplicate()

            for i, img in enumerate(images):
                doc.layers[i].name = ''.join(img.split('.')[:-1])
                for obj in doc.layers[i].layers:
                    obj.name = ' '.join(obj.name.split(' ')[:-1])

            doc.saveAs(file, psd.PhotoshopSaveOptions(), True)
            doc.close()

    def __populate_precise(self, file: str, sourse: str):
        raise NotImplementedError
