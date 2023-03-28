from mujoco_mm import MapMaker
from mujoco_mm.entities import Cube, Box, Capsule, Cylinder, Sphere, Mesh

from adam import Simulation
from adam.entities import AdamInfo


def main():
    directory_path: str = 'tests/assets/'
    filename: str = 'obstacles.xml'

    map_maker: MapMaker = MapMaker(directory_path+filename)

    # Cube 1
    cube_1: Cube = Cube('cube_1').set_geometry(size=0.5, position=(0.5, 0.0, 0.0)).set_dynamics(mass=1.0).set_appearance('#2f2f2f')

    # Cube 2
    cube_2: Cube = Cube('cube_2').set_geometry(size=0.5, position=(1.0, 0.0, 0.0)).set_dynamics(mass=1.0).set_appearance(color='#b64545', alpha=0.5)

    # Cube 3
    cube_3: Cube = Cube('cube_3').set_geometry(size=0.5, position=(1.0, 0.0, 0.5)).set_appearance('#c4c476')

    # Cube 4
    cube_4: Cube = Cube('cube_4').set_geometry(size=0.5, position=(0.5, 0.0, 0.5))

    # Box
    box: Box = Box('box').set_geometry(size=(0.2, 0.2, 0.5), position=(1.0, 0.0, 1.0)).set_appearance(color=(0.2, 0.2, 0.2), alpha=0.2)

    # Capsule
    capsule: Capsule = Capsule('capsule').set_geometry(size=(0.2, 0.5), position=(0.5, -0.5, 0.0))

    # Cylinder
    cylinder: Cylinder = Cylinder('cylinder').set_geometry(size=(0.2, 0.5), position=(1.0, -0.5, 0.0))

    # Sphere
    sphere: Sphere = Sphere('sphere').set_geometry(size=0.25, position=(0.5, -1.0, 0.0))

    # Desk
    desk: Mesh = Mesh('desk', 'mujoco_mm/assets/desk.stl')

    map_maker.add_bodies([cube_1, cube_2, cube_3, cube_4, box, capsule, cylinder, sphere, desk])
    map_maker.make()

    Simulation.export_scene(directory_path)
    map_maker.add_to(directory_path + 'scene.xml')

    sim: Simulation = Simulation()
    initial_data: AdamInfo = sim.load_scene('tests/assets/scene.xml')

    sim.extend_collisions({77: 'table'})

    for _ in range(1000):
        sim.step(initial_data.left_manipulator.configuration, initial_data.right_manipulator.configuration)
        sim.render()


if __name__ == '__main__':
    main()