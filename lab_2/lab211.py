# 13
import turtle
turtle.shape("turtle")
turtle.begin_fill()
turtle.circle(80)
turtle.color("yellow")
turtle.end_fill()
# eyes
turtle.begin_fill()
turtle.up()
turtle.goto(30, 110)
turtle.down()
turtle.circle(10)
turtle.color("blue")
turtle.end_fill()

turtle.begin_fill()
turtle.up()
turtle.goto(-30, 110)
turtle.down()
turtle.circle(10)
turtle.color("blue")
turtle.end_fill()
# mouth
turtle.width(5)
turtle.color("red")
turtle.up()
turtle.goto(30, 50)
turtle.left(90)
turtle.down()
turtle.circle(30, -180)
# nose
turtle.width(10)
turtle.color("black")
turtle.up()
turtle.goto(0, 90)
turtle.left(90)
turtle.down()
turtle.left(90)
turtle.backward(45)
