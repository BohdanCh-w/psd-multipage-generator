'''Dimensions of the document'''


class Dimensions:
    '''Represents document dimensions'''

    def __init__(self, width: float, height: float) -> None:
        self.width = round(width)
        self.height = round(height)

    @property
    def dims(self) -> tuple[int, int]:
        '''tuple of dimensions'''
        return (self.width, self.height)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dimensions):
            return NotImplemented

        return self.width == other.width and self.height == other.height

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Dimensions):
            return NotImplemented

        return self.width != other.width or self.height != other.height

    def __str__(self) -> str:
        return f'{self.width}x{self.height}'

    def __repr__(self) -> str:
        return f'<Dimensions:{self.width}x{self.height}>'
