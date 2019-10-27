import turtle
#import the turtle drawing module
wn = turtle.Screen()
wn.bgcolor("yellow")
# create a canvas, or screen to draw on
alex = turtle.Turtle()
#create a turtle object named alex. turles face east to start
alex.color("blue")
#(Remember that Python is case sensitive, so the module name, turtle, with a lowercase t, is different from the type Turtle because of the uppercase T.)
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.backward(50)
alex.right(100)
alex.forward(20)

bob = turtle.Turtle()
bob.color("red")
bob.left(90)
bob.forward(100)

#move alex
wn.exitonclick()
#keep the window open until you click on it
