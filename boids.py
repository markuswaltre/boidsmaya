import maya.cmds as cmds
import random
from boid import *
from vec import *
from separation import *
from cohesion import *
from alignment import *
from goals import *
from GUI import *

## variables
TIMESTEP = 20 # this is speed n' stuff
START_POS = 40

def deleteAllObjects():
	if len(cmds.ls('boid*', r=True)) > 0:
		cmds.select('boid*', r=True)
		cmds.delete()		

def createBoids(number):
	arr = []

	for index in range(number):
		arr.append(make_boid(index))

	return arr

def firstKeyframe(boids_array, bScale, cBoxShowTarget):
	for boid in boids_array:

		pos = []
		pos.append(random.random() * START_POS - START_POS/2)
		pos.append(random.random() * START_POS - START_POS/2)
		pos.append(random.random() * START_POS - START_POS/2)

		boid.setPosition(pos)
		boid.setScale(bScale)

		keyframeTranslate(boid.getObj(), 0, pos)
		keyframeTranslate(boid.getTarget(), 0, pos)
		boid.setAim()
		if not cBoxShowTarget:
			boid.hideTarget()

def keyframeTranslate(obj, t, position):
	cmds.setKeyframe(obj, time=t, v=position[0], at='translateX')
	cmds.setKeyframe(obj, time=t, v=position[1], at='translateY')
	cmds.setKeyframe(obj, time=t, v=position[2], at='translateZ')

def simulateKeyframes(boids_array, cRadius, sRadius, aRadius, nFrames, cWeight, sWeight, aWeight, mSpeed, goals_array, cBoxUseGoals, goals):
	for keyframe in range(nFrames/TIMESTEP):
		for boidIndex in range(len(boids_array)):
			boid = boids_array[boidIndex]

			## get steering rules
			separation 	= calculateSeparation(boidIndex, boids_array, sRadius)
			cohesion 	= calculateCohesion(boidIndex, boids_array, cRadius)
			alignment 	= calculateAlignment(boidIndex, boids_array, aRadius)
		
			separation = scale_by_scalar(separation, sWeight)
			alignment = scale_by_scalar(alignment, aWeight)
			cohesion = scale_by_scalar(cohesion, cWeight)

			## current velocity and position
			currentVelocity = boid.getVelocity()
			currentPosition = boid.getPosition()

			## new velocity
			newVelocity = add(currentVelocity, add(cohesion, add(alignment,separation)))
			if(cBoxUseGoals):
				goalVelocity = goals.calculateGoal(currentPosition, goals_array)
				newVelocity = add(newVelocity, scale_by_scalar(goalVelocity, 4))

			if(length(newVelocity) > mSpeed):	
				newVelocity = scale_by_scalar(newVelocity, 0.75)

			boid.setVelocity(newVelocity)

			## new position for boid
			newPosition = add(currentPosition, scale_by_scalar(newVelocity, 0.4))
			boid.setPosition(newPosition)

			## new position for target
			targetPosition = add(newPosition, scale_by_scalar(newVelocity, 0.4))
			boid.setTargetPosition(targetPosition)

			## update keyframe position
			keyframeTranslate(boid.getObj(), keyframe*TIMESTEP, newPosition)
			keyframeTranslate(boid.getTarget(), keyframe*TIMESTEP, targetPosition)

def main(nBoids, bScale, nFrames, mSpeed, cWeight, cRadius, sWeight, sRadius, aWeight, aRadius, cBoxShowTarget, cBoxUseGoals, cBox3):
	## set keyframe 0
	cmds.currentTime( 0 )

	## delete scene
	deleteAllObjects()

	## create boids
	boids_array = createBoids(nBoids)

	## create goal object
	goals = Goals()

	## get goals in scene
	goals_array = []
	if cBoxUseGoals:
		goals_array = goals.getGoals()

	## randomize positions
	firstKeyframe(boids_array, bScale, cBoxShowTarget)

	## simulate keyframes
	simulateKeyframes(boids_array, cRadius, sRadius, aRadius, nFrames, cWeight, sWeight, aWeight, mSpeed, goals_array, cBoxUseGoals, goals)

	cmds.playbackOptions(max=nFrames)
	cmds.playbackOptions(aet=nFrames)

	## play environment
	cmds.play()

createUI( 'BEZTBOIDZ', applyCallback )

