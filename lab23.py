# 5
import turtle
turtle.shape("turtle")
n1 = 100
y = 1
x = 1
for i in range(0, 10):
    for k in range(4):
        turtle.forward(n1)
        turtle.left(90)
    n1 = n1 + 40
    turtle.penup()
    x = x - 20
    y = y - 20
    turtle.goto(x,y)
    turtle.pendown()



