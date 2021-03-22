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
bluesquilt_list = [aquamarine, darkblue, teal, darkgreen, tan]

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

def initializeTurtle(long, tall, color): #don't mess with this
    """Sets up the window and initializes the turtle
    to be at the center of the screen."""
    padding = 25  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = long + padding, height = tall + padding)
    bgcolor(color)
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(0) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    pu()
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east

def drawFatRectangle(size, color): #i think we can delete this
    """Draws a single rectangle of side length size and given color"""
    pd() #put down pen
    pen(fillcolor = color) #chooses color to fill in shape
    pencolor(color) #chooses color for pen itself
    begin_fill() #tells turtle that this is the start of the shape it is going to fill in
    fd(size) #moves forward by length size
    lt(90) #turns left 90 degrees
    fd(size/2) #moves forward by size/2
    lt(90) #turns left 90 degrees
    fd(size) #moves forward by size
    lt(90) #turns left by 90 degrees
    fd(size/2) #moves forward by size/2
    lt(90) #turns left by 90 degrees to return to original position
    end_fill() #tells turtle it is finished drawing the shape and to fill it in
    pu() #picks up pen

def drawTallRectangle(size, color): #and this
    """Draws a single rectangle of side length size and given color"""
    pd() #put down pen
    pen(fillcolor = color) #chooses color to fill in shape
    pencolor(color) #chooses color for pen itself
    begin_fill() #tells turtle that this is the start of the shape it is going to fill in
    fd(size/2) #moves forward by length size/2
    lt(90) #turns left 90 degrees
    fd(size) #moves forward by size
    lt(90) #turns left 90 degrees
    fd(size/2) #moves forward by size/2
    lt(90) #turns left by 90 degrees
    fd(size) #moves forward by size
    lt(90) #turns left by 90 degrees to return to original position
    end_fill() #tells turtle it is finished drawing the shape and to fill it in
    pu() #picks up pen

def drawNewRectangle(length, height, color): #pretty sure this is the one to keep
    """Draws a single rectangle of given dimensions and color"""
    pd() #put down pen
    pen(fillcolor = color) #chooses color to fill in shape
    pencolor(color) #chooses color for pen itself
    begin_fill() #tells turtle that this is the start of the shape it is going to fill in
    fd(length) #moves forward by length
    lt(90) #turns left 90 degrees
    fd(height) #moves forward by height
    lt(90) #turns left 90 degrees
    fd(length) #moves forward by length
    lt(90) #turns left by 90 degrees
    fd(height) #moves forward by height
    lt(90) #turns left by 90 degrees to return to original position
    end_fill() #tells turtle it is finished drawing the shape and to fill it in
    pu() #picks up pen

#sandy hill quilt stuff
def drawSkinnyColumn(size, height, color1, color2): #or this
#these should both probably be able to take in the rectangle function tbh
    """Draws a skinny rectangle a fraction of the height
    and then another skinny rectangle on top of it to complete the column for sandyhilllazygal"""
    #seems like there's probably a cleaner way to do this
    pd()
    pen(fillcolor = color1)
    pencolor(color1)
    s = random.uniform(1,3) #chooses a value between 1 and 3 to decide what fraction of the height to make the first rectangle
    begin_fill() #starts to draw bottom skinny rectangle of varying height
    fd(size/16)
    lt(90)
    fd(height/s)
    lt(90)
    fd(size/16)
    lt(90)
    fd(height/s)
    lt(90)
    end_fill() #finishes drawing bottom rectangle of varying height
    pu()
    fd(size/16) #directs turtle to the upper left corner of the new rectangle, facing east
    lt(90)
    fd(height/s)
    lt(90)
    fd(size/16)
    rt(180)
    pd()
    pen(fillcolor = color2) #switches to new pen color
    pencolor(color2)
    begin_fill() #begins drawing new recangle to fill the rest of the height
    fd(size/16)
    lt(90)
    fd(height-height/s)
    lt(90)
    fd(size/16)
    lt(90)
    fd(height-height/s)
    end_fill() #finishes drawing new rectangle to fill the rest of the height
    pu()
    fd(height/s) #goes to bottom right corner of the column to be ready for next section
    lt(90)
    fd(size/16)

def drawMiniRows(size, color1, color2): #or this
    """Draws a skinny rectangle a fraction of the quarter width
    and then another skinny rectangle beside it to complete the quarter row for sandyhilllazygal"""
    pd()
    pen(fillcolor = color1) #chooses color for first rectangle
    pencolor(color1)
    s = random.uniform(1,1.667) #chooses number to divide size by to determine rectangle length
    begin_fill() #starts to draw first rectangle
    fd(size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    end_fill()
    pu()
    pen(fillcolor = color2) #chooses color for the second rectangle
    pencolor(color2)
    fd(size/(4*s)) #moves to start of second rectangle
    pd()
    begin_fill() #starts to draw second rectangle
    fd(size/4-size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/4-size/(4*s))
    lt(90)
    fd(size/16)
    lt(90)
    end_fill()
    pu()
    fd(size/4-size/(4*s)) #moves to top left corner of the first rectangle to prepare for next row
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/4)
    lt(180)

def SandyHillQuilt(size, backgroundcolor, colorlist): #at least this still works lol
    """Draws the SandyHillQuilt, since that once proceeds very differently from the other two"""
    initializeTurtle(size, size, backgroundcolor)
    bk(size/2) #moves from center of screen to bottom left
    rt(90)
    fd(size/2)
    lt(90)
    for i in range(5): #first 5 columns
        drawSkinnyColumn(size, size, random.choice(colorlist), random.choice(colorlist))
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
    for i in range(7): #last 7 columns
        drawSkinnyColumn(size, size, random.choice(colorlist), random.choice(colorlist))



def TestingBoundaries(long, tall, lxbound, lybound, uxbound, uybound, colorlist): #this currently respects boundaries
    """ This function takes in a length, width, lower bounds, upper bounds, and a color list and then
    randomly draws rectangles in a variety of sizes, orientations, and colors that respect the boundaries by first deciding
    whether to draw a tall or fat rectangle, then checking that the far corner of the rectangle would be in bounds
    before starting to draw it. if it won't be in bounds, we determine how it will go out of bounds and instead make the rectangle
    go to that bound but not past it."""

    for _ in range(30): #draw 30 rectangles
        newsize = long/random.randint(2,4) #randomly decide the fractional size of the rectangle
        if random.randint(0,100)  % 2 == 0: #randomly decide orientation -> tall boy cases
            if xcor() + newsize/2 <= uxbound and ycor() + newsize <= uybound: #fits in both dimensions
                drawNewRectangle(newsize/2, newsize, random.choice(colorlist))
            elif xcor() + newsize/2 >= uxbound and ycor() + newsize <= uybound: #doesnt fit in x
                drawNewRectangle(uxbound - xcor(), newsize, random.choice(colorlist)) #resize appropriately
            elif xcor() + newsize/2 <= uxbound and ycor() + newsize >= uybound: #doesnt fit in y
                drawNewRectangle(newsize/2, uybound - ycor(), random.choice(colorlist)) #resize appropriately
            elif xcor() + newsize/2 >= uxbound and ycor() + newsize >= uybound: #doesnt fit in either
                drawNewRectangle(uxbound - xcor(), uybound - ycor(), random.choice(colorlist)) #resize appropriately
        else: #fat boy cases
            if xcor() + newsize <= uxbound and ycor() + newsize/2 <= uybound: #fits in both dimensions
                drawNewRectangle(newsize, newsize/2, random.choice(colorlist))
            elif xcor() + newsize/2 >= uxbound and ycor() + newsize <= uybound: #doesnt fit in x
                drawNewRectangle(uxbound - xcor(), newsize/2, random.choice(colorlist)) #resize appropriately
            elif xcor() + newsize/2 <= uxbound and ycor() + newsize >= uybound: #doesnt fit in y
                drawNewRectangle(newsize, uybound - ycor(), random.choice(colorlist)) #resize appropriately
            elif xcor() + newsize/2 >= uxbound and ycor() + newsize >= uybound: #doesnt fit in either
                drawNewRectangle(uxbound - xcor(), uybound - ycor(), random.choice(colorlist)) #resize appropriately
        setx(random.randint(lxbound, uxbound)) #randomly moves to new coordinates within bounds for next rectangle
        sety(random.randint(lybound, uybound))

if __name__=='__main__':
    """Testing code- uncomment whichever quilt you want to generate"""
    #initializeTurtle(800, 800, bluesquilt_list[0])
    #TestingBoundaries(800, 800, -400, -400, 400, 0, bluesquilt_list)
    #TestingBoundaries(800, 800, -400, 0, 400, 400, bluesquilt_list)

    initializeTurtle(800, 800, navy)
    TestingBoundaries(800, 800, -400, -400, 400, 400, bluesquilt_list)

    #testDrawQuilt(800, bluesquilt_list) #blue quilt
    #testDrawQuilt(800, redgreyquilt_list) #red/grey quilt
    #SandyHillQuilt(800, lipstick, sandyhilllazygalquilt_list) #sandhilllazygal quilt

    #I want the red/grey quilt to split in half and draw twice but I'm struggling to make that happen
    #setting a boundary turtle can't cross seems like the next step
    #the whole setx/sety deal may be easier than my moving it around by random amounts thing
    #using recursion
    #technically speaking, they shouldn't overlay but fit together <- no idea how to tackle that
    exitonclick()
