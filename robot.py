from sensor import SENSOR
from motor import MOTOR
import constraints as c

import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np

from pyrosim.neuralNetwork import NEURAL_NETWORK

import os
class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system(f"del brain{solutionID}.nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")

                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

                jointName = jointName.decode("utf-8")

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        self.stateOfLinkZero = p.getLinkState(self.robotId,0)

        self.positionOfLinkZero = self.stateOfLinkZero[0]

        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
        
        fitness_filename = f"fitness{self.solutionID}.txt"
        with open(fitness_filename, "w") as file:
            file.write(str(self.xCoordinateOfLinkZero))
            file.close()

        os.system(f'rename tmp{self.solutionID}.txt fitness{self.solutionID}.txt')