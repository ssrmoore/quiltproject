#lets experiment with turtle to draw the quilt, since we are familiar with it

from turtle import * #this seems like it must do something important

purple = '#8E44AD'
gold = '#F4D03F'

def initializeTurtle(size):
    """Setups up the window and initializes the turtle
    to be at the bottom left corner of the pattern
    facing east (which is the default direction)."""
    padding = 25  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = size + padding, height = size + padding)
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(1) # Choose a pen thickness
    speed(3) # Set the speed; 0=fastest, 1=slowest, 6=normal
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east
    # Put turtle in bottom left corner of the quilt
    pu()
    setx(-size/2)
    sety(-size/2)
    pd()

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

def testDrawQuilt(size, color1 = purple):
    """Initializes turtle, calls drawSquare"""
    # initialize turtle
    initializeTurtle(size)
    # call drawQuilt
    drawRectangle(size, color1)
    # save the figure
    #getscreen().getcanvas().postscript(file="drawQuilt({},{}).eps".format(size))


if __name__=='__main__':
    """Testing code"""

    testDrawQuilt(500)
    exitonclick()
