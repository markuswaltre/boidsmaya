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
KEYFRAMES = 4000
TIMESTEP = 20
boids_array = []
goal_array = []


def deleteAllObjects():
	# cmds.select(all=True)
	# cmds.delete()

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

def simulateKeyframes(boids_array, goals_array):
	goal_index = 0
	for keyframe in range(KEYFRAMES/TIMESTEP):
		for boidIndex in range(len(boids_array)):
			boid = boids_array[boidIndex]

			## get vectors
			separation 	= calculateSeparation(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			cohesion 	= calculateCohesion(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			alignment 	= calculateAlignment(boidIndex, boids_array, NEIGHBOR_DISTANCE)
			
			if(boidIndex==0):
				separation = scale_by_scalar(separation,0.5)
				cohesion = scale_by_scalar(cohesion,0.5)

			separation = scale_by_scalar(separation, 0.06)
			alignment = scale_by_scalar(alignment, -0.02)
			newVelocity = [0,0,0]

			## new velocity
			currentVelocity = boid.getVelocity()
			newVelocity = add(currentVelocity, add(cohesion, add(alignment,separation)))

			#moved currentPosition here because it is used in this if statement
			currentPostion = boid.getPosition()
			if(boidIndex == 0):
				print dist(currentPostion, goals_array[goal_index])
				if(dist(currentPostion, goals_array[goal_index]) < 10):
					goal_index = goal_index + 1
					if(goal_index > len(goals_array)-1):
						goal_index = (len(goals_array)-1)
				goalVector = sub(goals_array[goal_index], currentPostion)
				goalVector = norm(goalVector)
				goalVector = scale_by_scalar(goalVector, 0.7)
				newVelocity = add(newVelocity, goalVector)
				

			# newVelocity = add(currentVelocity, cohesion)
			boid.setVelocity(newVelocity)

			## new position
			newPosition = add(currentPostion, scale_by_scalar(newVelocity, 0.4))
			boid.setPosition(newPosition)



			# if(boidIndex == 0):
			# 	print boid.getObj()
			# 	target = cmds.polyCube(width=0.5, height=0.5, depth=0.5,  n='target')
			# 	cmds.setAttr('%s.translate'%target[0], currentPostion[0]+newVelocity[0], newPosition[1]+newVelocity[1], newPosition[2]+newVelocity[2])
			# 	cmds.aimConstraint(target[0], boid.getObj()[0], aim=[1,0,0], u=[0,0,1], wu=[1,0,0], wut='vector', o=[0.00001, 0.0, 0.0])
			# 	cmds.delete(target[0])

			## update keyframe
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[0], at='translateX')
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[1], at='translateY')
			cmds.setKeyframe(boid.getObj(), time=keyframe*TIMESTEP, v=newPosition[2], at='translateZ')
	


def main(number):

	## delete scene
	deleteAllObjects()

	## create boids
	boids_array = createBoids(number)

	## get goals in scene
	goals_array = getGoals()

	## randomize positions
	firstKeyframe(boids_array)

	## simulate keyframes
	simulateKeyframes(boids_array, goals_array)

	## play environment
	cmds.play()

createUI( 'BEZTBOIDZ', applyCallback )