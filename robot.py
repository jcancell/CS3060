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
                desiredAngle = desiredAngle * c.motorJointRange

                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

                jointName = jointName.decode("utf-8")

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        #self.stateOfLinkZero = p.getLinkState(self.robotId,0)
        self.basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)

        #self.positionOfLinkZero = self.stateOfLinkZero[0]
        self.basePosition = self.basePositionAndOrientation[0]

        #self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
        self.xPosition = self.basePosition[0]
        self.yPosition = self.basePosition[1]
        self.zPosition = self.basePosition[2]

        #print(self.basePositionAndOrientation)
        #print(self.basePosition)
        #print(self.xPosition)
        fitnessVal = 0.01
        #fitnessVal = self.xPosition
        
        if self.zPosition < 2:
            fitnessVal = 10.0
        else:
            fitnessVal = self.xPosition
        
        
        fitness_filename = f"tmp{self.solutionID}.txt"
        with open(fitness_filename, "w") as file:
            file.write(str(fitnessVal))
            file.close()

        os.system(f'rename tmp{self.solutionID}.txt fitness{self.solutionID}.txt')