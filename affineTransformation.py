import turtle
import math

window = turtle.Screen()
pen = turtle.Turtle()
window.screensize(10000, 10000)
window.setworldcoordinates(-500, -500, 500, 500)
window.bgcolor("black")
pen.color("green")
pen.pensize(.000001)
pen.shape("blank")
pen.speed(100000)

pen2 = turtle.Turtle()
pen2.color("green")
pen2.pensize(.000001)
pen2.shape("blank")
pen2.speed(100000)

penX = turtle.Turtle()
penX.color("white")
penX.pensize(1)
penX.shape("blank")
penX.speed(100000)

penY = turtle.Turtle()
penY.color("green")
penY.pensize(.000001)
penY.shape("blank")
penY.speed(100000)

def drawCoordinatePlane():
    pen.up()
    pen.goto(-500, 0)
    pen.setheading(0)
    pen.down()
    pen.forward(1000)
    pen.up()
    pen.goto(0, 500)
    pen.setheading(270)
    pen.down()
    pen.forward(1000)


def affineTransformX(a, b, c, d, e, f, x, y):
    return (a * x) + (b * y) + e


def affineTransformY(a, b, c, d, e, f, x, y):
    return (c * x) + (d * y) + f


#drawCoordinatePlane()

squareTopX = []
squareTopY = []
squareBottomX = []
squareBottomY = []
squareLeftX = []
squareLeftY = []
squareRightX = []
squareRightY = []

for x in range(-250, 250, 4):
    squareTopX.insert(x + 250, x)
    squareBottomX.insert(x + 250, x)
    squareLeftX.insert(x + 250, - 250)
    squareRightX.insert(x + 250, 250)

for y in range(-250, 250, 4):
    squareTopY.insert(y + 250, 250)
    squareBottomY.insert(y + 250, -250)
    squareLeftY.insert(y + 250, y)
    squareRightY.insert(y + 250, y)

pen.up()

# for i in range(0, len(squareTopX)):
#     pen.goto(squareTopX[i], squareTopY[i])
#     pen.dot()
#     pen.goto(squareBottomX[i], squareBottomY[i])
#     pen.dot()
#     pen.goto(squareLeftX[i], squareLeftY[i])
#     pen.dot()
#     pen.goto(squareRightX[i], squareRightY[i])
#     pen.dot()

pen.color("white")

# a = 1/2
# b = 0
# c = 0
# d = 1/2
# e = 250
# f = 250
# for i in range(0, len(squareTopX), 2):
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareTopX[i], squareTopY[i]),
#              affineTransformY(a, b, c, d, e, f, squareTopX[i], squareTopY[i]))
#     pen.dot()
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareBottomX[i], squareBottomY[i]),
#              affineTransformY(a, b, c, d, e, f, squareBottomX[i], squareBottomY[i]))
#     pen.dot()
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareLeftX[i], squareLeftY[i]),
#              affineTransformY(a, b, c, d, e, f, squareLeftX[i], squareLeftY[i]))
#     pen.dot()
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareRightX[i], squareRightY[i]),
#              affineTransformY(a, b, c, d, e, f, squareRightX[i], squareRightY[i]))
#     pen.dot()
#
a = 1 * math.cos(math.pi/4)
b = 1 * math.sin(math.pi/4)
c = 1 * math.sin(math.pi/4)
d = 0 * math.cos(math.pi/4)
e = 0
f = 0
#
# for i in range(0, len(squareTopX)):
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareTopX[i], squareTopY[i]),
#              affineTransformY(a, b, c, d, e, f, squareTopX[i], squareTopY[i]))
#     pen.dot()
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareBottomX[i], squareBottomY[i]),
#              affineTransformY(a, b, c, d, e, f, squareBottomX[i], squareBottomY[i]))
#     pen.dot()
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareLeftX[i], squareLeftY[i]),
#              affineTransformY(a, b, c, d, e, f, squareLeftX[i], squareLeftY[i]))
#     pen.dot()
#     pen.goto(affineTransformX(a, b, c, d, e, f, squareRightX[i], squareRightY[i]),
#              affineTransformY(a, b, c, d, e, f, squareRightX[i], squareRightY[i]))
#     pen.dot()

topLeftCornerX = -250
topLeftCornerY = 250
topRightCornerX = 250
topRightCornerY = 250
bottomLeftCornerX = -250
bottomLeftCornerY = -250
bottomRightCornerX = 250
bottomRightCornerY = -250

# pen.goto(topLeftCornerX, topLeftCornerY)
# pen.down()
# pen.goto(topRightCornerX, topRightCornerY)
# pen.goto(bottomRightCornerX, bottomRightCornerY)
# pen.goto(bottomLeftCornerX, bottomLeftCornerY)
# pen.goto(topLeftCornerX, topLeftCornerY)

pen.up()
pen2.up()
penX.up()
penY.up()

yAxisBottom = -5000
yAxisTop = 5000
xAxisLeft = -5000
xAxisRight = 5000

step = 5
rotationDegree = 0

for degree in range(0, 360 * 100, step):
    a = 2 * math.cos(math.radians(degree)*0) * math.cos(math.radians(rotationDegree))  # should cause a rotation around the y axis
    b = 2 * math.sin(math.radians(degree)*0) * -1 * math.sin(math.radians(rotationDegree))
    c = 2 * math.sin(math.radians(degree)) * math.sin(math.radians(rotationDegree))
    d = 2 * math.cos(math.radians(degree)) * math.cos(math.radians(rotationDegree))  # should cause a rotation around the x axis
    e = 0
    f = 0

    if degree % 360 == 0:
        rotationDegree += 10

    penX.goto(affineTransformX(a, b, c, d, e, f, xAxisLeft, 0), affineTransformY(a, b, c, d, e, f, xAxisLeft, 0))
    penX.down()
    penX.goto(affineTransformX(a, b, c, d, e, f, xAxisRight, 0), affineTransformY(a, b, c, d, e, f, xAxisRight, 0))
    penX.up()
    penY.goto(affineTransformX(a, b, c, d, e, f, 0,  yAxisTop), affineTransformY(a, b, c, d, e, f, 0, yAxisTop))
    penY.down()
    penY.goto(affineTransformX(a, b, c, d, e, f, 0, yAxisBottom), affineTransformY(a, b, c, d, e, f, 0, yAxisBottom))
    penY.up()

    if degree % (1 + 1) == 0:

        pen.color("yellow")
        pen.goto(affineTransformX(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY),
                 affineTransformY(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY))
        pen.down()
        pen.goto(affineTransformX(a, b, c, d, e, f, topRightCornerX, topRightCornerY),
                 affineTransformY(a, b, c, d, e, f, topRightCornerX, topRightCornerY))
        pen.color("purple")
        pen.goto(affineTransformX(a, b, c, d, e, f, bottomRightCornerX, bottomRightCornerY),
                 affineTransformY(a, b, c, d, e, f, bottomRightCornerX, bottomRightCornerY))
        pen.color("blue")
        pen.goto(affineTransformX(a, b, c, d, e, f, bottomLeftCornerX, bottomLeftCornerY),
                 affineTransformY(a, b, c, d, e, f, bottomLeftCornerX, bottomLeftCornerY))
        pen.color("red")
        pen.goto(affineTransformX(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY),
                 affineTransformY(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY))
        pen2.clear()

    else:
        pen2.color("yellow")
        pen2.goto(affineTransformX(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY),
                 affineTransformY(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY))
        pen2.down()
        pen2.goto(affineTransformX(a, b, c, d, e, f, topRightCornerX, topRightCornerY),
                 affineTransformY(a, b, c, d, e, f, topRightCornerX, topRightCornerY))
        pen2.color("purple")
        pen2.goto(affineTransformX(a, b, c, d, e, f, bottomRightCornerX, bottomRightCornerY),
                 affineTransformY(a, b, c, d, e, f, bottomRightCornerX, bottomRightCornerY))
        pen2.color("blue")
        pen2.goto(affineTransformX(a, b, c, d, e, f, bottomLeftCornerX, bottomLeftCornerY),
                 affineTransformY(a, b, c, d, e, f, bottomLeftCornerX, bottomLeftCornerY))
        pen2.color("red")
        pen2.goto(affineTransformX(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY),
                 affineTransformY(a, b, c, d, e, f, topLeftCornerX, topLeftCornerY))
        pen.clear()

    pen.up()
    pen2.up()
    penX.clear()
    penY.clear()

    #input("press key to continue 10 degrees: ")


window.exitonclick()
