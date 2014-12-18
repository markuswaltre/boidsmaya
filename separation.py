from vec import *
from boid import *

def calculateSeparation(currentBoidIndex, boids, NEIGHBOR_DISTANCE):
	neighbors = []
	currentBoidPos = boids[currentBoidIndex].getPosition()
	WHEIGHT = 1#0.06
	separationVector = [0,0,0]

	for index in range(len(boids)):
		if(index != currentBoidIndex):
			if(dist(currentBoidPos, boids[index].getPosition()) < NEIGHBOR_DISTANCE):
				neighbors.append(boids[index].getPosition())

	numberOfNeighbors = len(neighbors)

	if(numberOfNeighbors > 0):
		for neighborPos in neighbors:
			temp = sub(currentBoidPos, neighborPos)
			separationVector = add(separationVector, temp)

		separationVector = scale_by_scalar(separationVector, WHEIGHT)

	return separationVector
		