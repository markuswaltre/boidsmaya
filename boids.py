import maya.cmds as cmds
import random
from boid import *
from vec import *
from separation import *
from cohesion import *
from alignment import *
from GUI import *

## variables
OBJECTS = 20
NEIGHBOR_DISTANCE = 40
KEYFRAMES = 2000
TIMESTEP = 20
START_POS = 40

def deleteAllObjects():
	cmds.select( all=True )
	cmds.delete()

def createBoids(number):
	arr = []

	for index in range(number):
		arr.append(make_boid(index))

	return arr

def firstKeyframe(boids_array):
	for boid in boids_array:

		pos = []
		pos.append(random.random() * START_POS - START_POS/2)
		pos.append(random.random() * START_POS - START_POS/2)
		pos.append(random.random() * START_POS - START_POS/2)

		vel = [0, 0, 0]

		boid.setPosition(pos)
		boid.setVelocity(vel)

		keyframeTranslate(boid.getObj(), 0, pos)
		keyframeTranslate(boid.getTarget(), 0, pos)
		boid.setAim()

def keyframeTranslate(obj, t, position):
	cmds.setKeyframe(obj, time=t, v=position[0], at='translateX')
	cmds.setKeyframe(obj, time=t, v=position[1], at='translateY')
	cmds.setKeyframe(obj, time=t, v=position[2], at='translateZ')

def simulateKeyframes(boids_array):

	for keyframe in range(KEYFRAMES/TIMESTEP):
		for boidIndex in range(len(boids_array)):
			boid = boids_array[boidIndex]

			## get vectors
			separation 	= calculateSeparation(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			cohesion 	= calculateCohesion(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			alignment 	= calculateAlignment(boidIndex, boids_array, NEIGHBOR_DISTANCE)
		
			separation = scale_by_scalar(separation, 0.06)
			alignment = scale_by_scalar(alignment, -0.02)
			newVelocity = [0,0,0]

			## new velocity
			currentVelocity = boid.getVelocity()
			newVelocity = add(currentVelocity, add(cohesion, add(alignment,separation)))
			
			boid.setVelocity(newVelocity)

			## new position for boid
			currentPosition = boid.getPosition()
			newPosition = add(currentPosition, scale_by_scalar(newVelocity, 0.4))
			boid.setPosition(newPosition)

			## new position for target
			targetPosition = add(newPosition, scale_by_scalar(newVelocity, 0.4))
			boid.setTargetPosition(targetPosition)

			## update keyframe position
			keyframeTranslate(boid.getObj(), keyframe*TIMESTEP, newPosition)
			keyframeTranslate(boid.getTarget(), keyframe*TIMESTEP, targetPosition)

def main(number):

	## delete scene
	deleteAllObjects()

	## create boids
	boids_array = createBoids(number)

	## randomize positions
	firstKeyframe(boids_array)

	## simulate keyframes
	simulateKeyframes(boids_array)

	## play environment
	cmds.play()

createUI( 'BEZTBOIDZ', applyCallback )

