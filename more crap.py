import turtle
import math


wn = turtle.Screen()

wn.setworldcoordinates(1,-1,180.5,1)

sin_wave = turtle.Turtle()


x = 0
for angle in range(0,361,10):
    y = math.sin(math.radians(angle))
    sin_wave.goto(x,y)
    x = x+5
