import math

# takes a vector and returns its unit vector
# I think this might be broken, not sure...
def makeVectorUnit(vector):
    magnitude = math.sqrt((vector[0] * vector[0])
                          + (vector[1] * vector[1])
                          + (vector[2] + vector[2]))
    unitVector = [vector[0] / magnitude, vector[1] / magnitude, vector[2] / magnitude]

    return unitVector


# uses the spherical coordinates to create a normal vector to the sphere
def makeUnitN (rho, phi, theta):
    x = rho * math.sin(math.radians(phi)) * math.cos(math.radians(theta))
    y = rho * math.sin(math.radians(phi)) * math.sin(math.radians(theta))
    z = rho * math.cos(math.radians(phi))

    N = [x, y, z]
    magnitue = math.sqrt((N[0] * N[0]) + (N[1] * N[1]) + (N[2] * N[2]))
    N[0] /= magnitue
    N[1] /= magnitue
    N[2] /= magnitue
    return N


# uses the spherical coordinates to make the point on the sphere where the camera is
def makeCameraPoint(rho, phi, theta):
    x = rho * math.sin(math.radians(phi)) * math.cos(math.radians(theta))
    y = rho * math.sin(math.radians(phi)) * math.sin(math.radians(theta))
    z = rho * math.cos(math.radians(phi))

    point = [x, y, z]

    return point


# makes a vector that is -5 phi from the normal vector
def makeUnitZ (rho, phi, theta):
    x = rho * math.sin(math.radians(phi - 5)) * math.cos(math.radians(theta))
    y = rho * math.sin(math.radians(phi - 5)) * math.sin(math.radians(theta))
    z = rho * math.cos(math.radians(phi - 5))

    Z = [x, y, z]
    magnitude = math.sqrt((Z[0] * Z[0]) + (Z[1] * Z[1]) + (Z[2] * Z[2]))
    Z[0] /= magnitude
    Z[1] /= magnitude
    Z[2] /= magnitude
    return Z


# crosses two vectors, doesn't normalize
def crossVectorsUnit (vector1, vector2):
    x = (vector1[1] * vector2[2]) - (vector1[2] * vector2[1])
    y = (vector1[2] * vector2[0]) - (vector1[0] * vector2[2])
    z = (vector1[0] * vector2[1]) - (vector1[1] * vector2[0])

    newVector = [x, y, z]

    return newVector


# makes a unit vector U which represents the X axis
def makeUnitU(Z, N):
    U = crossVectorsUnit(Z, N)
    magnitude = math.sqrt((U[0] * U[0]) + (U[1] * U[1]) + (U[2] * U[2]))
    U[0] /= magnitude
    U[1] /= magnitude
    U[2] /= magnitude
    return U


# makes a unit vector V which represents the Y axis
def makeUnitV(N, U):
    V = crossVectorsUnit(N, U)
    magnitued = math.sqrt((V[0] * V[0]) + (V[1] * V[1]) + (V[2] * V[2]))
    V[0] /= magnitued
    V[1] /= magnitued
    V[2] /= magnitued
    return V


# gets the scalar component of one vector in the direction of the other
def scalarProjection(planeVector, pointVector):
    x1 = planeVector[0] * pointVector[0]
    y1 = planeVector[1] * pointVector[1]
    z1 = planeVector[2] * pointVector[2]

    return x1 + y1 + z1
