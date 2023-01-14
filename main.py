from turtle import Turtle, Screen
import random as r

turtle = Turtle()
screen = Screen()
colors = ["royal blue", "chartreuse", "forest green", "light salmon", "maroon", "dark slate blue", "medium spring green"]


def turn_right(angle=90):
    turtle.right(angle)


def move(steps=100):
    turtle.forward(steps)


def back(steps=100):
    turtle.backward(steps)


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


def generate_shapes():
    for v in range(3, 11):
        color = r.choice(colors)
        turtle.color(color)
        draw_shape(vertex=v)


def generate_walks(steps=10):
    for i in range(steps):
        dir = r.choice(directions)
        # speed = r.choice(speed_type)
        color = r.choice(colors)
        turtle.color(color)
        # turtle.speed(speed)
        turtle.speed("fastest")
        turn_right(dir)
        move(50)


directions = [0, 90, 180, 270]
speed_type = ["fastest", "fast", "normal", "slow", "slowest"]

turtle.shape("arrow")
turtle.pensize(10)


generate_walks(steps=200)


screen.exitonclick()