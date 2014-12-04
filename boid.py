import maya.cmds as cmds

class Boid(object):
	_name = "" 
	_position = [0, 0, 0]
	_velocity = [0, 0, 0]
	_obj = ""

	def __init__(self, order):
		self._name = "cube%s" % order
		self._obj = cmds.polyCube(constructionHistory=True, width=1, height=1, depth=1, n=self._name)

	def getPosition(self):
		return self._position

	def setPosition(self, position):
		self._position = position

	def getVelocity(self):
		return self._velocity

	def setVelocity(self, velocity):
		self._velocity = velocity

	def getName(self):
		return self._name

	def getObj(self):
		return self._obj

def make_boid(order):
	return Boid(order)