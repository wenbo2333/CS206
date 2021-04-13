from simulation import SIMULATION
import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
import os
import time
import pybullet_data
import sys

directOrGUI = sys.argv[1]   # Gets the 2nd element after python3
solutionID = sys.argv[2]    # Gets the 3rd element after python3
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()