import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
# To write arrays to file
import os
# To slow things down
import time
import pybullet_data

# --Number of loops the program iterates over--
numLoops = 600

# gravity (alterned)
gravity = -9.8*1.5

# number of generations evaluated
numberOfGenerations = 20

# Population size
populationSize = 10

# number of sensors
numSensorNeurons = 4

# number of motors
numMotorNeurons = 8

# makes the joint's angle range narrower/larger
motorJointRange = 0.27

# --The bots motion--
# Motor motion
amplitude = numpy.pi/4
frequency = 10
phaseOffset = 0

# Back Leg motion
amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

# Frontleg motion
amplitudeFrontLeg = numpy.pi/4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = numpy.pi/2

# values that vary sinusoidally over the range -pi to pi, determine cycle movement
motorValuesBackLeg = amplitudeBackLeg * numpy.sin(frequencyBackLeg * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + phaseOffsetBackLeg)
motorValuesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + phaseOffsetFrontLeg)

# max force of motors
maxForce = 55