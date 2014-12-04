import maya.cmds as cmds
import random
from boid import *
from vec import *
from separation import *
from cohesion import *
from alignment import *

## variables
OBJECTS = 20
NEIGHBOR_DISTANCE = 40
KEYFRAMES = 2000
TIMESTEP = 50

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
		# xVel = 0
		# yVel = 0
		# zVel = 0

		boid.setPosition([xPos, yPos, zPos])
		boid.setVelocity([xVel, yVel, zVel])

		cmds.setKeyframe(boid.getObj(), time=0, v=xPos, at='translateX')
		cmds.setKeyframe(boid.getObj(), time=0, v=yPos, at='translateY')
		cmds.setKeyframe(boid.getObj(), time=0, v=zPos, at='translateZ')

def simulateKeyframes(boids_array):

	for keyframe in range(KEYFRAMES/TIMESTEP):
		for boidIndex in range(len(boids_array)):
			boid = boids_array[boidIndex]

			## get vectors
			separation 	= calculateSeparation(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			# cohesion 	= calculateCohesion(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			# alignment 	= calculateAlignment(boidIndex, boids_array, NEIGHBOR_DISTANCE)

			## new velocity
			currentVelocity = boid.getVelocity()
			# newVelocity = add(currentVelocity, add(cohesion, alignment))
			newVelocity = add(currentVelocity, separation)
			boid.setVelocity(newVelocity)

			## new position
			currentPostion = boid.getPosition()
			newPosition = add(currentPostion, newVelocity)
			boid.setPosition(newPosition)

			## update keyframe
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[0], at='translateX')
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[1], at='translateY')
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[2], at='translateZ')
		
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

