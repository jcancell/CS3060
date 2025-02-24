from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
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
