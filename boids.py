import maya.cmds as cmds
import random
from boid import *
from vec import *

distance = 10
timedelta = 2000
startval = 0
objects = 20
timestep = 6

cubes = []
cubeposX = []
cubeposY = []
cubeposZ = []


def deleteAllObjects():
	cmds.select( all=True )
	cmds.delete()

	return True

def createBoids():
	return True

def createObjects():
	for x in range(objects):
		name = "cube%s" % x
		tmp = cmds.polyCube(constructionHistory=True, width=1, height=1, depth=1, n=name)
		cubes.append(tmp)
		zCord = random.random()*10
		xCord = random.random()*10
		cubeposX.append(xCord)
		cubeposZ.append(zCord)
		cmds.setKeyframe(tmp, time=1, v=zCord, at='translateZ')
		cmds.setKeyframe(tmp, time=1, v=xCord, at='translateX')

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
	boids_array = createBoids()
	# createObjects()
	# simulate()
	x = make_boid(0)
	y = make_boid(1)
	y.setPosition([1, 1, 1])
	print x.getPosition()
	print y.getPosition()

	print dist(x.getPosition(), y.getPosition())
	cmds.play()

