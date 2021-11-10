# 11
import turtle
turtle.shape("turtle")
n = 0
x = 0
y = 0
turtle.right(90)
for i in range(20):
    turtle.circle(30 + n)
    turtle.goto(0, 0)
    turtle.right(180)
    turtle.circle(30 + n)
    turtle.goto(0, 0)
    n = n + 15
