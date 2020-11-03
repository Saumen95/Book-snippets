import turtle
import math

def arc(t, radius, angle):
    circum = 2 * math.pi * radius
    # we'll use 360 segments (one per degree), so length should be c/360
    length = circum / 360
    for i in range(angle):
        t.fd(length)
        t.lt(1)

def petal(t, radius, angle):
    # draws one petal, using the arc function twice
    for i in range(2):
        arc(t, radius, angle)
        t.lt(180 - angle)

def flower(t, petals, radius, angle):
    for i in range(petals):
        petal(t, radius, angle)
        t.lt(360 / petals)

bob = turtle.Turtle()
flower(bob, 48, 150, 100)

turtle.mainloop()