from .body import Body


class Mesh(Body):
    '''
    the Mesh class inherits from the ~.entities.Body class and load a mesh from a file

    Parameters
    ----------
    filename : str
        the path to the mesh file

    name : str
        a unique string identifier
    '''

    def __init__(self, name: str, mesh_file: str) -> None:
        super().__init__()
        self.name = name
        self.type = 'mesh'
        self.mesh_file = mesh_file

    def set_geometry(self, position: tuple[float, float, float] | None = None, orientation: tuple[float, float, float, float] | tuple[float, float, float] | None = None, center_location: str | None = None):
        size: int = 0
        return super().set_geometry(size, position, orientation, center_location)
