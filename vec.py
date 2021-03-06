import math

def add(u, v):    
	return [a + b for a, b in zip(u, v)]

def sub(u, v):
	return [a - b for a, b in zip(u, v)]

def eq(u, v):
	return all([a == b for a, b in zip(u, v)])

def length_squared(u):
	return sum([a ** 2 for a in u])

def length(u):
	return math.sqrt(length_squared(u))

def scale(u, v):
	return [a * b for a, b in zip(u, v)]

def div_by_scalar(u, scalar):
	return [u[0]/float(scalar), u[1]/float(scalar), u[2]/float(scalar)]

def scale_by_scalar(u, scalar):
	return [a * scalar for a in u]

def dist(u, v):
	return length(sub(v, u))

def dist_squared(u, v):
	return length_squared(sub(v, u))

def setlength(u, l):
	return scale_by_scalar(u, l / length(u))

def norm(u):
	return setlength(u, 1)

def dotproduct(u, v):
  return sum((a*b) for a, b in zip(u, v))

def angle(u, v):
  return math.acos(dotproduct(u, v) / (length(u) * length(v)))