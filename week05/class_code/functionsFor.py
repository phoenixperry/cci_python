import turtle

def drawSquare(t,sz):
    """make turtle t draw a square with the size of sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightGreen")

alex = turtle.Turtle()
drawSquare(alex,50)
wn.exitonclick()

