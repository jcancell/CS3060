import numpy as np
import constraints as c
import pyrosim.pyrosim as pyrosim
class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        self.values = np.zeros(c.SIM_STEPS)

    def Get_Value(self, x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
        if x == c.SIM_STEPS - 1:
            print(self.values)