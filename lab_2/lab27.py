# 9
import turtle
turtle.shape("turtle")
n = 3
a = 0
y = 0
x = 0
for i in range(100):
    for k in range(0, n):
        turtle.forward(50 + a)
        turtle.left(360/n)
    turtle.penup()
    n = n + 1
    a = a + 3
    x = x - 3
    y = y - 2 ** n
    turtle.pendown()