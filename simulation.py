from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
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
        self.sensors = {}
        self.motors = {}
        
        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        for x in range(c.SIM_STEPS):
            #print(x)
            
            p.stepSimulation()
            '''
            backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

            frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

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