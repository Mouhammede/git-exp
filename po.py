import turtle
turtle.bgcolor("black")
t=turtle.Turtle()
t.pencolor("green")
for i in range(450):
    t.left(1)
    if(i%100==0 and i!=0):
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)
    t.forward(1)
turtle.done()