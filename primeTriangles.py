import turtle
import primefac
import math
#
window = turtle.Screen()

pen = turtle.Turtle()

window.screensize(1000, 1000)

window.setworldcoordinates(0, 0, 1000, 1000)

window.bgcolor("black")
pen.color("green")
pen.pensize(.000001)
pen.shape("blank")
pen.speed(0)

window.tracer(10000, 10)
pen.up()

def F (x):
    coef1 = int(abs((math.cos((math.pi / 2) * x))))
    coef2 = int(abs((math.sin((math.pi / 2) * x))))
    func1 = ((x + x + 397) * (x + x + 397 + 1) / 2) + x
    func2 = ((x + 59 + x + 59 - 59) * (x + 59 + x + 59 - 59 + 1) / 2) + (x + 59)
    F = coef1 * func1 + coef2 * func2
    return F


# for working with hybrid functions.

# primeRateCheck = 10000
# numPrime = 0
#
# for x in range(0, primeRateCheck):
#     print x
#     if primefac.isprime(F(x)):
#         numPrime += 1
#
# print "numPrime: " + str(numPrime)
#
#
# input()
#
# consecutiveTriples = []
# xStart = 0
# numXToCheck = 10000000
#
# for x in range(xStart, xStart + numXToCheck):
#     print x
#     if primefac.isprime(F(x)):
#         firstNum = F(x)
#         firstX = x
#         count = 0
#         while primefac.isprime(F(x+1)):
#             num = F(x+1)
#             count += 1
#             x += 1
#         consecutiveTriples += [(firstX, firstNum, count)]
#
# sortedTriples = sorted(consecutiveTriples, key=lambda s: s[2], reverse=True)
#
# print consecutiveTriples[:10]
# print sortedTriples[:10]
#

# input()
# for calculating lines of slope less than 1.

# xInt = -50000
# numOfXInt = 100000
# numPrimes = 0
# primeRateFactor = 1000
# listOfPrimePairs = []
# denominator = 2
#
#
# for xInt in range(xInt, xInt + numOfXInt):
#     print(xInt)
#     if xInt <= 0:
#         for x in range(0, primeRateFactor * denominator, denominator):
#             y = (1.0/denominator)*x - xInt
#
#
#



# Calculates consecutive primes, works with slope 0 lines only

# consecutiveTriples = []
# xStart = 0
# numXToCheck = 1000000
# yInt = 463
#
# for x in range(xStart, xStart + numXToCheck):
#     print x
#     y = yInt
#     num = ((x + y)*(x + y + 1) / 2) + x
#     if primefac.isprime(num):
#         firstNum = num
#         firstX = x
#         count = 0
#         while primefac.isprime(((x+1+y)*(x+1+y+1)/2)+x+1):
#             num = ((x+1+y)*(x+1+y+1)/2)+x+1
#             count += 1
#             x += 1
#             y = yInt
#         consecutiveTriples += [(firstX, firstNum, count)]
#
# sortedTriples = sorted(consecutiveTriples, key=lambda s: s[2], reverse=True)
#
# print consecutiveTriples[:10]
# print sortedTriples[:10]
#
# input("plz wait")

# Calculates consecutive primes, works with slope 1 lines only

# consecutiveTriples = []
# xStart = 10000000
# numXToCheck = 10000000
# yInt = 397
#
# for x in range(xStart, xStart + numXToCheck):
#     print x
#     y = x + yInt
#     num = ((x + y)*(x + y + 1) / 2) + x
#     if primefac.isprime(num):
#         firstNum = num
#         firstX = x
#         count = 0
#         while primefac.isprime(((x+1+y+1)*(x+1+y+1+1)/2)+x+1):
#             num = ((x+1+y+1)*(x+1+y+1+1)/2)+x+1
#             count += 1
#             x += 1
#             y = x + yInt
#         consecutiveTriples += [(firstX, firstNum, count)]
#
# sortedTriples = sorted(consecutiveTriples, key=lambda s: s[2], reverse=True)
#
# print consecutiveTriples[:10]
# print sortedTriples[:10]

# input("plz wait")

# This is for vertical lines ie slope 0, from y=[0,100000]
# numPrime = 0
# listOfPrimePairs = []
#
# for yInt in range(0, 100000):
#     print(yInt)
#     for x in range(0, 1000):
#         num = (((x + yInt)*(x + yInt + 1)) / 2) + x
#         if primefac.isprime(num):
#             numPrime += 1
#     listOfPrimePairs += [(yInt, numPrime)]
#     numPrime = 0
#
#
# listOfPrimePairs = sorted(listOfPrimePairs, key=lambda s: s[1], reverse=True)
# print(listOfPrimePairs[:5])
#
# input("plz wait")


# for generating positive slopes

# numPrime = 0
# xStart = 0
# primeRateCheck = 1000
# numIntChecks = 100000
# listOfPrimePairs = []
# slope = 1
#
# for xStart in range(xStart, numIntChecks + xStart):
#     print(xStart)
#
#     if xStart <= 0:
#         for x in range(0, primeRateCheck):
#             # don't forget to check the slope!!!
#             y = slope*x - xStart
#
#             num = ((((x + y) * (x + y + 1)) / 2) + x)
#             if primefac.isprime(int(num)):
#                 numPrime += 1
#     else:
#         for x in range(xStart, xStart + primeRateCheck):
#             # don't forget to check the slope!!!
#             y = slope*x - xStart
#
#             num = ((((x + y) * (x + y + 1)) / 2) + x)
#             if primefac.isprime(int(num)):
#                 numPrime += 1
#     listOfPrimePairs += [(xStart, numPrime)]
#     numPrime = 0
#
# listOfPrimePairs = sorted(listOfPrimePairs, key=lambda s: s[1], reverse=True)
#
#
# # print(max(listOfPrimePairs, key=lambda x:x[1]))
# print(listOfPrimePairs[:10])

ys = 2
xs = 2
xo = 0
yo = 0

for x in range(xo, (1000/xs)+xo):
    for y in range(yo, (1000/ys)+yo):
        num = ((((x+(y))*(x+(y)+1))/2) + x)
        if primefac.isprime(num):
            pen.color("green")
            pen.goto(x*xs-xo, y*ys-yo)
            pen.dot()
        # if y == 0 and x%5 == 0:
        #     pen.color("white")
        #     pen.goto(x*xs, y*ys-10)
        #     pen.write(num)
    #window.update()

# pen.color("white")
# pen.goto(60*xs-xo, 0*ys-yo)
# pen.down()
# pen.goto(1000*xs-xo, 1020*ys-yo)
# window.update()

window.exitonclick()