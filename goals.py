from vec import *
import maya.cmds as cmds

class Goals(object):
	_goal_index = 0

	def getGoals(self):
		goals = []

		if len(cmds.ls('goal*', r=True)) > 0:
			cmds.select('goal*', r=True)
			selected = cmds.ls(sl=True)
			for item in range(len(selected)/2): 
				x = cmds.getAttr("%s.translateX" % selected[item])
				y = cmds.getAttr("%s.translateY" % selected[item])
				z = cmds.getAttr("%s.translateZ" % selected[item])
				pos = [x,y,z]
				goals.append(pos)

		return goals

	def calculateGoal(self, currentPosition, goals_array):
		goal_index = self._goal_index

		if(dist(currentPosition, goals_array[goal_index]) < 5):
			goal_index = goal_index + 1

			if (goal_index == len(goals_array)):
				goal_index = 0

		goalVelocity = sub(goals_array[goal_index], currentPosition)
		goalVelocity = norm(goalVelocity)
		goalVelocity = scale_by_scalar(goalVelocity, 0.7)

		self._goal_index = goal_index

		return goalVelocity