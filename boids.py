import maya.cmds as cmds
import random
from boid import *
from vec import *
from separation import *
from cohesion import *
from alignment import *
from GUI import *

## variables
TIMESTEP = 20
START_POS = 40
goal_array = []


def deleteAllObjects():
	cmds.select(all=True)
	cmds.delete()

	cmds.select('boid*', r=True)
	cmds.delete()


def getGoals():
	goals = []

	cmds.select('goal*', r=True)
	selected = cmds.ls(sl=True)
	for item in range(len(selected)/2): 
		x = cmds.getAttr("%s.translateX" % selected[item])
		y = cmds.getAttr("%s.translateY" % selected[item])
		z = cmds.getAttr("%s.translateZ" % selected[item])
		pos = [x,y,z]
		goals.append(pos)

	return goals


	
	

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

def simulateKeyframes(boids_array, cRadius, sRadius, aRadius, nFrames, cWeight, sWeight, aWeight, mSpeed, goals_array):
	goal_index = 0
	for keyframe in range(nFrames/TIMESTEP):
		for boidIndex in range(len(boids_array)):
			boid = boids_array[boidIndex]

			## get vectors

			separation 	= calculateSeparation(boidIndex, boids_array, sRadius)
			cohesion 	= calculateCohesion(boidIndex, boids_array, cRadius)
			alignment 	= calculateAlignment(boidIndex, boids_array, aRadius)

			if(boidIndex==0):
				separation = scale_by_scalar(separation,0.5)
				cohesion = scale_by_scalar(cohesion,0.5)
		
			separation = scale_by_scalar(separation, sWeight)
			alignment = scale_by_scalar(alignment, aWeight)
			cohesion = scale_by_scalar(cohesion, cWeight)

			newVelocity = [0,0,0]

			## new velocity
			currentVelocity = boid.getVelocity()

			newVelocity = add(currentVelocity, add(cohesion, add(alignment,separation)))

			if(length(newVelocity) > mSpeed):	
				newVelocity = scale_by_scalar(newVelocity, 0.75)

			currentPosition = boid.getPosition()

			if(boidIndex == 0):
				#	print dist(currentPosition, goals_array[goal_index])
				if(dist(currentPosition, goals_array[goal_index]) < 10):
					goal_index = goal_index + 1
					if(goal_index > len(goals_array)-1):
						goal_index = (len(goals_array)-1)
				goalVector = sub(goals_array[goal_index], currentPosition)
				goalVector = norm(goalVector)
				goalVector = scale_by_scalar(goalVector, 0.7)
				newVelocity = add(newVelocity, goalVector)
				

			boid.setVelocity(newVelocity)

			## new position for boid
			#currentPosition = boid.getPosition()
			newPosition = add(currentPosition, scale_by_scalar(newVelocity, 1))

			boid.setPosition(newPosition)

			## new position for target
			targetPosition = add(newPosition, scale_by_scalar(newVelocity, 0.4))
			boid.setTargetPosition(targetPosition)

			## update keyframe position
			keyframeTranslate(boid.getObj(), keyframe*TIMESTEP, newPosition)
			keyframeTranslate(boid.getTarget(), keyframe*TIMESTEP, targetPosition)

def main(nBoids, bScale, nFrames, mSpeed, cWeight, cRadius, sWeight, sRadius, aWeight, aRadius, cBoxShowTarget, cBoxUseGoals, cBox3):

	## delete scene
	deleteAllObjects()

	## create boids
	boids_array = createBoids(nBoids)

	## get goals in scene
	goals_array = getGoals()

	## randomize positions
	firstKeyframe(boids_array, bScale, cBoxShowTarget)

	## simulate keyframes

	simulateKeyframes(boids_array, cRadius, sRadius, aRadius, nFrames, cWeight, sWeight, aWeight, mSpeed, goals_array)

	cmds.playbackOptions(max=nFrames)
	cmds.playbackOptions(aet=nFrames)

	## play environment
	cmds.play()

createUI( 'BEZTBOIDZ', applyCallback )

