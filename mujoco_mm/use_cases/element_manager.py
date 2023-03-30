import pkg_resources

from .xml_parser import XMLParser
from ..entities import Body
from ..core import utils


class ElementManager:
    def __init__(self) -> None:
        self.bodies: list[str] = []
        self.meshes: list[str] = []

    def append_body(self, body: Body) -> None:
        self.append_mesh_element(body)
        self.append_body_element(body)

    def append_mesh_element(self, body: Body) -> None:
        if body.type != 'mesh':
            return

        # Asset element
        mesh_attr: str = XMLParser.create_attribute('name', body.name)
        mesh_file: str = body.mesh_file if body.mesh_file.endswith('.stl') else pkg_resources.resource_filename('mujoco_mm', 'assets/' + body.mesh_file + '.stl')  # type: ignore

        file_attr: str = XMLParser.create_attribute('file', mesh_file)

        mesh_element: str = XMLParser.create_element('mesh', [mesh_attr, file_attr], None)

        self.meshes.append(mesh_element)

    def append_body_element(self, body: Body) -> None:
        # Geom
        # - Mandatory attributes
        type_attr: str = XMLParser.create_attribute('type', body.type)
        color_attr: str = XMLParser.create_attribute('rgba', (*body.color, body.alpha) if type(body.color) is tuple else utils.hex_to_rgba(body.color, body.alpha))  # type: ignore

        # - Optional attributes
        size_attr: str | None = XMLParser.create_attribute('size', body.size) if body.type != 'mesh' else None
        mesh_attr: str | None = XMLParser.create_attribute('mesh', body.name) if body.type == 'mesh' else None

        geom_attributes = [type_attr, mesh_attr, color_attr, size_attr]
        geom_attributes = [attribute for attribute in geom_attributes if attribute is not None]

        geom_element: str = XMLParser.create_element('geom', geom_attributes, None)

        # Inertial
        inertial_element: str | None = None
        joint_element: str | None = None
        if body.mass:
            # Inertial
            inertia_pos_attr: str = XMLParser.create_attribute('pos', body.center_of_mass)
            mass_attr: str = XMLParser.create_attribute('mass', body.mass)
            diaginertia_attr: str = XMLParser.create_attribute('diaginertia', (0.001, 0.001, 0.001))

            inertial_element = XMLParser.create_element('inertial', [mass_attr, inertia_pos_attr, diaginertia_attr], None)

            # Joint
            name_attr: str = XMLParser.create_attribute('name', body.name + '_freejoint')
            joint_element = XMLParser.create_element('freejoint', [name_attr], None)

        # Body
        name_attr: str = XMLParser.create_attribute('name', body.name)
        position_attr: str = XMLParser.create_attribute('pos', body.position)
        orientation_attr: str = XMLParser.create_attribute('quat', body.orientation if len(body.orientation) == 4 else utils.euler_to_quaternion(*body.orientation))

        elements_list = [geom_element, joint_element, inertial_element]
        elements_list = [element for element in elements_list if element is not None]

        body_element: str = XMLParser.create_element('body', [name_attr, position_attr, orientation_attr], elements_list)

        self.bodies.append(body_element)

    def wrap(self, name: str) -> str:
        # Wrap bodies
        worldbody_element: str = XMLParser.create_element('worldbody', None, self.bodies)

        # Wrap assets
        assets_element: str = XMLParser.create_element('asset', None, self.meshes)

        # Wrap in general
        model_attr: str = XMLParser.create_attribute('model', name)
        content: str = XMLParser.create_element('mujoco', [model_attr], [assets_element, worldbody_element])

        return content
