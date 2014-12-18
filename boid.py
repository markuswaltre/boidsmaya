import maya.cmds as cmds

class Boid(object):
	_name = "" 
	_position = [0, 0, 0]
	_velocity = [0, 0, 0]
	_scale = 1
	_obj = ""
	_target = ""
	_positionTarget = [0, 0, 0]

	def __init__(self, order):
		self._name = "boid%s" % order

		# self._obj = cmds.polyCone(constructionHistory=True, radius=2, height=5, n=self._name)
		self._obj = cmds.polyCube(constructionHistory=True, width=2, height=2, n=self._name)
		self._target = cmds.polyCube(width=0.5, height=0.5, depth=0.5,  n="%starget" % self._name)

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

	def setTargetPosition(self, position):
		self._positionTarget = position

	def getTargetPosition(self):
		return self._positionTarget

	def getTarget(self):
		return self._target

	def hideTarget(self):
		cmds.hide( self._target )

	def getName(self):
		return self._name

	def getObj(self):
		return self._obj

	def setAim(self):
		cmds.aimConstraint(self._target, self._obj, aim=[0, 1, 0], u=[0, 1, 0], wu=[0, 1, 0], o=[0, 0, 0], wut='vector')

def make_boid(order):
	return Boid(order)
	