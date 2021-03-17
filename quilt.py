from turtle import *
import random

#ask about self plagiarism

#all the HTML colors for the blue quilt
aquamarine = '#51D3F7'
darkblue = '#2D40A2'
tan = '#DDBA7C'
teal = '#0588AE'
darkgreen = '#1D402F'
navy = '#1F2B41'

#all the HTML colors for the red/grey blocks and strips quilt
red = '#C8361E'
brown = '#563226'
lightgrey = '#CFC3AD'
grey = '#757266'
darkgrey = '#363435'
black = '#1D1D1F'

#all the HTML colors for the SandyHillLazyGal quilt
orange = '#D67646'
yellow = '#CD8B33'
purple = '#5E4968'
newblack = '#383836'
newbrown = '#9B5C3A'
grass = '#98AA59'
snow = '#CEBD9F'
newblue = '#353B51'
darkteal = '#285B60'
lipstick = '#BD213A'

def initializeTurtle(size, color):
    """Sets up the window and initializes the turtle
    to be at the center of the screen."""
    padding = 25  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = size + padding, height = size + padding)
    bgcolor(color)
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(0) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east
    rt(90)
    fd(size/2)
    lt(90)

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

def drawSkinnyColumn(size, color1, color2):
    """Draws a single rectangle of side length size and given color
    assuming turtle is initially at one of its endpoints"""
    pd()
    pen(fillcolor = color1)
    pencolor(color1)
    s = random.uniform(1,3)
    begin_fill()
    fd(size/16)
    lt(90)
    fd(size/s)
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/s)
    lt(90)
    end_fill()
    fd(size/16)
    lt(90)
    fd(size/s)
    lt(90)
    fd(size/16)
    rt(180)
    pen(fillcolor = color2)
    pencolor(color2)
    begin_fill()
    fd(size/16)
    lt(90)
    fd(size-size/s)
    lt(90)
    fd(size/16)
    lt(90)
    fd(size-size/s)
    end_fill()
    fd(size/s)
    lt(90)
    fd(size/16)


    pu()

def testDrawQuilt(size, color1, color2, color3, color4, color5, color6):
    """Initializes turtle, and then calls drawRectangle multiple times in different places and colors"""
    initializeTurtle(size, color6)
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
        fd(y/4)
        if y % 2 == 0:
            lt(90)
            w = random.randint(1,size)
            fd(w/4)

def SandyHillQuilt(size, color1, color2, color3, color4, color5, color6, color7, color8, color9, color10):
#should probably make it so a list just feeds into this instead
    initializeTurtle(size, color1)
    lt(180)
    fd(size/2)
    lt(180)
    #how to have it randomly choose colors?
    colors_list = [color2, color3, color4, color5, color6, color7, color8, color9, color10]
    for i in range(5):
        if i % 2 == 0:
            drawSkinnyColumn(size, random.choice(colors_list), random.choice(colors_list))
        else:
            drawSkinnyColumn(size, random.choice(colors_list), random.choice(colors_list))
    fd(size/4)
    for i in range(7):
        if i % 2 == 0:
            drawSkinnyColumn(size, random.choice(colors_list), random.choice(colors_list))
        else:
            drawSkinnyColumn(size, random.choice(colors_list), random.choice(colors_list))

#its frustrating to me that the rectangles tend to concentrate in a half/quadrant
#technically speaking, they shouldn't overlay but fit together

if __name__=='__main__':
    """Testing code"""

    #testDrawQuilt(800, teal, aquamarine, darkblue, tan, darkgreen, navy) #blue quilt
    #testDrawQuilt(800, red, lightgrey, grey, darkgrey, brown, black) #red/grey quilt
    #I want this quilt to split in half and draw twice but I'm struggling to make that happen
    SandyHillQuilt(800, lipstick, orange, yellow, purple, newbrown, grass, newblack, snow, newblue, darkteal)
    exitonclick()
