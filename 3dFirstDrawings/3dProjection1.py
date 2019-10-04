import turtle
# file which contains the functions to draw cube and coordinate axis
import cubeFunctions as funcsCube
import axisFunctions as funcsAxis
import cubeTwo


# just a function which prints out the commands
def printInstructions():
    print("q to quit, w s to change phi, a d to change theta")
    print("c to toggle cube, x to toggle axis")
    print("r to reset to 0 0 200 phi theta rho respectively")
    print("f to pay respects, or toggle the fill of the cube")
    print("h for help lol")


# defines all the parameters for the window and turtle
window = turtle.Screen()
pen = turtle.Turtle()
window.bgcolor("black")
pen.color("green")
pen.pensize(10)
pen.shape("blank")
pen.speed(100)
window.tracer(0, 0)

# holds info for angle down from z (phi)
# angle around z on x y plane (theta)
# and radius of the sphere
phi = 45
theta = 0
rho = 300

# this controls how much rho phi and theta will change from user input
phiDelta = 10
thetaDelta = 10
rhoDelta = .05

# allows toggling the cube plane and fill
cubeToggle = 0
planeToggle = 0
fillToggle = 0

# holds user input, set to y for no particular reason
command = "y"

# prints the instructions on start of program
printInstructions()

# this keeps the program running until the user hits q
while command != 'q':
    window.update()
    # gets the users input for the command
    command = input()
    # clears the screen from previous frame
    pen.clear()
    # checks the various commands and changes accordingly
    if command == 'w':
        phi -= phiDelta

    if command == 's':
        phi += phiDelta

    if command == 'a':
        theta -= thetaDelta

    if command == 'd':
        theta += thetaDelta

    if command == 'i':
        rho += rhoDelta

    if command == 'o':
        rho -= rhoDelta

    if command == 'c':
        cubeToggle += 1

    if command == 'x':
        planeToggle += 1

    if command == 'f':
        fillToggle += 1

    if command == 'r':
        rho = 200
        phi = 0
        theta = 0
        cubeToggle = 0
        planeToggle = 0
        fillToggle = 0

    if command == 'h':
        printInstructions()
    # this is where it draws the cube or planes based on the toggle
    if planeToggle % 2 == 0:
        funcsAxis.drawCoordinatePlanes(rho, phi, theta, pen)
    if cubeToggle % 2 == 0:
        funcsCube.drawCube(rho, phi, theta, pen, fillToggle)
        #cubeTwo.drawCube(rho, phi, theta, pen, fillToggle)
