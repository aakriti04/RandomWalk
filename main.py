from turtle import Turtle, Screen
import random

# https://en.wikipedia.org/wiki/Random_walk
tiny = Turtle()
screen = Screen()
screen.colormode(255)
tiny.shape("classic")
tiny.pensize(15)
tiny.speed("fastest")


def get_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


for _ in range(150):
    angles = [0, 90, 180, 270]
    angle = random.choice(angles)
    distances = [10, 12, 15, 18, 20, 25, 30, 35, 40]
    dist = random.choice(distances)
    tiny.pencolor(get_color())
    tiny.forward(dist)
    tiny.setheading(angle)

screen.exitonclick()
