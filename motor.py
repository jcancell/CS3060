import numpy as np
import constraints as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.SIM_STEPS)

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.backLeg_amplitude
        self.frequency = c.backLeg_frequency
        self.offset = c.backLeg_phaseOffset
        
        vals = np.linspace(0, 2 * np.pi, c.SIM_STEPS)

        self.motorValues = [self.amplitude * np.sin(self.frequency * x + self.offset)for x in vals]

    def Set_Value(self, robotId, x):
        
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[x],
            maxForce = 50)

