import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for x in range(1000):
    p.stepSimulation()
    t.sleep(1/60)
    print(x)
p.disconnect()