import matplotlib.pyplot
import numpy
import os.path

backLegSensorValues = numpy.load("data/backLegSense.npy")
frontLegSensorValues = numpy.load("data/frontLegSense.npy")
# Visualization
matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label='front leg',linewidth=1)
matplotlib.pyplot.title('Visualization')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
