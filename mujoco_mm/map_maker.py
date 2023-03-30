from .entities import Body
from .use_cases import ElementManager


class MapMaker:
    '''
    the MapMaker class contains all the methods to create a map on top of a given scene

    Methods
    -------
    add_bodies:
        add the designed bodies to the map

    make:
        exports the map to an .xml file
    '''

    def __init__(self) -> None:
        # Attributes
        self.body_names: list[str] = []

        # Helpers
        self.element_manager: ElementManager = ElementManager()

    def add_bodies(self, bodies: list[Body]) -> None:
        '''
        add the designed bodies to the map

        Parameters
        ----------
        bodies : list[~.entities.Body]
            the list of bodies to include to the map
        '''
        for body in bodies:
            if body.type != 'mesh' and not body.size:
                raise ValueError(f'the body with id {body.name} must have a size')

            if body.name in self.body_names:
                raise ValueError(f'the bodies must have unique names. Name "{body.name}" is repeated')

            self.body_names.append(body.name)
            self.element_manager.append_body(body)

    def make(self, filename: str) -> None:
        '''
        exports the map to an .xml file

        Notes
        -----
        The name of the file is specified at instancing the class
        '''
        name: str = filename.split('/')[-1].split('.')[0]
        file_content: str = self.element_manager.wrap(name)

        with open(filename, 'w') as file:
            file.write(file_content)
