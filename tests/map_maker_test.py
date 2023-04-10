import numpy as np
import mujoco
from mujoco_viewer import MujocoViewer

from mujoco_mm import MapMaker
from mujoco_mm.entities import Cube, Box, Capsule, Cylinder, Sphere, Mesh


def main():
    map_1: MapMaker = MapMaker()

    # Objects
    # desk: Mesh = Mesh('desk', 'desk').set_geometry(position=(1.0, 0.0, 0.0), orientation=(0.0, 0.0, -np.pi/2)).set_appearance(color='#9F8170')
    box: Box = Box('box').set_geometry(size=(0.3, 0.3, 0.1), position=(1.0, 0.0, 1.0)).set_dynamics(mass=1.0)

    # box_1: Box = Box('box_1').set_geometry(size=(0.6, 1.5, 0.1), position=(0.0, 0.0, 1.5))

    map_1.add_bodies([box])
    map_1.make('tests/assets/obstacles.xml')

    # MuJoCo
    model = mujoco.MjModel.from_xml_path('tests/assets/scene.xml')  # type: ignore
    data = mujoco.MjData(model)  # type: ignore

    viewer: MujocoViewer = MujocoViewer(model, data)
    viewer.cam.lookat = (0.0, 0.0, 0.5)
    viewer.cam.azimuth = -135.0
    viewer.cam.elevation = -20.0
    viewer.cam.distance = 3.5

    for _ in range(1000):
        mujoco.mj_step(model, data)  # type: ignore
        viewer.render()


if __name__ == '__main__':
    main()
