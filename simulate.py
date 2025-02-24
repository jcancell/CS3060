from simulation import SIMULATION

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as t
import numpy as np
import random as rd
import constraints as c

simulation = SIMULATION()

SIM_STEPS = c.SIM_STEPS
# num seconds between loop iterations
SIM_SPEED = c.SIM_SPEED

frontLeg_amplitude = c.frontLeg_amplitude
frontLeg_frequency = c.frontLeg_frequency
frontLeg_phaseOffset = c.frontLeg_phaseOffset

backLeg_amplitude = c.backLeg_amplitude
backLeg_frequency = c.backLeg_frequency
backLeg_phaseOffset = c.backLeg_phaseOffset

backLegSensorValues = np.zeros(SIM_STEPS)
frontLegSensorValues = np.zeros(SIM_STEPS)
backLegMotorValues = np.zeros(SIM_STEPS)
frontLegMotorValues = np.zeros(SIM_STEPS)

vals = np.linspace(0, 2 * np.pi, SIM_STEPS)

backLeg_targetAngles = [backLeg_amplitude * np.sin(backLeg_frequency * x + backLeg_phaseOffset)for x in vals]

frontLeg_targetAngles = [frontLeg_amplitude * np.sin(frontLeg_frequency * x + frontLeg_phaseOffset)for x in vals]

for x in range(SIM_STEPS):
    p.stepSimulation()

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

    t.sleep(SIM_SPEED)

p.disconnect()

np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
np.save('data/backLegMotorValues.npy', backLegMotorValues)
np.save('data/frontLegMotorValues', frontLegMotorValues)
