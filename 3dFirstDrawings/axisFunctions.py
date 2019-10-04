# this is where I have the functions for drawing the axis
import vectorFunctions as vecFunc

# holds info for the planes
planeLength = 600
xAxis = [[planeLength / 2, 0, 0], [-(planeLength / 2), 0, 0]]
yAxis = [[0, planeLength / 2, 0], [0, -(planeLength / 2), 0]]
zAxis = [[0, 0, planeLength / 2], [0, 0, -(planeLength / 2)]]

# draws the coordinate planes
def drawCoordinatePlanes(rho, phi, theta, pen):
    # creates the vectors for projection
    N = vecFunc.makeUnitN(rho, phi, theta)
    Z = vecFunc.makeUnitZ(rho, phi, theta)
    U = vecFunc.makeUnitU(Z, N)
    V = vecFunc.makeUnitV(N, U)

    # draws the respective axis
    pen.color("green")
    pen.up()
    pen.goto(vecFunc.scalarProjection(U, xAxis[0]), vecFunc.scalarProjection(V, xAxis[0]))
    pen.write("X", False, "right")
    pen.down()
    pen.goto(vecFunc.scalarProjection(U, xAxis[1]), vecFunc.scalarProjection(V, xAxis[1]))
    pen.up()
    pen.write("-X", False, "right")

    pen.color("white")
    pen.goto(vecFunc.scalarProjection(U, yAxis[0]), vecFunc.scalarProjection(V, yAxis[0]))
    pen.write("Y", False, "right")
    pen.down()
    pen.goto(vecFunc.scalarProjection(U, yAxis[1]), vecFunc.scalarProjection(V, yAxis[1]))
    pen.up()
    pen.write("-Y", False, "right")

    pen.color("hot pink")
    pen.goto(vecFunc.scalarProjection(U, zAxis[0]), vecFunc.scalarProjection(V, zAxis[0]))
    pen.write("Z", False, "right")
    pen.down()
    pen.goto(vecFunc.scalarProjection(U, zAxis[1]), vecFunc.scalarProjection(V, zAxis[1]))
    pen.up()
    pen.write("-Z", False, "right")

