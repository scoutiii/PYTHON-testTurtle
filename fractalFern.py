import turtle
import random

window = turtle.Screen()

pen = turtle.Turtle()

window.screensize(500, 1000)

window.setworldcoordinates(-250, 0, 250, 1000)

window.bgcolor("black")
pen.color("green")
pen.pensize(.000001)
pen.shape("blank")
pen.speed(1000000000000000000)

window.tracer(10000, 0)

pen.goto(0, 0)
pen.goto(250, 0)
pen.goto(250, 1000)
pen.goto(-250, 1000)
pen.goto(-250, 0)
pen.goto(0, 0)
pen.up()

XOld = 0
Yold = 0
Xnew = 0
Ynew = 0

scalingFactor = 107

for i in range(1000000):
    prob = random.randint(0, 100)

    if prob <= 1:
        Xnew = 0
        Ynew = .16 * Yold
    elif prob <= (1 + 85):
        Xnew = (.85 * XOld) + (.04 * Yold)
        Ynew = (-.04 * XOld) + (.85 * Yold) + 1.60
    elif prob <= (1 + 85 + 7):
        Xnew = (.20 * XOld) + (-.26 * Yold)
        Ynew = (.23 * XOld) + (.22 * Yold) + 1.60
    else :
        Xnew = (-.15 * XOld) + (.28 * Yold)
        Ynew = (.26 * XOld) + (.24 * Yold) + .44

    pen.goto(scalingFactor * Xnew, scalingFactor * Ynew)
    pen.dot()
    pen.up()

    XOld = Xnew
    Yold = Ynew

window.exitonclick()
