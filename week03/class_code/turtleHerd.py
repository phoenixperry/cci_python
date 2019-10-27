import turtle

wn = turtle.Screen()
wn.bgcolor("black")
alex = turtle.Turtle()
alex.color("yellow")
sam = turtle.Turtle()
sam.color("red")
tiny = turtle.Turtle()
tiny.color("green")

alex.goto(100,100)
alex.forward(100)

sam.goto(120,120)
sam.forward(100)

tiny.goto(140,140)
tiny.forward(100)

wn.exitonclick()
