from simulation import SIMULATION

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as t
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

backLegMotorValues = np.zeros(SIM_STEPS)
frontLegMotorValues = np.zeros(SIM_STEPS)

vals = np.linspace(0, 2 * np.pi, SIM_STEPS)

backLeg_targetAngles = [backLeg_amplitude * np.sin(backLeg_frequency * x + backLeg_phaseOffset)for x in vals]

frontLeg_targetAngles = [frontLeg_amplitude * np.sin(frontLeg_frequency * x + frontLeg_phaseOffset)for x in vals]

simulation = SIMULATION()
simulation.Run()

np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
np.save('data/backLegMotorValues.npy', backLegMotorValues)
np.save('data/frontLegMotorValues', frontLegMotorValues)
