"""Tutorial on Turtles"""
from turtle import Turtle, colormode, done
from turtle import *

import turtle
leo: Turtle = Turtle()
turtle.screensize(canvwidth=500, canvheight=500,
                  bg="#ffd04e")

leo.fillcolor("#4efeff")

side_length: int = 300
x:int = -150
y: int = -130

# leo.forward(300)
# leo.left(90)
# leo.forward(70)
# leo.left(90)
# leo.forward(70)
# leo.left(90)
# leo.forward(70)
# leo.left(180)
# leo.forward(70)
# leo.left(90)
# leo.forward(160)
# leo.right(90)
# leo.forward(70)
# leo.left(90)
# leo.forward(70)
# leo.left(90)
# leo.forward(210)
# leo.left(90)
# leo.forward(70)
# leo.left(90)
# leo.forward(70)

leo.penup()
leo.goto(x, y)
leo.pendown()

i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.fillcolor("#ff0ba2")
bob.penup()
bob.goto(x, y)
bob.pendown()

i: int = 0
while (i < 140):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(120)
    bob.speed(7)
    i = i + 1

done()