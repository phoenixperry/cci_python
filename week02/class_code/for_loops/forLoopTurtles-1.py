import turtle

wn = turtle.Screen()
wn.bgcolor("black")
alex = turtle.Turtle()
alex.color("yellow")
sam = turtle.Turtle()
sam.color("red")
tiny = turtle.Turtle()
tiny.color("green")
x = 100

for t_ in [alex, sam, tiny]:
    x+=20
    t_.goto(x,x)
    t_.forward(100)

#for i in range(0, 10, 2):
 #   print(i)

wn.exitonclick()
