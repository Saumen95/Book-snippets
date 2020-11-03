import turtle
import math

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,n,length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    # r is radius, so circumference is 2 * pi * r
    c = 2 * math.pi * r
    # we'll use 360 segments (one per degree), so length should be c/360
    length = c / 360
    for i in range(360):
        t.fd(length)
        t.lt(1)

def arc(t,r,angle):
    # r is radius, so circumference is 2 * pi * r
    c = 2 * math.pi * r
    # we'll use 360 segments (one per degree), so length should be c/360
    length = c / 360
    for i in range(angle):
        t.fd(length)
        t.lt(1)

bob = turtle.Turtle()
arc(bob,100,90)

turtle.mainloop()
