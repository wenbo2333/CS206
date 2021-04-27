import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import time
import constants as c
class SOLUTION:
    # defines a constructor for this class
    def __init__(self, id):
        self.myID = id
        # numSensorNeurons x numMotorNeurons matrix of random values/weights in a certain range
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
    
    def Start_Simulation(self, directOrGUI): 
        self.Create_World()
        self.Create_Body()
        self.Generate_Brain()
        strId = str(self.myID)
        os.system("python3 simulate.py " + directOrGUI + " " + strId + " 2&>1 &")

    def Wait_For_Simulation_To_End(self): 
        fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        os.system("rm " + fitnessFileName)

    def Create_World(self):
        # Tell pyrosim where to store information about the world you'd like to create. 
        pyrosim.Start_SDF("world.sdf")
        # This world will currently be called box, because it will only contain a box (links can be spheres, cylinders, or boxes).
        pyrosim.Start_SDF("boxes.sdf")
        # Stores a box with initial position x, y, z and length, width and height all equal to 1 meter, in box.sdf.
        length, width, height = 20, 4, 1
        x, y, z = 0,0,1
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
        # Finish generate.py by appending
        pyrosim.End()

        while not os.path.exists("world.sdf"):
            time.sleep(0.01)

    def Create_Body(self):
        # Description of the robot's body in this urdf file
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,2.5] , size=[1, 1, 1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0.0 0.5 2", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0.5] , size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso" , child = "BackLeg" , type = "revolute", position = "0.0 -0.5 2", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0.5] , size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent= "Torso" , child = "LeftLeg" , type = "revolute", position = "-0.5 0.0 2", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0.5] , size=[1,0.2,0.2])
        pyrosim.Send_Joint(name = "Torso_RightLeg", parent= "Torso" , child = "RightLeg" , type = "revolute", position = "0.5 0.0 2", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0.5] , size=[1,0.2,0.2])
        
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg", parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = "0.0 1.0 0.5", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg", parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = "0.0 -1.0 0.5", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg", parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = "-1.0 0.0 0.5", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg", parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = "1.0 0.0 0.5", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.End()

        while not os.path.exists("body.urdf"):
            time.sleep(0.01)

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        # Sensor neurons - going to receive a value from sensors stored in Torso, BackLeg, and FrontLeg
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")

        # Motor neurons - send values to the motor controlling joint Torso_BackLeg & Torso_FrontLeg
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name = 8 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 9 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 10 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 11 , jointName = "RightLeg_RightLowerLeg")

        # Generating synapses - Connects neuron i to neuron j with a synaptic with weight w
        # Outer loop  iterate over the names of the SENSOR neurons
        for currentRow in range(c.numSensorNeurons):
            # Inner loop  iterate over each of the MOTOR neurons
            for currentColumn in range(c.numMotorNeurons):
                # generate a synapse that connects the ith sensor neuron to the jth motor neuron. 
                # send random synaptic weights in the range [-1,1]
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+(c.numSensorNeurons) , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

        while not os.path.exists("brain"+str(self.myID)+".nndf"):
            time.sleep(0.01)

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons-1)
        randomColumn = random.randint(0, c.numMotorNeurons-1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self, newId):
        self.myID = newId
