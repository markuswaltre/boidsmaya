import maya.cmds as cmds
import random
from boid import *
from vec import *
from separation import *

## variables
OBJECTS = 20
NEIGHBOR_DISTANCE = 2

timedelta = 2000
startval = 0
timestep = 6

cubes = []
cubeposX = []
cubeposY = []
cubeposZ = []


def deleteAllObjects():
	cmds.select( all=True )
	cmds.delete()

	return True

def createBoids(size):
	arr = []

	for index in range(size):
		arr.append(make_boid(index))

	return arr

def firstKeyframe(boids_array):
	for boid in boids_array:
		xPos = random.random()*20 - 10
		yPos = random.random()*20 - 10
		zPos = random.random()*20 - 10

		xVel = random.random() - 1
		yVel = random.random() - 1
		zVel = random.random() - 1

		boid.setPosition([xPos, yPos, zPos])
		boid.setVelocity([xVel, yVel, zVel])

		cmds.setKeyframe(boid.getObj(), time=0, v=xPos, at='translateX')
		cmds.setKeyframe(boid.getObj(), time=0, v=yPos, at='translateY')
		cmds.setKeyframe(boid.getObj(), time=0, v=zPos, at='translateZ')

def simulateKeyframes(boids_array):

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
	## delete scene
	deleteAllObjects()
	## create boids
	boids_array = createBoids(OBJECTS)
	## randomize positions
	firstKeyframe(boids_array)

	## simulate keyframes

	print separation(0, boids_array, NEIGHBOR_DISTANCE)

	## create keyframes
	#simulateBoids(boids_array)

	# createObjects()
	# simulate()
	# x = make_boid(0)
	# y = make_boid(1)
	# y.setPosition([1, 1, 1])
	# print x.getPosition()
	# print y.getPosition()

	# print dist(x.getPosition(), y.getPosition())
	cmds.play()

