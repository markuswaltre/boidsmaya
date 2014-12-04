import maya.cmds as cmds
import random
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

class Boid(object):
	_name = "" 
	_position = [0, 0, 0]
	_velocity = [0, 0, 0]

	def __init__(self, order):
		self._name = "cube%s" % order
		cmds.polyCube(constructionHistory=True, width=1, height=1, depth=1, n=self._name)

	def getPosition(self):
		return self._position

	def setPosition(self, position):
		self._position = position

	def getVelocity(self):
		return _velocity

	def setVelocity(self, velocity):
		self._velocity = velocity

	def getName(self):
		return self._name

def make_boid(order):
	return Boid(order)

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

def deleteAllObjects():
	cmds.select( all=True )
	cmds.delete()

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
	# createObjects()
	# simulate()
	x = make_boid(0)
	y = make_boid(1)
	y.setPosition([1, 1, 1])
	print x.getPosition()
	print y.getPosition()

	print dist(x.getPosition(), y.getPosition())
	cmds.play()

