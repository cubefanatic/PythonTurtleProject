import random
import turtle
from turtle import Turtle

tim = Turtle()

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


draw_shapes()
screen = turtle.Screen()
screen.exitonclick()
