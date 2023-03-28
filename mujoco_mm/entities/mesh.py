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
