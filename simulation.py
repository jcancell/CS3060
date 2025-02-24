from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR

class SIMULATION:

    def __init__(self):

        self.world = WORLD()
        self.robot = ROBOT()
        self.sensors = {}
        self.motors = {}