import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import os
class SENSOR:
	# defines a constructor for this class
	def __init__(self, linkName):
		self.linkName = linkName

		# Create a numpy vector, filled with zeros, that has the same length as the number of iterations of your for loop, just before entering the for loop
		self.values = numpy.zeros(c.numLoops)

	def Get_Value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		# Save all sensor values
		if t == (c.numLoops-1):
			self.Save_Values()

	def Save_Values(self):
		# Save SensorValues in backLegSensorValues.npy folder
		numpy.save(os.path.join('data', 'SensorValues.npy'), self.values)