from world import WORLD
from robot import ROBOT
import constraints as c

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as t
class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()
        
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()

    def __del__(self):

        p.disconnect()

    def Run(self):
        for x in range(c.SIM_STEPS):
            #print(x)
            
            p.stepSimulation()
            self.robot.Sense(x)
            
            '''
            # Back Leg Motor
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = simulation.robot.robotId,
                jointName = b'Torso_BackLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = backLeg_targetAngles[x],
                maxForce = 50)
            
            backLegMotorValues[x] = backLeg_targetAngles[x]

            # Front Leg Motor
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = simulation.robot.robotId,
                jointName = b'Torso_FrontLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = frontLeg_targetAngles[x],
                maxForce = 50)
            
            frontLegMotorValues[x] = frontLeg_targetAngles[x]
            '''
            t.sleep(c.SIM_SPEED)