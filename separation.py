from vec import *
from boid import *

def calculateSeparation(currentBoidIndex, boids, NEIGHBOR_DISTANCE):
	neighbors = []
	currentBoidPos = boids[currentBoidIndex].getPosition()
	separationVector = [0,0,0]

	for index in range(len(boids)):
		if(index != currentBoidIndex):
			if(dist(currentBoidPos, boids[index].getPosition()) < NEIGHBOR_DISTANCE):
				neighbors.append(boids[index].getPosition())

	for neighborPos in neighbors:
		temp = sub(currentBoidPos, neighborPos)
		temp = scale_by_scalar(temp, -1)
		separationVector = add(separationVector, temp)

	return separationVector
		