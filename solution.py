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

        pyrosim.Send_Cube(name="Box1", pos=[-22.5, 0, 1] , size=[50, 5, 2])

        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")


        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 4], size=[length, width, height])


        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0, 0.5, 4] , jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])


        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0, -0.5, 4] , jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])


        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5, 0, 4] , jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])


        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 4],jointAxis="0 1 0")
        
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1,0.2,0.2])


        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])


        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])


        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])


        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])

        pyrosim.End()
        #exit() #Step 30
    
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        '''
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName="RightLeg")
        '''
        pyrosim.Send_Sensor_Neuron(name = 0, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 5, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")

        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_RightLowerLeg")

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