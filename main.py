from turtle import Turtle, Screen
import random as r

turtle = Turtle()
screen = Screen()
colors = ["royal blue", "chartreuse", "forest green", "light salmon", "maroon", "dark slate blue", "medium spring green"]

def turn_right(angle=90):
    turtle.right(angle)


def move(steps=100):
    turtle.forward(steps)


def draw_shape(vertex=3, length=100):
    angle = 360/vertex
    for i in range(vertex):
        move(length)
        turn_right(angle)


def draw_dashed_line(length=4, steps=10):
    for i in range(steps):
        move(length)
        turtle.penup()
        move(length)
        turtle.pendown()


turtle.shape("arrow")
turtle.color(colors[1])
# draw_dashed_line(length=20, steps=4)

for v in range(3, 9):
    color = r.choice(colors)
    turtle.color(color)
    draw_shape(vertex=v)


screen.exitonclick()