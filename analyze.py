import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load('data/backLegSensorValues.npy')

#print(backLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)

#frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

#print(backLegSensorValues)

#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2.5)


#targetAngles = numpy.load('data/targetAngles.npy')

#matplotlib.pyplot.plot(targetAngles)


backLegMotorValues = numpy.load('data/backLegMotorValues.npy')

matplotlib.pyplot.plot(backLegMotorValues, label="Back Leg", linewidth=5)

frontLegMotorValues = numpy.load('data/frontLegMotorValues.npy')

matplotlib.pyplot.plot(frontLegMotorValues, label="Front Leg", linewidth=1.5)


matplotlib.pyplot.legend()

matplotlib.pyplot.show()