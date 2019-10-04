import turtle
import random

window = turtle.Screen()

pen = turtle.Turtle()

window.screensize(600, 600)

window.bgcolor("black")
pen.color("green")
pen.pensize(.000001)
pen.shape("blank")
pen.speed(1)


def TreeRecur(x, y, deg, dist, depth, maxDepth, previousDegree):
    degree = deg #* random.uniform(0, .5)
    pen.setheading(previousDegree)
    pen.left(degree)
    pen.forward(dist)

    newX = pen.xcor()
    newY = pen.ycor()

    if depth < maxDepth:
        TreeRecur(newX, newY, deg, dist, depth + 1, maxDepth, degree)

    pen.up()
    pen.goto(x, y)
    pen.setheading(-1 * (degree + deg + 90))
    pen.down()

    pen.left(-1 * degree)
    pen.forward(dist)

    newX = pen.xcor()
    newY = pen.ycor()

    if depth < maxDepth:
        TreeRecur(newX, newY, deg, dist, depth + 1, maxDepth, degree)

    pen.up()


def WrapTreeRecur(maxDepth, distance, degree):
    pen.up()
    pen.goto(0,0)
    pen.down()
    pen.setheading(90)
    pen.forward(distance)
    TreeRecur(pen.xcor(), pen.ycor(), degree, distance, 0, maxDepth, 90)


WrapTreeRecur(3, 50, 60)

window.exitonclick()
