from boid import *
from vec import *

def cohesionRule(currentBoidIndex, boids, NEIGHBOUR_DISTANCE):
	perceivedFlockCenter = [0, 0, 0]
	for index in range(len(boids)):              												   #for all the boids
        	if index != currentBoidIndex:  
                if(dist(currentBoidIndex, boids[index].getPosition()) < NEIGHBOUR_DISTANCE)                        									   #except the boid at hand
            	   perceivedFlockCenter = vec.add(perceivedFlockCenter, boids[index].getPosition())    #calculate the total pfc

	perceivedFlockCenter = perceivedFlockCenter/range(len(boids))						#Calculate avg pfc

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