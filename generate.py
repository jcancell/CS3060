import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5

#pyrosim.Send_Cube(name="Box1", pos=[x, y, z] , size=[length, width, height])

#x, y, z = 1, 0, 1.5

#pyrosim.Send_Cube(name="Box2", pos=[x, y, z] , size=[length, width, height])

for i in range(10):
    pyrosim.Send_Cube(name="Tower", pos=[x, y, (z + i)], size=[length, width, height])
    length, width, height = length * 0.9, width * 0.9, height * 0.9

pyrosim.End()