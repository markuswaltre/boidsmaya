from boid import *
from vec import *

def calculateCohesion(currentBoidIndex, boids, NEIGHBOUR_DISTANCE):
	perceivedFlockCenter = [0, 0, 0]
	numberOfNeighbours = 0
	WHEIGHT = 0.2

	for index in range(len(boids)):
		#skip the current boid            												       
		if index != currentBoidIndex:
			#and the boids not in range
			if(dist(boids[currentBoidIndex].getPosition(), boids[index].getPosition()) < NEIGHBOUR_DISTANCE):
				#then calculate the total pfc
				perceivedFlockCenter = add(perceivedFlockCenter, boids[index].getPosition())
				numberOfNeighbours = numberOfNeighbours + 1
	
	#Calculate avg pfc
	if(numberOfNeighbours > 0):
		perceivedFlockCenter = div_by_scalar(perceivedFlockCenter, numberOfNeighbours)	
		direction = sub(perceivedFlockCenter, boids[currentBoidIndex].getPosition())
		direction = scale_by_scalar(direction, WHEIGHT)
	else:
		direction = [0, 0, 0]
		
	return direction 