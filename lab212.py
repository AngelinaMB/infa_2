# 14.1
import turtle
turtle.shape("turtle")
n = 11
angel_degree = 180.0 - 180.0 / n

for i in range(n):
    turtle.forward(150)
    turtle.right(angel_degree)