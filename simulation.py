from world import WORLD
from robot import ROBOT
import constraints as c

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as t
class SIMULATION:

    def __init__(self, directOrGUI):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)

        self.directOrGUI = directOrGUI

        #self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()
        
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def __del__(self):

        p.disconnect()

    def Run(self):
        for x in range(c.SIM_STEPS):
            
            p.stepSimulation()
            self.robot.Sense(x)

            self.robot.Think()

            self.robot.Act(x)
            
            if self.directOrGUI == "GUI":
                t.sleep(c.SIM_SPEED)

    def Get_Fitness(self):
        self.robot.Get_Fitness()