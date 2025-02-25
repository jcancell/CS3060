import numpy as np
import constraints as c
import pyrosim.pyrosim as pyrosim
class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        self.values = np.zeros(c.SIM_STEPS)

    def Get_Value(self, x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        np.save(f'data/{self.linkName}_SensorValues.npy', self.values)