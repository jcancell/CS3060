import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rd
import constraints as c

SIM_STEPS = c.SIM_STEPS
# num seconds between loop iterations
SIM_SPEED = c.SIM_SPEED

frontLeg_amplitude = c.frontLeg_amplitude
frontLeg_frequency = c.frontLeg_frequency
frontLeg_phaseOffset = c.frontLeg_phaseOffset

backLeg_amplitude = c.backLeg_amplitude
backLeg_frequency = c.backLeg_frequency
backLeg_phaseOffset = c.backLeg_phaseOffset

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(SIM_STEPS)
frontLegSensorValues = np.zeros(SIM_STEPS)
backLegMotorValues = np.zeros(SIM_STEPS)
frontLegMotorValues = np.zeros(SIM_STEPS)

vals = np.linspace(0, 2 * np.pi, SIM_STEPS)

backLeg_targetAngles = [backLeg_amplitude * np.sin(backLeg_frequency * x + backLeg_phaseOffset)for x in vals]

frontLeg_targetAngles = [frontLeg_amplitude * np.sin(frontLeg_frequency * x + frontLeg_phaseOffset)for x in vals]

#np.save('data/targetAngles.npy', targetAngles)
#exit()

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
        targetPosition = backLeg_targetAngles[x],
        maxForce = 50)
    
    backLegMotorValues[x] = backLeg_targetAngles[x]

    # Front Leg Motor
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = frontLeg_targetAngles[x],
        maxForce = 50)
    
    frontLegMotorValues[x] = frontLeg_targetAngles[x]

    t.sleep(SIM_SPEED)
    #print(x)
p.disconnect()

np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
np.save('data/backLegMotorValues.npy', backLegMotorValues)
np.save('data/frontLegMotorValues', frontLegMotorValues)
#print(backLegSensorValues)