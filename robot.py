import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
class ROBOT:
	# defines a constructor for this class
	def __init__(self, solutionID):
		# load and prepare to simulate body.urdf
		self.robot = p.loadURDF("body.urdf")
		# Pyrosim has to do some additional setting up when it is used to simulate sensors
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		nndfFile = "brain" + str(solutionID) + ".nndf"
		self.nn = NEURAL_NETWORK(nndfFile)
		os.system("rm " + nndfFile)

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(t)

	def Prepare_To_Act(self):
		self.motors = dict()
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self, t):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[jointName].Set_Value(self, desiredAngle*c.motorJointRange)

	def Think(self):
		self.nn.Update()

	def Get_Fitness(self, solutionID):
		basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
		basePosition = basePositionAndOrientation[0]
		zPosition = basePosition[2]

		file = "tmp"+str(solutionID)+".txt"
		f = open(file, "w")
		f.write(str(zPosition))
		f.close()
		os.system("mv " + file + " " + "fitness"+str(solutionID)+".txt")
