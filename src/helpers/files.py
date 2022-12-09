'''files helper functions'''
from pathlib import Path


image_formats = ('png', 'jpg', 'jpeg')

def get_img_pathes(dir: Path) -> list[Path]:
    '''Returns sorted list of images inside directory'''
    def is_image(file: Path):
        return file.suffix.lstrip('.') in image_formats

    return list(filter(lambda x: is_image(x) and not x.is_dir(), dir.glob('*')))
