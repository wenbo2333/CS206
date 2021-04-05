from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time


class SIMULATION:
    def __init__(self, directOrGui):
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGui == "GUI":
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()


    def RUN(self):
        for i in range(300):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1/60)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
