from simulation import SIMULATION
'''
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as t
import numpy as np
import random as rd
import constraints as c
'''
simulation = SIMULATION()
simulation.Run()
'''
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
np.save('data/backLegMotorValues.npy', backLegMotorValues)
np.save('data/frontLegMotorValues', frontLegMotorValues)
'''