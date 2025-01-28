import pyrosim.pyrosim as pyrosim

length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box1", pos=[x - 3, y + 3, z] , size=[length, width, height])

    #x, y, z = 1, 0, 1.5

    #pyrosim.Send_Cube(name="Box2", pos=[x, y, z] , size=[length, width, height])

    '''
    for i in range(10):
        pyrosim.Send_Cube(name="Tower", pos=[x, y, (z + i)], size=[length, width, height])
        length, width, height = length * 0.9, width * 0.9, height * 0.9
    '''

    '''
    size = 1

    for i in range(5):
        for i in range(5):
            for i in range(10):
                pyrosim.Send_Cube(name="Tower", pos=[x, y, (z + i)], size=[size, size, size])
                size = size * 0.9

            y = y + 1
            size = 1
            
        x = x + 1
        y = 0
    '''

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])

    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [x + 0.5, y, z + 1])

    pyrosim.Send_Cube(name="Leg", pos=[x + 1, y, z + 1], size=[length, width, height])

    pyrosim.End()

Create_World()
Create_Robot()