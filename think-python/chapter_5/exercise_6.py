import turtle

def koch(t, length):
    if length < 3:
        t.fd(length)
    else:
        koch(t, length / 3)
        t.lt(60)
        koch(t, length / 3)
        t.rt(120)
        koch(t, length / 3)
        t.lt(60)
        koch(t, length / 3)

def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        t.rt(120)

bob = turtle.Turtle()

length = 300

bob.lt(180)
bob.pu()
bob.fd(length / 2)
bob.rt(90)
bob.fd(length / 2)
bob.rt(90)
bob.pd()

snowflake(bob, length)

turtle.mainloop()
