import maya.cmds as cmds
import random

distance = 10
timedelta = 3000
startval = 0
objects = 70
timestep = 60

cubes = []
cubeposX = []
cubeposY = []
cubeposZ = []

def boid(): 
	_position = 0
	_velocity = 0
	

def createObjects():
	for x in range(objects):
		name = 'cube%s' % x
		tmp = cmds.polyCube(constructionHistory=True, width=1, height=1, depth=1, n=name)
		cubes.append(tmp)
		zCord = random.random()*10
		xCord = random.random()*10
		cubeposX.append(xCord)
		cubeposZ.append(zCord)
		cmds.setKeyframe(tmp, time=1, v=zCord, at='translateZ')
		cmds.setKeyframe(tmp, time=1, v=xCord, at='translateX')

	return True

def deleteAllObjects():
	cmds.select( all=True )
	cmds.delete()

	return True


def simulate():
	for x in range(timedelta/timestep):
		x = x * timestep
		for cube in range(objects):
			cubeposX[cube] += random.random()*2 - 1
			cubeposZ[cube] += random.random()*2 - 1

			cmds.setKeyframe(cubes[cube], time=x, v=cubeposZ[cube], at='translateZ')
			cmds.setKeyframe(cubes[cube], time=x, v=cubeposX[cube], at='translateX')

	return True
		
def main():
	deleteAllObjects()
	createObjects()
	simulate()
	cmds.play()