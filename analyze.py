import numpy
import os
import matplotlib.pyplot as plt

# Load sensor data
# backLegSensorValues = numpy.load(os.path.join('data', 'backLegSensorValues.npy'));
# frontLegSensorValues = numpy.load(os.path.join('data', 'frontLegSensorValues.npy'));

# print(backLegSensorValues)
# print(frontLegSensorValues)

# plt.plot(backLegSensorValues, label='BackLeg', linewidth=5)
# plt.plot(frontLegSensorValues, label='FrontLeg', linewidth=3)

# plt.xlabel("Time Step")
# plt.ylabel("Sensor Values")

# Load sinusoidally array
motorValuesBackLeg = numpy.load(os.path.join('data', 'motorValuesBackLeg.npy'));
motorValuesFrontLeg = numpy.load(os.path.join('data', 'motorValuesFrontLeg.npy'));
plt.plot(motorValuesBackLeg, label='Back Leg Motor values', linewidth=5)
plt.plot(motorValuesFrontLeg, label='Front Leg Motor values', linewidth=1)

# print((numpy.pi/4)*numpy.sin(targetAngles))
# plt.plot(targetAngles)

plt.legend()
plt.show()

exit()