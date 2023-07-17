'''checking helper functions'''


from typing import Callable


def validate(condition: bool | Callable[[], bool], error: str, panic: bool = True) -> bool:
    '''Validate condition'''
    if callable(condition):
        condition = condition()

    if condition:
        return True

    if panic:
        raise ValueError(f'Error: {error}')

    return False
