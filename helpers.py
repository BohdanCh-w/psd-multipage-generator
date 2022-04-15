'''Helper functions'''
from os import listdir
from os.path import join, isdir


image_formats = ('png', 'jpg', 'jpeg')


def get_images(dir: str) -> list[str]:
    '''Get sorted list of images in directory'''
    def is_image(file):
        return file.split('.')[-1] in image_formats

    def is_file(file):
        return not isdir(join(dir, file))

    return list(filter(lambda x: is_image(x) and is_file(x), listdir(dir)))


def compare_size(size1: tuple[float], size2: tuple[float]) -> bool:
    '''Compare floats converted to ints'''
    size1 = tuple(map(round, size1))
    size2 = tuple(map(round, size2))
    return size1 == size2

def validate(condition: bool, error: str, panic: bool=True) -> None:
    '''Validate condition'''
    if callable(condition):
        condition = condition()

    if condition:
        return True

    if panic:
        raise ValueError(f'Error: {error}')

    return False
