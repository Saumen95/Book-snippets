import turtle
import math

def wedge(t, length, slices):
    inner_angle = 360 / slices
    outer_angle = (180 - inner_angle) / 2
    outer_length = 2 * length * math.cos (outer_angle / 180 * math.pi)
    t.fd(length)
    t.lt(180 - outer_angle)
    t.fd(outer_length)
    t.lt(180 - outer_angle)
    t.fd(length)
    t.lt(180)

def pie(t, length, slices):
    for i in range(slices):
        wedge(t, length, slices)

bob = turtle.Turtle()
pie(bob, 200, 7)

turtle.mainloop()