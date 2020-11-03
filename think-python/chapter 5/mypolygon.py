import turtle
bob = turtle.Turtle()
bob.fd(100)

for i in range(4):
    bob.fd(100)
    bob.lt(90)

print(bob)
turtle.mainloop()
