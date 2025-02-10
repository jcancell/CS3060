import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy

SIM_STEPS = 1000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(SIM_STEPS)

for x in range(SIM_STEPS):
    p.stepSimulation()

    #backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    #print(backLegTouch)

    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    t.sleep(1/60)
    #print(x)
p.disconnect()

numpy.save('data\output.npy', backLegSensorValues)
print(backLegSensorValues)