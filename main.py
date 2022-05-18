import random
import turtle
from turtle import Turtle

tim = Turtle()

tim.speed("fastest")
turtle.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shapes():
    perfect_angles = [60, 90, 108, 120, 128.57, 135, 140, 144]
    angles_index = 0
    for i in range(3, 11):
        tim.color(random.choice(colours))
        index = i
        for line in range(index):
            tim.forward(100)
            tim.right(180-perfect_angles[angles_index])
        angles_index += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    for _ in range(200):
        tim.color(random_color())
        angles = [0, 90, 180, 270]
        directions = ["forward", "backward", "left", "right"]
        angle_choice = random.choice(angles)
        direction_choice = random.choice(directions)
        if direction_choice == "forward":
            tim.forward(random.randint(1, 100))
        elif direction_choice == "backward":
            tim.backward(random.randint(1, 100))
        elif direction_choice == "left":
            tim.left(angle_choice)
        elif direction_choice == "right":
            tim.right(angle_choice)


def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading()+gap_size)


draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
