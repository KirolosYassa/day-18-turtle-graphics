from turtle import Turtle, Screen
import random as r

turtle = Turtle()
screen = Screen()
# colors = ["royal blue", "chartreuse", "forest green", "light salmon", "maroon", "dark slate blue", "medium spring green"]


def generate_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    color = (red, green, blue)
    return color


def set_new_color():
    color = generate_color()
    turtle.pencolor(color)


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


def draw_circle(radius=50):
    turtle.circle(radius=radius)


def draw_dashed_line(length=4, steps=10):
    for i in range(steps):
        move(length)
        turtle.penup()
        move(length)
        turtle.pendown()


def generate_shapes():
    for v in range(3, 11):
        set_new_color()
        draw_shape(vertex=v)


def generate_walks(steps=10):
    for i in range(steps):
        dir = r.choice(directions)
        # speed = r.choice(speed_type)
        set_new_color()
        # turtle.speed(speed)
        turn_right(dir)
        move(50)


def draw_spirograph(steps=5, radius=50, speed="fastest"):
    turtle.fillcolor("white")
    turtle.speed(speed)
    for i in range(int(360/steps)):
        set_new_color()
        draw_circle(radius)
        turtle.setheading(turtle.heading() + steps)


directions = [0, 90, 180, 270]
speed_type = ["fastest", "fast", "normal", "slow", "slowest"]

# Setting the screen color-mode
screen.colormode(255)
turtle.shape("arrow")
turtle.pensize(1)


draw_spirograph(steps=5, radius=100)


screen.exitonclick()
