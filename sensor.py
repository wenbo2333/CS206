import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.values = numpy.zeros(1000)
        self.linkName = linkName

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save("data/sensorValues.npy", self.values)
