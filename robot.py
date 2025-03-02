from sensor import SENSOR
from motor import MOTOR
import constraints as c

import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np

from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:

            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, x):
        for sensor in self.sensors.values():
            sensor.Get_Value(x)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:

            self.motors[jointName] = MOTOR(jointName)

    def Act(self, x):
        for motor in self.motors.values():
            motor.Set_Value(self.robotId, x)

    def Think(self):
        self.nn.Print()
        