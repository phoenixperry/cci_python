import turtle

wm = turtle.Screen()
tess = turtle.Turtle()
tess.color("red")
tess.right(90)
tess.forward(100)
tess.right(90)
tess.stamp() #leaves turtle shape

for i in range(0, 32, 4):
    tess.speed(2) #goes from 0 to 10 with 10 fastest
    tess.shape("blank")
    tess.color("red")
    tess.right(90)
    tess.forward(20)
# lifts pen up and down
tess.up()
tess.forward(100)
tess.down()
tess.right(90)
tess.forward(100)

mark = tess
print(mark)
wm.exitonclick()
