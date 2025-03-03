import numpy as np
import constraints as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.SIM_STEPS)

        self.amplitude = c.AMPLITUDE
        self.offset = c.OFFSET

        if self.jointName == b'Torso_FrontLeg':
            self.frequency = c.FREQUENCY
        else:
            self.frequency = c.FREQUENCY / 2

        vals = np.linspace(0, 2 * np.pi, c.SIM_STEPS)

        self.motorValues = [self.amplitude * np.sin(self.frequency * x + self.offset)for x in vals]

    def Set_Value(self, robotId, desiredAngle):
        
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[int(desiredAngle)],
            maxForce = 50)
    

