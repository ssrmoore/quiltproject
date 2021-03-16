#lets experiment with turtle to draw the quilt, since we are familiar with it

from turtle import * #this seems like it must do something important
import random

purple = '#8E44AD'
gold = '#F4D03F'
black = '#0C0B0B'
lightpurple = '#C089D3'

aquamarine = '#51D3F7'
darkblue = '#2D40A2'
tan = '#DDBA7C'
teal = '#0588AE'
darkgreen = '#1D402F'
navy = '#1F2B41'

def initializeTurtle(size):
    """Sets up the window and initializes the turtle
    to be at the bottom left corner of the pattern
    facing east (which is the default direction)."""
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
    """Draws a single square of side length size and given color
    assuming turtle is initially at one of its endpoints"""
    pd()
    pen(fillcolor = color)
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

def testDrawQuilt(size):
    """Initializes turtle, and then calls drawRectangle multiple times in different places"""
    # initialize turtle
    initializeTurtle(size)
    for _ in range(20):
        z = random.randint(1, 3)
        x = random.randint(1, 6)
        if x % 6 == 0:
            drawRectangle(size/z, aquamarine)
        elif x % 6 == 1:
            drawRectangle(size/z, darkblue)
        elif x % 6 == 2:
            drawRectangle(size/z, tan)
        elif x % 6 == 3:
            drawRectangle(size/z, teal)
        elif x % 6 == 4:
            drawRectangle(size/z, darkgreen)
        elif x % 6 == 5:
            drawRectangle(size/z, navy)
        y = random.randint(1,size)
        fd(y/6)
        if y % 2 == 0:
            lt(90)
            w = random.randint(1,size)
            fd(w/6)

    # save the figure
    #getscreen().getcanvas().postscript(file="drawQuilt({},{}).eps".format(size))

#also pick a better color palette, maybe by pulling from quilt if we were fancy
#how to solve the running off screen problem?


if __name__=='__main__':
    """Testing code"""

    testDrawQuilt(800)
    exitonclick()
