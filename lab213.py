# 14.2
import turtle
turtle.shape("turtle")
n = 5
angel_degree = 180.0 - 180.0 / n

for i in range(n):
    turtle.forward(150)
    turtle.right(angel_degree)