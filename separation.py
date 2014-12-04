#Author Tobias Palmér
#Date: 2014-12-04

#Returns the calculated separation vector for the current boid

from vec import *
from boid import *

def calculateSeparation(currentBoidIndex, allBoids):
	neghborBoids = []
	currentBoidPos = allBoids[currentBoidIndex].getPosition()
	separationVector = [0,0,0]

	for index in allBoids.len()
		if(index != currentBoidIndex)
			if(dist(currentBoidPos , allBoids[index].getPosition()) < neighborDistance)
				neghborBoids.append(allBoids[index].getPosition())

	for neighborPos in neghborBoids
		temp = sub(currentBoidPos, neighborPos)
		temp = scale_by_scalar(temp,-1)
		separationVector = add(separationVector,temp)

	return separationVector
		