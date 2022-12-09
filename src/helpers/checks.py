'''checking helper functions'''


def validate(condition: bool, error: str, panic: bool=True) -> None:
    '''Validate condition'''
    if callable(condition):
        condition = condition()

    if condition:
        return True

    if panic:
        raise ValueError(f'Error: {error}')

    return False
