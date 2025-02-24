from sensor import SENSOR
from motor import MOTOR
import constraints as c

import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        self.motors = {}

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:

            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, x):
        for sensor in self.sensors.values():
            sensor.Get_Value(x)