from vec import *
from boid import *

def calculateAlignment(currentBoidIndex, boids, NEIGHBOR_DISTANCE):
	neighbors = []
	currentBoidPos = boids[currentBoidIndex].getPosition()
	avgVelocity = [0, 0, 0]
	WHEIGHT = 0.2

	for index in range(len(boids)):
		if(index != currentBoidIndex):
			if(dist(currentBoidPos, boids[index].getPosition()) < NEIGHBOR_DISTANCE):
				neighbors.append(boids[index])

	numberOfNeighbors = len(neighbors)

	if(numberOfNeighbors > 0):
		for neighbor in neighbors:
			avgVelocity = add(avgVelocity, neighbor.getVelocity())

		avgVelocity = scale_by_scalar(avgVelocity, WHEIGHT)

	return avgVelocity

