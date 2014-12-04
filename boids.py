import maya.cmds as mc
import random

distance = 10
timedelta = 2000
startval = 0
objects = 30
timestep = 40

cubes = []
cubeposX = []
cubeposY = []
cubeposZ = []

def createObjects():
    for x in range(objects):
        tmp = mc.polyCube(constructionHistory=True, width=1, height=1, depth=1)
        cubes.append(tmp)
        zCord = random.random()*10
        xCord = random.random()*10
        cubeposX.append(xCord)
        cubeposZ.append(zCord)
        mc.setKeyframe(tmp, time=1, v=zCord, at='translateZ')
        mc.setKeyframe(tmp, time=1, v=xCord, at='translateX')

    return True
    
def simulate():
    for x in range(timedelta/timestep):
        x = x * timestep
        for cube in range(objects):
            cubeposX[cube] += random.random()*2 - 1
            cubeposZ[cube] += random.random()*2 - 1

            mc.setKeyframe(cubes[cube], time=x, v=cubeposZ[cube], at='translateZ')
            mc.setKeyframe(cubes[cube], time=x, v=cubeposX[cube], at='translateX')

    return True
        
def main():
    createObjects()
    set = mc.sets()
    print mc.select('set1')
