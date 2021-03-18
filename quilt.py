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
bluesquilt_list = [navy, aquamarine, darkblue, teal, darkgreen, tan]

#all the HTML colors for the red/grey blocks and strips quilt
red = '#C8361E'
brown = '#563226'
lightgrey = '#CFC3AD'
grey = '#757266'
darkgrey = '#363435'
black = '#1D1D1F'
redgreyquilt_list = [black, red, brown, lightgrey, grey, darkgrey]

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
sandyhilllazygalquilt_list = [orange, yellow, purple, newblack, newbrown, grass, snow, newblue, darkteal]

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
    pu()
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east

def drawRectangle(size, color):
    """Draws a single rectangle of side length size and given color"""
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

def drawRectangle2(size, color):
    """Draws a single rectangle of side length size and given color
    assuming turtle is initially at one of its endpoints and the rectangle will fit within the screen"""
    pd()
    pen(fillcolor = color)
    pencolor(color)
    begin_fill()
    fd(size)
    if -400 <= xcor() <= 400 and -400 <= ycor() <= 400:
        lt(90)
        fd(size/2)
    if -400 <= xcor() <= 400 and -400 <= ycor() <= 400:
        lt(90)
        fd(size)
    if -400 <= xcor() <= 400 and -400 <= ycor() <= 400:
        lt(90)
        fd(size/2)
    lt(90)
    end_fill()
    pu()
#I have no idea why the hell this sometimes draws a triangle and having the pen not be clear is a problem

def drawSkinnyColumn(size, height, color1, color2):
    """Draws a skinny rectangle a fraction of the height
    and then another skinny rectangle on top of it to complete the column for sandyhilllazygal"""
    #seems like there's probably a cleaner way to do this
    pd()
    pen(fillcolor = color1)
    pencolor(color1)
    s = random.uniform(1,3)
    begin_fill()
    fd(size/16)
    lt(90)
    fd(height/s)
    lt(90)
    fd(size/16)
    lt(90)
    fd(height/s)
    lt(90)
    end_fill()
    fd(size/16)
    lt(90)
    fd(height/s)
    lt(90)
    fd(size/16)
    rt(180)
    pen(fillcolor = color2)
    pencolor(color2)
    begin_fill()
    fd(size/16)
    lt(90)
    fd(height-height/s)
    lt(90)
    fd(size/16)
    lt(90)
    fd(height-height/s)
    end_fill()
    fd(height/s)
    lt(90)
    fd(size/16)
    pu()

def drawMiniRows(size, color1, color2):
    """Draws a skinny rectangle a fraction of the quarter width
    and then another skinny rectangle beside it to complete the quarter row for sandyhilllazygal"""
    pd()
    pen(fillcolor = color1)
    pencolor(color1)
    s = random.uniform(1,1.667)
    begin_fill()
    fd(size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    end_fill()
    pen(fillcolor = color2)
    pencolor(color2)
    fd(size/(4*s))
    begin_fill()
    fd(size/4-size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/4-size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    end_fill()
    fd(size/4-size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/4)
    lt(180)
    pu()

def testDrawQuilt(size, colorlist): #should probably delete this one but keeping for now just in case
    """Initializes turtle, and then calls drawRectangle multiple times in different places and colors"""
    initializeTurtle(size, colorlist[0])
    for _ in range(30):
        z = random.randint(2, 4)
        drawRectangle(size/z, random.choice(colorlist))
        y = random.randint(1,size)
        fd(y/4)
        if y % 2 == 0:
            lt(90)
            w = random.randint(1,size)
            fd(w/4)

#def recursiveHelper(size, colorlist):
#if size <= 200:


def testDrawQuilt2(size, colorlist): #this moves them around a bit more randomly than the OG
    """Initializes turtle, and then calls drawRectangle multiple times in different places and colors a bit more randomly"""
    initializeTurtle(size, colorlist[0])
    for _ in range(30):
        z = random.randint(2, 4)
        drawRectangle(size/z, random.choice(colorlist))
        setx(random.randint(-400,400))
        sety(random.randint(-400,400))
        if xcor() % 2 == 0: #so that they'll randomly draw upwards sometimes
            lt(90)

def SandyHillQuilt(size, backgroundcolor, colorlist):
    """Draws the SandyHillQuilt, since that once proceeds very differently from the other two"""
    initializeTurtle(size, backgroundcolor)
    bk(size/2)
    rt(90)
    fd(size/2)
    lt(90)
    for i in range(5): #first 5 columns
        drawSkinnyColumn(size, size, random.choice(colorlist), random.choice(colorlist))
    #this is where the middle squares should go
    for i in range(4):
        drawMiniRows(size, random.choice(colorlist), random.choice(colorlist)) #short horizontal stripes
    for i in range(4):
        drawSkinnyColumn(size, size/4, random.choice(colorlist), random.choice(colorlist)) #short vertical stripes
    lt(90) #blank space for red
    fd(size/2)
    lt(90)
    fd(size/4)
    lt(180)
    for i in range(4):
        drawMiniRows(size, random.choice(colorlist), random.choice(colorlist)) #short horizontal stripes
    fd(size/4)
    rt(90)
    fd(size)
    lt(90)
    #end of middle squares
    for i in range(7): #last 7 columns
        drawSkinnyColumn(size, size, random.choice(colorlist), random.choice(colorlist))



if __name__=='__main__':
    """Testing code- uncomment whichever quilt you want to generate"""

    #testDrawQuilt2(800, bluesquilt_list) #blue quilt
    #testDrawQuilt2(800, redgreyquilt_list) #red/grey quilt
    SandyHillQuilt(800, lipstick, sandyhilllazygalquilt_list) #sandhilllazygal quilt
    #I want the red/grey quilt to split in half and draw twice but I'm struggling to make that happen
    #setting a boundary turtle can't cross seems like the next step
    #the whole setx/sety deal may be easier than my moving it around by random amounts thing
    #using recursion
    #technically speaking, they shouldn't overlay but fit together <- no idea how to tackle that
    exitonclick()
