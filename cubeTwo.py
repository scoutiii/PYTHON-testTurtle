# this is where I am storing my functions for drawing cubes
import math
import pointPlanePairs as classes
import vectorFunctions as vecFunc

# holds the coordinate points for each side of a cube
cubeSize = 100
cubeGap = 10
differential = 150
squareTop = [[-cubeSize + differential, -cubeSize+differential, (cubeSize + cubeGap)+differential],
             [cubeSize+differential, -cubeSize+differential, (cubeSize + cubeGap)+differential],
             [cubeSize+differential, cubeSize+differential, (cubeSize + cubeGap)+differential],
             [-cubeSize+differential, cubeSize+differential, (cubeSize + cubeGap)+differential]]
squareFront = [[(cubeSize + cubeGap)+differential, -cubeSize+differential, cubeSize+differential],
               [(cubeSize + cubeGap)+differential, -cubeSize+differential, -cubeSize+differential],
               [(cubeSize + cubeGap)+differential, cubeSize+differential, -cubeSize+differential],
               [(cubeSize + cubeGap)+differential, cubeSize+differential, cubeSize+differential]]
squareRight = [[cubeSize+differential, (cubeSize + cubeGap)+differential, cubeSize+differential],
               [cubeSize+differential, (cubeSize + cubeGap)+differential, -cubeSize+differential],
               [-cubeSize+differential, (cubeSize + cubeGap)+differential, -cubeSize+differential],
               [-cubeSize+differential, (cubeSize + cubeGap)+differential, cubeSize+differential]]
squareBack = [[-(cubeSize + cubeGap)+differential, cubeSize+differential, cubeSize+differential],
              [-(cubeSize + cubeGap)+differential, cubeSize+differential, -cubeSize+differential],
              [-(cubeSize + cubeGap)+differential, -cubeSize+differential, -cubeSize+differential],
              [-(cubeSize + cubeGap)+differential, -cubeSize+differential, cubeSize+differential]]
squareLeft = [[-cubeSize+differential, -(cubeSize + cubeGap)+differential, cubeSize+differential],
              [-cubeSize+differential, -(cubeSize + cubeGap)+differential, -cubeSize+differential],
              [cubeSize+differential, -(cubeSize + cubeGap)+differential, -cubeSize+differential],
              [cubeSize+differential, -(cubeSize + cubeGap)+differential, cubeSize+differential]]
squareBottom = [[cubeSize+differential, cubeSize+differential, -(cubeSize + cubeGap)+differential],
                [-cubeSize+differential, cubeSize+differential, -(cubeSize + cubeGap)+differential],
                [-cubeSize+differential, -cubeSize+differential, -(cubeSize + cubeGap)+differential],
                [cubeSize+differential, -cubeSize+differential, -(cubeSize + cubeGap)+differential]]


# function which will draw a given side and fill it in
def drawCubeSidesFilled(squarePoints, U, V, pen, color):
    pen.up()
    pen.color(color)
    pen.begin_fill()
    pen.goto(vecFunc.scalarProjection(U, squarePoints[0]), vecFunc.scalarProjection(V, squarePoints[0]))
    pen.down()
    pen.goto(vecFunc.scalarProjection(U, squarePoints[1]), vecFunc.scalarProjection(V, squarePoints[1]))
    pen.goto(vecFunc.scalarProjection(U, squarePoints[2]), vecFunc.scalarProjection(V, squarePoints[2]))
    pen.goto(vecFunc.scalarProjection(U, squarePoints[3]), vecFunc.scalarProjection(V, squarePoints[3]))
    pen.goto(vecFunc.scalarProjection(U, squarePoints[0]), vecFunc.scalarProjection(V, squarePoints[0]))
    pen.end_fill()
    pen.up()


# draws a cube side but not fill it in
def drawCubeSidesUnFilled(squarePoints, U, V, pen, color):
    pen.up()
    pen.color(color)

    pen.goto(vecFunc.scalarProjection(U, squarePoints[0]), vecFunc.scalarProjection(V, squarePoints[0]))
    pen.down()
    pen.goto(vecFunc.scalarProjection(U, squarePoints[1]), vecFunc.scalarProjection(V, squarePoints[1]))
    pen.goto(vecFunc.scalarProjection(U, squarePoints[2]), vecFunc.scalarProjection(V, squarePoints[2]))
    pen.goto(vecFunc.scalarProjection(U, squarePoints[3]), vecFunc.scalarProjection(V, squarePoints[3]))
    pen.goto(vecFunc.scalarProjection(U, squarePoints[0]), vecFunc.scalarProjection(V, squarePoints[0]))

    pen.up()


# finds the distance from a point to another point
def distanceFromPoint(centerPoinnt, outsidePoint):
    x = centerPoinnt[0] - outsidePoint[0]
    y = centerPoinnt[1] - outsidePoint[1]
    z = centerPoinnt[2] - centerPoinnt[2]

    magnitude = math.sqrt((x * x) + (y * y) + (z * z))

    return magnitude


# finds the distances from all points on a side from a give point
def distanceFromCubeSide(centerPoint, cubeSide, color):
    distPlanArray = []
    for i in range(0, 4):
        dist = distanceFromPoint(centerPoint, cubeSide[i])
        obj = classes.pointPlanePairs(dist, cubeSide, color)
        distPlanArray.append(obj)
    return distPlanArray.sort(reverse=False, key=sortOrder)


# to help sort all of the distances
def sortOrder(obj):
    return obj.whatIsDistance()


def averagePlanePoint(plane):
    x = [plane[0][0], plane[1][0], plane[2][0], plane[3][0]]
    y = [plane[0][1], plane[1][1], plane[2][1], plane[3][1]]
    z = [plane[0][2], plane[1][2], plane[2][2], plane[3][2]]

    xSum = x[0] + x[1] + x[2] + x[3]
    ySum = y[0] + y[1] + y[2] + y[3]
    zSum = z[0] + z[1] + z[2] + z[3]

    return [xSum / 4, ySum / 4, zSum / 4]


# draws the whole cube given its various states
def drawCube(rho, phi, theta, pen, fillState):
    # creates the vectors for projection
    N = vecFunc.makeUnitN(rho, phi, theta)
    Z = vecFunc.makeUnitZ(rho, phi, theta)
    U = vecFunc.makeUnitU(Z, N)
    V = vecFunc.makeUnitV(N, U)
    point = vecFunc.makeCameraPoint(rho, phi, theta)



    squareTopSingle = classes.pointPlanePairs(distanceFromPoint(point, averagePlanePoint(squareTop)), squareTop, "red")
    squareFrontSingle = classes.pointPlanePairs(distanceFromPoint(point, averagePlanePoint(squareFront)), squareFront, "orange")
    squareRightSingle = classes.pointPlanePairs(distanceFromPoint(point, averagePlanePoint(squareRight)), squareRight, "yellow")
    squareBackSingle = classes.pointPlanePairs(distanceFromPoint(point, averagePlanePoint(squareBack)), squareBack, "lime green")
    squareLeftSingle = classes.pointPlanePairs(distanceFromPoint(point, averagePlanePoint(squareLeft)), squareLeft, "blue")
    squareBottomSingle = classes.pointPlanePairs(distanceFromPoint(point, averagePlanePoint(squareBottom)), squareBottom, "purple")

    cubeSideDistances = [squareTopSingle,
                         squareFrontSingle,
                         squareRightSingle,
                         squareBackSingle,
                         squareLeftSingle,
                         squareBottomSingle]
    cubeSideDistances.sort(reverse=True, key=sortOrder)

    for plane in cubeSideDistances:
        if fillState % 2 == 0:
            drawCubeSidesFilled(plane.whatIsPlane(), U, V, pen, plane.whatIsColor())
        else:
            drawCubeSidesUnFilled(plane.whatIsPlane(), U, V, pen, plane.whatIsColor())



    # # gets all of the distances from the camera point
    # planeDists1 = distanceFromCubeSide(point, squareTop, "red")
    # planeDists2 = distanceFromCubeSide(point, squareFront, "orange")
    # planeDists3 = distanceFromCubeSide(point, squareRight, "yellow")
    # planeDists4 = distanceFromCubeSide(point, squareBack, "lime green")
    # planeDists5 = distanceFromCubeSide(point, squareLeft, "blue")
    # planeDists6 = distanceFromCubeSide(point, squareBottom, "violet")
    # # adds all the distances to one array
    # allDistances = planeDists1 + planeDists2 + planeDists3 + planeDists4 + planeDists5 + planeDists6
    # allDistances.sort(reverse=True, key=sortOrder)
    #
    # closestPlanes = []
    #
    # for i in allDistances:
    #     closestPlanes.append(i)
    #     for j in allDistances:
    #         if j.whatIsPlane() == i.whatIsPlane():
    #             closestPlanes.append(j)
    #             allDistances.remove(j)
    #
    # farthestPlanes = allDistances
    # farthestPlanes.sort(reverse=False, key=sortOrder)
    #
    #
    # # goes through at draws the cube from back to front (likely to change how this works)
    # for plane in farthestPlanes:
    #     if fillState % 2 == 0:
    #         drawCubeSidesFilled(plane.whatIsPlane(), U, V, pen, plane.whatIsColor())
    #     else:
    #         drawCubeSidesUnFilled(plane.whatIsPlane(), U, V, pen, plane.whatIsColor())
    #     for i in farthestPlanes:
    #         if i.whatIsPlane() == plane.whatIsPlane():
    #             farthestPlanes.remove(i)
    #
    # for plane in closestPlanes:
    #     if fillState % 2 == 0:
    #         drawCubeSidesFilled(plane.whatIsPlane(), U, V, pen, plane.whatIsColor())
    #     else:
    #         drawCubeSidesUnFilled(plane.whatIsPlane(), U, V, pen, plane.whatIsColor())
    #     for i in closestPlanes:
    #         if i.whatIsPlane() == plane.whatIsPlane():
    #             closestPlanes.remove(i)
