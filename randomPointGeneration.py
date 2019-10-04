import turtle
import math
import random

window = turtle.Screen()

pen = turtle.Turtle()

window.screensize(600, 600)
window.setworldcoordinates(0, 0, 510, 510)

window.bgcolor("white")
pen.color("black")
pen.pensize(.000001)
pen.shape("blank")
pen.speed(1000000000000000000)
window.tracer(1000, 0)

p0 = [0, 0]
p1 = [500, 0]
p2 = [250, 500]
endPoints = [p0, p1, p2]
x = 0
y = 1

pen.up()
pen.goto(0, 500)
pen.down()
pen.dot()
pen.goto(500, 500)
pen.dot()
pen.goto(250, 0)
pen.dot()
pen.goto(0, 500)
pen.up()

random.seed()

previousX = 250
previousY = 0

for i in range(100000):
    #print(i)
    point = random.randint(0, 2)
    startX = endPoints[point][x]
    startY = endPoints[point][y]

    newX = ((previousX - startX) / 2) + 250
    newY = ((previousY - startY) / 2) + 250

    pen.goto(newX, newY)
    pen.dot()
    pen.down()
    pen.up()

    previousX = newX
    previousY = newY

window.exitonclick()
