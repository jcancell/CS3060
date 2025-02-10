import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')

#print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)

frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

#print(backLegSensorValues)

matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2.5)

matplotlib.pyplot.legend()

matplotlib.pyplot.show()