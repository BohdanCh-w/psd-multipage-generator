'''Helper functions'''
from pathlib import Path


image_formats = ('png', 'jpg', 'jpeg')

def get_img_pathes(dir: Path) -> list[Path]:
    '''Returns sorted list of images inside directory'''
    def is_image(file: Path):
        return file.suffix.lstrip('.') in image_formats

    return list(filter(lambda x: is_image(x) and not x.is_dir(), dir.glob('*')))

def validate(condition: bool, error: str, panic: bool=True) -> None:
    '''Validate condition'''
    if callable(condition):
        condition = condition()

    if condition:
        return True

    if panic:
        raise ValueError(f'Error: {error}')

    return False
