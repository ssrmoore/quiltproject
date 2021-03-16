#lets experiment with turtle to draw the quilt, since we are familiar with it

from turtle import * #this seems like it must do something important
import random

purple = '#8E44AD'
gold = '#F4D03F'
black = '#0C0B0B'
lightpurple = '#C089D3'

def initializeTurtle(size):
    """Sets up the window and initializes the turtle
    to be at the bottom left corner of the pattern
    facing east (which is the default direction)."""
    padding = 25  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = size + padding, height = size + padding)
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(1) # Choose a pen thickness
    speed(6) # Set the speed; 0=fastest, 1=slowest, 6=normal
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
    for _ in range(7):
        x = random.randint(1, 6)
        if x % 4 == 0:
            drawRectangle(size/x, purple)
        elif x % 4 == 1:
            drawRectangle(size/x, lightpurple)
        elif x % 4 == 2:
            drawRectangle(size/x, black)
        elif x % 4 == 3:
            drawRectangle(size/x, gold)
        y = random.randint(1,size)
        fd(y/6)
        if y % 2 == 0:
            lt(90)
            z = random.randint(1,size)
            fd(z/6)

    # save the figure
    #getscreen().getcanvas().postscript(file="drawQuilt({},{}).eps".format(size))

#also pick a better color palette, maybe by pulling from quilt if we were fancy
#how to solve the running off screen problem?


if __name__=='__main__':
    """Testing code"""

    testDrawQuilt(800)
    exitonclick()
