from world import WORLD
from robot import ROBOT
import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
import os
import time
import pybullet_data
class SIMULATION:
	# defines a constructor for this class
	def __init__(self, directOrGUI, solutionID):
		self.directOrGUI = directOrGUI
		self.id = solutionID
		# Connected to pybullet
		# Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
		if (directOrGUI == 'DIRECT'):
			self.physicsClient = p.connect(p.DIRECT)
		else:
			self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())

		self.world = WORLD()
		self.robot = ROBOT(solutionID)

		# add gravity 
		p.setGravity(0,0, c.gravity)

	def Run(self):
		#For loop that iterates 1000 times
		for i in range(c.numLoops):
			# time.sleep(1/60)
			# Only time.sleep() if simulation is running to the screen
			if (self.directOrGUI == 'GUI'):
				time.sleep(1/900)
			p.stepSimulation()
			self.robot.Sense(i)
			self.robot.Think()
			self.robot.Act(i)

	def Get_Fitness(self):
		self.robot.Get_Fitness(self.id)

	# defines a destructor for this class   
	def __del__(self):
		p.disconnect()