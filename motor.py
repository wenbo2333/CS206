import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p
import os
class MOTOR:
	# defines a constructor for this class
	def __init__(self, jointName):
		self.jointName = jointName

	def	Set_Value(self, robot, desiredAngle):
		# Making motor go
		pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = c.maxForce)
