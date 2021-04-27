import pyrosim.pyrosim as pyrosim
import random

def Create_World():
	# Tell pyrosim where to store information about the world you'd like to create. 
	# Assignment 5, need a world.sdf
	# pyrosim.Start_SDF("world.sdf")
	# This world will currently be called box, because it will only contain a box (links can be spheres, cylinders, or boxes).
	pyrosim.Start_SDF("boxes.sdf")
	
	# Stores a box with initial position x=0, y=0, z=0.5, 
	# and length, width and height all equal to 1 meter, in box.sdf.
	length, width, height = 10, 4, 1
    x, y, z = 0,0,1
	pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
		
	# Finish generate.py by appending
	pyrosim.End()

def Generate_Body():
	# description of the robot's body in this urdf file
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "2.0 0.0 1.0")
	pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1, 1, 1])
	pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1, 1, 1])
	pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso" , child = "BackLeg" , type = "revolute", position = "1.0 0.0 1.0")
	pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1, 1, 1])
	pyrosim.End()

def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	# This particular neuron is going to receive a value from sensor stored in Torso
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
	# send two additional neurons to brain.nndf
	pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
	# Motor neurons - send values to the motor controlling joint Torso_BackLeg & Torso_FrontLeg
	pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
	pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
	# Generating a synapse - Connects neuron 0 to neuron 3 with a synaptic with weight 1.0
	# pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
	# # Connects sensor neuron 1 to motor neuron 3, 1 -> 3
	# pyrosim.Send_Synapse(sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.5 )
	# # Connects sensor neuron 0 to motor neuron 4
	# pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.5 )
	# # Connects sensor neuron 2 to motor neuron 4
	# pyrosim.Send_Synapse(sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )



	# Outer loop  iterate over the names of the three sensor neurons
	for i in range(3):
		# Inner loop  iterate over each of the two motor neurons
		for j in range(2):
			j = j + 3	# start at 3
			# generate a synapse that connects the ith sensor neuron to the jth motor neuron. 
			# send random synaptic weights in the range [-1,1
			pyrosim.Send_Synapse(sourceNeuronName = i , targetNeuronName = j , weight = random.uniform(-1, 1) )

	pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()