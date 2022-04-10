import colorsys
from turtle import *
import turtle
bgcolor("black")
speed(11)
for i in range(1000):
    color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)

    turtle.color(color)
    turtle.forward(i)
    turtle.right(98)

done()