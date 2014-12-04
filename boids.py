import maya.cmds as cmds
import random
from boid import *
from vec import *
from separation import *

## variables
OBJECTS = 20
NEIGHBOR_DISTANCE = 2
KEYFRAMES = 2000
TIMESTEP = 10

def deleteAllObjects():
	cmds.select( all=True )
	cmds.delete()

def createBoids():
	arr = []

	for index in range(OBJECTS):
		arr.append(make_boid(index))

	return arr

def firstKeyframe(boids_array):
	for boid in boids_array:
		xPos = random.random() * 20 - 10
		yPos = random.random() * 20 - 10
		zPos = random.random() * 20 - 10

		xVel = random.random() - 1
		yVel = random.random() - 1
		zVel = random.random() - 1

		boid.setPosition([xPos, yPos, zPos])
		boid.setVelocity([xVel, yVel, zVel])

		cmds.setKeyframe(boid.getObj(), time=0, v=xPos, at='translateX')
		cmds.setKeyframe(boid.getObj(), time=0, v=yPos, at='translateY')
		cmds.setKeyframe(boid.getObj(), time=0, v=zPos, at='translateZ')

def simulateKeyframes(boids_array):

	for keyframe in range(KEYFRAMES/TIMESTEP):
		for boidIndex in range(len(boids_array)):
			sep = calculateSeparation(boidIndex, boids_array, NEIGHBOR_DISTANCE)
		
def main():
	## delete scene
	deleteAllObjects()

	## create boids
	boids_array = createBoids()

	## randomize positions
	firstKeyframe(boids_array)

	## simulate keyframes
	simulateKeyframes(boids_array)

	## play environment
	cmds.play()

