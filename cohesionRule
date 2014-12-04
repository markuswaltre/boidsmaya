from boid import *
from vec import *

def cohesionRule(currentBoid, allBoids):
	perceivedFlockCenter = [0, 0, 0]
	for b in range(objects):              												#for all the boids
        	if b != allBoids:                          									#except the boid at hand
            	perceivedFlockCenter = vec.add(perceivedFlockCenter, boids_array[b].getPosition())  	#calculate the total pfc

	perceivedFlockCenter = perceivedFlockCenter/(range(objects)							#Calculate avg pfc

    vel = vec.sub(perceivedFlockCenter, currentBoid)*0.95;

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