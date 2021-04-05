import pyrosim.pyrosim as pyrosim
import random

# size
length = 1
width = 1
height = 1


def Create_World():
    # box
    pyrosim.Start_SDF("world.sdf")
    # the world
    pyrosim.Send_Cube(name="Box", pos=[-2, 2, 0.5], size=[length, width, height])
    # End
    pyrosim.End()


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    # Robot Torso
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    # Connect BackLeg to Torso with one joint
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="2.0 0.0 1.0")
    # Robot FrontLeg
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    # Connect FrontLeg to Torso with a second joint.
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="1.0 0.0 1.0")
    # The other BackLeg
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    # End
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLeg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    for i in {0, 1, 2}:
        for j in {3, 4}:
            pyrosim.Send_Synapse( sourceNeuronName=i, targetNeuronName=j, weight=random.uniform(-1, 1) )
    pyrosim.End()

# call the functions
Create_World()
Generate_Body()
Generate_Brain()
