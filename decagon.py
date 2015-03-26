import turtle
import random

awesome = turtle.Turtle()
awesome.pensize(10)
colors = ['orange','black']

def decagon(t,length):
    
    for i in range(10):
        t.color(random.choice(colors))
        t.forward(length)
        t.right(36)
        
decagon(awesome,50)
        
