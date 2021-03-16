from turtle import *
import random

#all the HTML colors for the blue quilt
aquamarine = '#51D3F7'
darkblue = '#2D40A2'
tan = '#DDBA7C'
teal = '#0588AE'
darkgreen = '#1D402F'
navy = '#1F2B41'

def initializeTurtle(size):
    """Sets up the window and initializes the turtle
    to be at the center of the screen."""
    padding = 25  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = size + padding, height = size + padding)
    bgcolor(navy)
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(0) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east

def drawRectangle(size, color):
    """Draws a single rectangle of side length size and given color
    assuming turtle is initially at one of its endpoints"""
    pd()
    pen(fillcolor = color)
    pencolor(color)
    begin_fill()
    fd(size)
    lt(90)
    fd(size/2)
    lt(90)
    fd(size)
    lt(90)
    fd(size/2)
    lt(90)
    end_fill()
    pu()

def testDrawQuilt(size, color1, color2, color3, color4, color5):
    """Initializes turtle, and then calls drawRectangle multiple times in different places and colors"""
    initializeTurtle(size)
    for _ in range(30):
        z = random.randint(2, 4)
        x = random.randint(1, 5)
        if x % 5 == 0:
            drawRectangle(size/z, color1)
        elif x % 5 == 1:
            drawRectangle(size/z, color2)
        elif x % 5 == 2:
            drawRectangle(size/z, color3)
        elif x % 5 == 3:
            drawRectangle(size/z, color4)
        elif x % 5 == 4:
            drawRectangle(size/z, color5)
        y = random.randint(1,size)
        fd(y/6)
        if y % 2 == 0:
            lt(90)
            w = random.randint(1,size)
            fd(w/6)

if __name__=='__main__':
    """Testing code"""

    testDrawQuilt(800, teal, aquamarine, darkblue, tan, darkgreen)
    exitonclick()
