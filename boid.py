import maya.cmds as cmds

class Boid(object):
	_name = "" 
	_position = [0, 0, 0]
	_velocity = [0, 0, 0]
	_scale = 1
	_obj = ""

	def __init__(self, order):
		self._name = "cube%s" % order
		self._obj = cmds.polyCone(constructionHistory=True, radius=2, height=5, n=self._name)

	def getPosition(self):
		return self._position

	def setPosition(self, position):
		self._position = position

	def setScale(self, scale):
		cmds.scale( scale, scale, scale, self._name )
		self._scale = scale;

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