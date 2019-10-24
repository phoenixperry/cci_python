import turtle
color = input("enter a color")
# Tools -> SublimeREPL -> Python -> Python - RUN current file

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color(color)
tess.pensize(3)
tess.forward(50)
tess.left(120)
tess.forward(50)
wn.exitonclick()
