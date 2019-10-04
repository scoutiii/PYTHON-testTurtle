import Camera as Camera
import FloorTile as flTl
import WallTile as wlTl
import turtle

window = turtle.Screen()
mapPen = turtle.Turtle()
window.bgcolor("black")
mapPen.color("green")
mapPen.pensize(1)
mapPen.shape("blank")
mapPen.speed(1000)
window.tracer(0, 0)
window.colormode(255)

cma = Camera.Camera(100, 70, 0, 1)

tileSize = 100
edgeColor = (200, 200, 200)
fillColor = (0, 100, 0)

mapElements = []
c = 0
for x in range(-500, 500, 100):
    for y in range(-500, 500, 100):
        mapElements.append(flTl.FloorTile(tileSize, [x, y, 0], edgeColor, fillColor, 1))
        mapElements.append(wlTl.WallTile(tileSize, [x, y, 0], edgeColor, (100, 0, 0), False, 1))
        c += 1

while True:
    window.update()
    input()
    mapPen.clear()

    distance = []
    for i in mapElements:
        dist = i.getDistance((cma.whatIsX(), cma.whatIsY(), cma.whatIsZ()))
        distance.append((dist, i))
    distance.sort(key=lambda j: j[0], reverse=True)

    for i in distance:
        i[1].drawObject(cma.whatIsRho(), cma.whatIsPhi(), cma.whatIsTheta(), mapPen)

    cma.setTheta(cma.whatIsTheta() + 10)
