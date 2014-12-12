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
TIMESTEP = 20

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

		xVel = 0 #random.random() - 1
		yVel = 0 #random.random() - 1
		zVel = 0 #random.random() - 1
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
			cohesion 	= calculateCohesion(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			alignment 	= calculateAlignment(boidIndex, boids_array, NEIGHBOR_DISTANCE)
		
			separation = scale_by_scalar(separation, 0.06)
			alignment = scale_by_scalar(alignment, -0.02)
			newVelocity = [0,0,0]
			## new velocity
			currentVelocity = boid.getVelocity()
			newVelocity = add(currentVelocity, add(cohesion, add(alignment,separation)))
			# newVelocity = add(currentVelocity, cohesion)
			boid.setVelocity(newVelocity)

			## new position
			currentPostion = boid.getPosition()
			newPosition = add(currentPostion, scale_by_scalar(newVelocity, 0.4))
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


	# import boidsmaya.boids as toby
	# import boidsmaya.separation as sep
	# import boidsmaya.cohesion as coh
	# import boidsmaya.boid as bd
	# reload(toby)
	# reload(sep)
	# reload(coh)
	# reload(bd)
	# toby.main()

