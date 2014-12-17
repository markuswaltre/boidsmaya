import maya.cmds as cmds
import random
from boid import *
from vec import *
from separation import *
from cohesion import *
from alignment import *
from GUI import *

## variables
#OBJECTS = 20
#NEIGHBOR_DISTANCE = 40
#KEYFRAMES = 2000
TIMESTEP = 20

def deleteAllObjects():
	cmds.select( all=True )
	cmds.delete()

def createBoids(number):
	arr = []

	for index in range(number):
		arr.append(make_boid(index))

	return arr

def firstKeyframe(boids_array, bScale):
	for boid in boids_array:
		xPos = random.random() * 20 - 10
		yPos = random.random() * 20 - 10
		zPos = random.random() * 20 - 10

		xVel = 0 #random.random() - 1
		yVel = 0 #random.random() - 1
		zVel = 0 #random.random() - 1
		# xVel = 0
		# yVel = 0
		# zVel = 0

		boid.setPosition([xPos, yPos, zPos])
		boid.setVelocity([xVel, yVel, zVel])
		boid.setScale(bScale)

		cmds.setKeyframe(boid.getObj(), time=0, v=xPos, at='translateX')
		cmds.setKeyframe(boid.getObj(), time=0, v=yPos, at='translateY')
		cmds.setKeyframe(boid.getObj(), time=0, v=zPos, at='translateZ')

def simulateKeyframes(boids_array, cRadius, sRadius, aRadius, nFrames, cWeight, sWeight, aWeight, mSpeed):

	for keyframe in range(nFrames/TIMESTEP):
		for boidIndex in range(len(boids_array)):
			boid = boids_array[boidIndex]

			## get vectors
			separation 	= calculateSeparation(boidIndex, boids_array, sRadius)
			cohesion 	= calculateCohesion(boidIndex, boids_array, cRadius)
			alignment 	= calculateAlignment(boidIndex, boids_array, aRadius)
		
			separation = scale_by_scalar(separation, sWeight)
			alignment = scale_by_scalar(alignment, aWeight)
			cohesion = scale_by_scalar(cohesion, cWeight)

			newVelocity = [0,0,0]

			## new velocity
			currentVelocity = boid.getVelocity()

			newVelocity = add(currentVelocity, add(cohesion, add(alignment,separation)))
			
			if(length(newVelocity) > mSpeed):	
				newVelocity = scale_by_scalar(newVelocity, 0.75)

			# newVelocity = add(currentVelocity, cohesion)
			boid.setVelocity(newVelocity)

			## new position
			currentPostion = boid.getPosition()
			newPosition = add(currentPostion, scale_by_scalar(newVelocity, 1))#0.08
			boid.setPosition(newPosition)

			if(boidIndex == 0):
				target = cmds.polyCube(width=0.5, height=0.5, depth=0.5,  n='target')
				cmds.setAttr('%s.translate'%target[0], newPosition[0], newPosition[1], newPosition[2])
				cmds.aimConstraint(target[0], boid.getObj()[0], aim=[0,-1,0], u=[0,0,1], wu=[1,0,0], wut='vector', o=[0.00001, 0.0, 0.0])
				# cmds.delete(target[0])

			## update keyframe
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[0], at='translateX')
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[1], at='translateY')
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[2], at='translateZ')
	


def main(nBoids, bScale, nFrames, mSpeed, cWeight, cRadius, sWeight, sRadius, aWeight, aRadius):

	## delete scene
	deleteAllObjects()

	## create boids
	boids_array = createBoids(nBoids)

	## randomize positions
	firstKeyframe(boids_array, bScale)

	## simulate keyframes
	simulateKeyframes(boids_array, cRadius, sRadius, aRadius, nFrames, cWeight, sWeight, aWeight, mSpeed)

	cmds.playbackOptions(max=nFrames)
	cmds.playbackOptions(aet=nFrames)

	## play environment
	cmds.play()

createUI( 'BEZTBOIDZ', applyCallback )