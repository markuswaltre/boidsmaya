from vec import *
from boid import *

def calculateAlignment(currentBoidIndex, boids, NEIGHBOR_DISTANCE):
	neighbors = []
	alignmentVector = [0, 0, 0]
	currentBoidPos = boids[currentBoidIndex].getPosition()

	for index in range(len(boids)):
		if(index != currentBoidIndex):
			if(dist(currentBoidPos, boids[index].getPosition()) < NEIGHBOR_DISTANCE):
				neighbors.append(boids[index])

	numberOfNeighbors = len(neighbors)

	for neighbor in neighbors:
		temp = [0, 0, 0]
		temp = add(temp, neighbor.getVelocity())
		temp = div_by_scalar(temp, numberOfNeighbors)
		alignmentVector = add(alignmentVector, temp)

	return alignmentVector

