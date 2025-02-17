import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rd

SIM_STEPS = 1000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(SIM_STEPS)
frontLegSensorValues = np.zeros(SIM_STEPS)

for x in range(SIM_STEPS):
    p.stepSimulation()

    #backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    #print(backLegTouch)

    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Back Leg Motor
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = (rd.uniform(-np.pi/2, np.pi/2)),
        maxForce = 50)
    
    # Front Leg Motor
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = (rd.uniform(-np.pi/2, np.pi/2)),
        maxForce = 50)

    t.sleep(1/60)
    #print(x)
p.disconnect()

np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#print(backLegSensorValues)