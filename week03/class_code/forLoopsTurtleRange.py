import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in["yellow", "red", "purple", "blue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

for i in range(4):
    alex.forward(50)
    alex.left(20)

#range(start,stop,step)
#always stops one before the end of range
wn.exitonclick()

