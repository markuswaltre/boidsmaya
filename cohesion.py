from boid import *
from vec import *

def calculateCohesion(currentBoidIndex, boids, NEIGHBOUR_DISTANCE):
	perceivedFlockCenter = [0, 0, 0]
    numberOfNeighbours = 0

	for index in range(len(boids)):  
        #skip the current boid            												       
    	if index != currentBoidIndex:  
            #and the boids not in range
            if(dist(currentBoidIndex, boids[index].getPosition()) < NEIGHBOUR_DISTANCE)               
               #then calculate the total pfc
        	   perceivedFlockCenter = vec.add(perceivedFlockCenter, boids[index].getPosition())       
               numberOfNeighbours += 1
    
    #Calculate avg pfc
	perceivedFlockCenter = vec.divide_by_scalar(perceivedFlockCenter,numberOfNeighbours)						      

    vel = boids[currentBoidIndex] + vec.sub(perceivedFlockCenter, boids[currentBoidIndex])*0.95;

	#nudge the boid in the correct direction toward the pfc 
    # if perceivedFlockCenter[0] > currentBoid.getPosition()[0]:
    #     perceivedFlockCenter[0] = (perceivedFlockCenter[0] - currentBoid.getPosition()[0])*(0.95)
    # if perceivedFlockCenter[0] < currentBoid.getPosition()[0]:
    #     perceivedFlockCenter[0] = (currentBoid[0] - perceivedFlockCenter[0])*(-0.95)
    # if perceivedFlockCenter[1] > currentBoid.getPosition()[1]:
    #     perceivedFlockCenter[1] = (perceivedFlockCenter[1] - currentBoid.getPosition()[1])*(0.95)
    # if perceivedFlockCenter[1] < currentBoid.getPosition()[1]:
    #     perceivedFlockCenter[1] = (currentBoid.getPosition()[1] - perceivedFlockCenter[1])*(-0.95)
    # if perceivedFlockCenter[2] > currentBoid.getPosition()[2]:
    #     perceivedFlockCenter[2] = (perceivedFlockCenter[2] - currentBoid.getPosition()[2])*(0.95)
    # if perceivedFlockCenter[2] < currentBoid.getPosition()[2]:
    #     perceivedFlockCenter[2] = (currentBoid.getPosition()[2] - perceivedFlockCenter[2])*(-0.95)

    return vel 