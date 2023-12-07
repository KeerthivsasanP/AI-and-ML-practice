import turtle
import random

t = turtle.Turtle()
canvas = t.getscreen()

no_of_circle = int(input("Enter the number of circles"))
angle = 360/no_of_circle
t.speed(30)

for _ in range(no_of_circle):
    t.circle(100)
    t.lt(angle)
