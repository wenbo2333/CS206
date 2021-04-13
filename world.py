import pybullet as p
import pybullet_data

class WORLD:
    def __init__(self):
        self.planeID = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
