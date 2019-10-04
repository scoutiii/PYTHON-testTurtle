# This class holds everything for the wall tiles
import VectorFunctions as vecFunc
import math


class WallTile:
    # Sets defaults for the wall objects
    def __init__(self, sideLength=100, centerPoint3=(0, 0, 0), edgeColor=(0, 0, 0), fillColor=(0, 0, 0), fill=True, side=1):
        self.fill = fill
        self.walkable = False
        # Can't have length that is zero
        if sideLength == 0:
            self.sideLength = 100
        else:
            self.sideLength = sideLength

        # No real restrictions on where the center point can go
        self.centerPoint = centerPoint3

        # Makes sure that the values for edge color are between 0 and 255
        if edgeColor[0] > 255 or edgeColor[0] < 0:
            self.edgeColor[0] = 0
        if edgeColor[1] > 255 or edgeColor[1] < 0:
            self.edgeColor[1] = 0
        if edgeColor[2] > 255 or edgeColor[2] < 0:
            self.edgeColor[2] = 0
        else:
            self.edgeColor = edgeColor

        # Same as above but for the fill color
        if fillColor[0] > 255 or edgeColor[0] < 0:
            self.fillColor[0] = 0
        if fillColor[1] > 255 or edgeColor[1] < 0:
            self.fillColor[1] = 0
        if fillColor[2] > 255 or edgeColor[2] < 0:
            self.fillColor[2] = 0
        else:
            self.fillColor = fillColor

        # sets the wall side
        # 1=+x, 2=+y, 3=-x, 4=-y
        if side < 1 or side > 4:
            self.side = 1
        else:
            self.side = side

        # Sets the points according to the sides
        # 1 gives positive x
        if self.side == 1:
            self.p1 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p2 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p3 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2])]
            self.p4 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2])]
        # 2 gives positive y
        elif self.side == 2:
            self.p1 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p2 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p3 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2])]
            self.p4 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2])]
        # 3 gives negative x
        elif self.side == 3:
            self.p1 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p2 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p3 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] + self.sideLength / 2),
                       (self.centerPoint[2])]
            self.p4 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2])]
        # 4 gives negative y
        else:
            self.p1 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p2 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2] + self.sideLength)]
            self.p3 = [(self.centerPoint[0] - self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2])]
            self.p4 = [(self.centerPoint[0] + self.sideLength / 2),
                       (self.centerPoint[1] - self.sideLength / 2),
                       (self.centerPoint[2])]

        # Puts all the points into an array
        self.cornerPoints = [self.p1, self.p2, self.p3, self.p4]

    def drawObject(self, rho, phi, theta, pen):
        if self.fill:
            # Creates the U and V directional vectors for the normal plane to the camera
            uAndV = vecFunc.findDirectionlVectorToCamera(rho, phi, theta)
            pen.up()
            pen.pencolor(self.edgeColor)
            pen.fillcolor(self.fillColor)
            pen.begin_fill()

            # Starts drawing using the projections of each point onto the directional vectors
            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[0]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[0]))
            pen.down()
            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[1]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[1]))

            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[2]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[2]))

            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[3]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[3]))

            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[0]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[0]))

            pen.end_fill()
            pen.up()
        else:
            # Creates the U and V directional vectors for the normal plane to the camera
            uAndV = vecFunc.findDirectionlVectorToCamera(rho, phi, theta)
            pen.up()
            pen.pencolor(self.edgeColor)

            # Starts drawing using the projections of each point onto the directional vectors
            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[0]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[0]))
            pen.down()
            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[1]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[1]))

            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[2]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[2]))

            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[3]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[3]))

            pen.goto(vecFunc.projectVector3(uAndV[0], self.cornerPoints[0]),
                     vecFunc.projectVector3(uAndV[1], self.cornerPoints[0]))

            pen.up()

    # Takes a point in r3, and finds the distance from the wall to that point
    def getDistance(self, distances=(0, 0, 0)):
        if self.side == 1:
            x = distances[0] - (self.centerPoint[0] + (self.sideLength / 2))
            y = distances[1] - (self.centerPoint[1])
            z = distances[2] - (self.centerPoint[2])
            return math.sqrt((x * x) + (y * y) + (z * z))
        elif self.side == 2:
            x = distances[0] - (self.centerPoint[0])
            y = distances[1] - (self.centerPoint[1] + (self.sideLength / 2))
            z = distances[2] - (self.centerPoint[2])
            return math.sqrt((x * x) + (y * y) + (z * z))
        elif self.side == 3:
            x = distances[0] - (self.centerPoint[0] - (self.sideLength / 2))
            y = distances[1] - (self.centerPoint[1])
            z = distances[2] - (self.centerPoint[2])
            return math.sqrt((x * x) + (y * y) + (z * z))
        else:
            x = distances[0] - (self.centerPoint[0])
            y = distances[1] - (self.centerPoint[1] - (self.sideLength / 2))
            z = distances[2] - (self.centerPoint[2])
            return math.sqrt((x * x) + (y * y) + (z * z))

    def isWalkable(self):
        return self.walkable
