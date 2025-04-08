import pyrosim.pyrosim as pyrosim
import random

length, width, height = 1, 1, 1

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box1", pos=[-3, 3, 0.5] , size=[1, 1, 1])

    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])

    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0, 0.5, 1] , jointAxis = "1 0 0") #Step 29

    pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0, -0.5, 1] , jointAxis = "1 0 0") # Step 29

    pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

    pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5, 0, 1] , jointAxis = "0 1 0") # Step 29

    pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

    pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1],jointAxis="0 1 0")
    
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
    '''
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])

    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])

    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])

    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

    pyrosim.End()
    '''

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name = 4, jointName="Torso_FrontLeg")

    for i in range(3):
        for j in range(3, 5):
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight = random.uniform(-1.0, 1.0))
            

    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()