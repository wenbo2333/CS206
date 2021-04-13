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
		# create an empty dictionary TO STORE SENSORS
		self.sensors = {}
		# gives us the name of every link in body.urdf
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		# get all the sensors and fill them w/ sensor values
		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(t)

	def Prepare_To_Act(self):
		# create an empty dictionary TO STORE MOTORS
		self.motors = dict()

		# gives us the name of every joint in body.urdf (attaching a motor to every joint)
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def	Act(self, t):
		# We are now going to discard motorValues and use values from the motor neurons instead.
		# iterate over all the neurons in the neural network
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				# extract the name of the joint to which this motor neuron connects
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				# extract the value of this motor neuron, as the desired angle for this joint
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				# pass desired angle to the appropriate motor
				self.motors[jointName].Set_Value(self, desiredAngle*c.motorJointRange)
				# print(neuronName + " " + jointName + " ", desiredAngle)

	def	Think(self):
		# flowing values from the sensors to the sensor neurons
		self.nn.Update()
		# UNCOMMENT THIS!!!!!!!!!!!!!!!!!
		# self.nn.Print()

	def Get_Fitness(self, solutionID):
		stateOfLinkZero = p.getLinkState(self.robot,0)
		positionOfLinkZero = stateOfLinkZero[0]
		xCoordinateOfLinkZero = positionOfLinkZero[0]
		# file = "fitness"+str(solutionID)+".txt"
		file = "tmp"+str(solutionID)+".txt"
		f = open(file, "w")
		f.write(str(xCoordinateOfLinkZero))
		f.close()
		os.system("mv " + file + " " + "fitness"+str(solutionID)+".txt")