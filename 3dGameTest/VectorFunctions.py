# This class holds all of the functions to create unit direction vectors for a plane
# As well as other functions that involve vectors (like dot, cross, magnitudes)
import math


# Checks to see if a vector is all 0, returns 0 if its 0, 1 if its not
def isVector3Zero(vector):
    if vector[0] == 0:
        if vector[1] == 0:
            if vector[2] == 0:
                print("Vector is Zero")
                return True
    else:
        return False


# Checks if vector is in R3
def isVectorNotR3(vector):
    if len(vector) > 3:
        print("Vector larger than R3")
        return True
    if len(vector) < 3:
        print("Vector smaller than R3")
        return True
    else:
        return False


# Takes two vectors and dots them
# Used to find the projection of a point in R3 onto a planes directional vector
def projectVector3(vector1, vector2):
    if isVector3Zero(vector1):
        print("Can't dot zero vectors")
        return vector1
    if isVector3Zero(vector2):
        print("Can't dot zero vectors")
        return vector2
    x1 = vector1[0] * vector2[0]
    y1 = vector1[1] * vector2[1]
    z1 = vector1[2] * vector2[2]

    return x1 + y1 + z1


# Takes two vector and returns the unit of their cross product
def crossVector3(vector1, vector2):
    # Checks if vector1 or vector2 is zero
    if isVector3Zero(vector1):
        print("Can't cross zero vectors")
        return vector1
    if isVector3Zero(vector2):
        print("Can't cross zero vectors")
        return vector2
    if isVectorNotR3(vector1):
        print("Can't cross vectors not in R3")
        return vector1
    if isVectorNotR3(vector2):
        print("Can't cross vectors not in R3")
        return vector2
    # Does cross product operations
    x = (vector1[1]*vector2[2]) - (vector2[1]*vector1[2])
    y = (vector1[2]*vector2[0]) - (vector2[2]*vector1[0])
    z = (vector1[0]*vector2[1]) - (vector2[0]*vector1[1])
    # Returns the vector which is the result of the cross product
    return [x, y, z]


# Takes in a vector (size 3 array), and returns it normalized
def makeVector3Unit(vector):
    # Checks if vector is not in R3
    if isVectorNotR3(vector):
        print("Vector not in R3, can't normalize")
        return vector
    # Just return the zero vector if zeros are given
    if isVector3Zero(vector):
        print("Can't normalize zero vector")
        return vector
    # Calculates the magnitude of the vector
    magnitude = math.sqrt(vector[0]*vector[0] +
                          vector[1]*vector[1] +
                          vector[2] * vector[2])
    # Goes through and divides the vector by its magnitude
    for i in range(0, 3):
        vector[i] /= magnitude
    # Returns that vector
    return vector


# Returns the point (size 3 array, can be though of like a vector) for a given rho phi theta, typically the camera
# NOTE: Always use degrees for phi and theta
def pointIn3SpaceSpherical(rho, phi, theta):
    x = rho * math.sin(math.radians(phi)) * math.cos(math.radians(theta))
    y = rho * math.sin(math.radians(phi)) * math.sin(math.radians(theta))
    z = rho * math.cos(math.radians(phi))

    return [x, y, z]


# Takes spherical coordinate in degrees, and finds the normal vector to the sphere at that point, returns normalized
def makeUnitN3(rho, phi, theta):
    n = pointIn3SpaceSpherical(rho, phi, theta)
    N = makeVector3Unit(n)
    return N


# Takes spherical coordinates in degrees and find the vector what is -5 degrees phi from the normal vector
def makeUnitZ3(rho, phi, theta):
    z = pointIn3SpaceSpherical(rho, phi-5, theta)
    Z = makeVector3Unit(z)
    return Z


# Takes spherical coordinates in degrees and finds the unit directional vector
# This vector goes in the tangent planes "x" direction
def makeUnitU3(rho, phi, theta):
    N = makeUnitN3(rho, phi, theta)
    Z = makeUnitZ3(rho, phi, theta)
    u = crossVector3(Z, N)
    U = makeVector3Unit(u)
    return U


# Takes spherical coordinates in degrees and finds the unit directional vector
# This vector goes in the tangent planes "y" direction
def makeUnitV3(rho, phi, theta):
    N = makeUnitN3(rho, phi, theta)
    U = makeUnitU3(rho, phi, theta)
    v = crossVector3(N, U)
    V = makeVector3Unit(v)
    return V


# Takes spherical coordinates in degrees and gives the two directional vectors which describe the plane at the point
def findDirectionlVectorToCamera(rho, phi, theta):
    U = makeUnitU3(rho, phi, theta)
    V = makeUnitV3(rho, phi, theta)
    return [U, V]
