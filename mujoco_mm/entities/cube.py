from .body import Body


class Cube(Body):
    '''
    the Cube class inherits from the ~.entities.Body class

    Parameters
    ----------
    name : str
        a unique string identifier
    '''

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.type = 'box'

    def set_geometry(self, size: float, position: tuple[float, float, float] | None = None, orientation: tuple[float, float, float, float] | None = None, center_location: str | None = None):
        if type(size) is not float:
            raise TypeError(f'the size of a {__class__.__name__} instance must be a float. Received {type(size)}')

        real_size: tuple[float, float, float] = (size/2.0, size/2.0, size/2.0)

        if position is not None:
            position = (position[0], position[1], position[2]+size/2.0)

        return super().set_geometry(real_size, position, orientation, center_location)
