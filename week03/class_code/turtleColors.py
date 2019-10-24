import turtle
wn = turtle.Screen()
myTurtle = turtle.Turtle()
myTurtle.color("red")
myTurtle.left(90)

for color_ in ["red", "blue", "orange"]:
    myTurtle.color(color_)
    myTurtle.forward(120)


for name in ["bob", "sam", "potato"]:
    print(name)

wn.exitonclick()

