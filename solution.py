import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constraints

length, width, height = 1, 1, 1

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        
        self.weights = np.random.rand(constraints.numSensorNeurons, constraints.numMotorNeurons)
        
        self.weights = self.weights * 2 - 1

        #print(self.weights)
        #exit()

    def Evaluate(self, mode="DIRECT"):
        self.Start_Simulation(mode)
        self.Wait_For_Simulation_To_End()

    def Start_Simulation(self, mode='DIRECT'):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("py simulate.py " + mode + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        #print(fitnessFileName)
        while not os.path.exists(fitnessFileName):
            #print(fitnessFileName)
            time.sleep(1.01)
        
        with open(fitnessFileName, 'r') as file:
            self.fitness = file.read()
            self.fitness = float(self.fitness)
            file.close()

        os.system(f'del {fitnessFileName}')
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box1", pos=[-3, 3, 0.5] , size=[length, width, height])

        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0], size=[length, width, height])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])

        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

        pyrosim.End()
    
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName="Torso_FrontLeg")

        for currentRow in range(constraints.numSensorNeurons):
            for currentColumn in range(constraints.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + constraints.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
                

        pyrosim.End()
        #exit()

    def Mutate(self):
        randomRow = random.randint(0, constraints.numSensorNeurons - 1)
        randomColumn = random.randint(0, constraints.numMotorNeurons - 1)

        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

        #self.Create_Brain()

    def Set_ID(self, ID):
        self.myID = ID