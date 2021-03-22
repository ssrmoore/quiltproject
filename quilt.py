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
redgreyquilt_list = [red, brown, lightgrey, grey, darkgrey]

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

def initializeTurtle(long, tall, color):
    """Sets up the window and initializes the turtle
    to be at the center of the screen."""
    padding = 0  # increase if patterns gets cut off
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

def drawNewRectangle(length, height, color):
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
def drawSkinnyColumn(size, height, color1, color2):
    """Draws a skinny rectangle a fraction of the height
    and then another skinny rectangle on top of it to complete the column for sandyhilllazygal"""
    s = random.uniform(1,3) #chooses a value between 1 and 3 to decide what fraction of the height to make the first rectangle
    drawNewRectangle(size/16, height/s, color1) #makes first rectangle
    fd(size/16) #directs turtle to the upper left corner of the new rectangle, facing east
    lt(90)
    fd(height/s)
    lt(90)
    fd(size/16)
    rt(180)
    drawNewRectangle(size/16, height-height/s, color2) #makes second rectangle
    fd(size/16) #goes to bottom right corner of the column to be ready for next section
    rt(90)
    fd(height/s)
    lt(90)

def drawMiniRows(size, color1, color2): #or this
    """Draws a skinny rectangle a fraction of the quarter width
    and then another skinny rectangle beside it to complete the quarter row for sandyhilllazygal"""
    s = random.uniform(1,1.667) #chooses number to divide size by to determine rectangle length
    drawNewRectangle(size/(4*s), size/16, color1) #draws first rectangle
    fd(size/(4*s)) #moves to start of second rectangle
    drawNewRectangle(size/4-size/(4*s), size/16, color2) #draws second rectangle
    fd(size/4-size/(4*s)) #moves to top left corner of the first rectangle to prepare for next row
    lt(90)
    fd(size/16)
    lt(90)
    fd(size/4)
    lt(180)

def SandyHillQuilt(size, backgroundcolor, colorlist):
    """Draws the SandyHillQuilt, since that one proceeds very differently from the other two"""
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



def DrawBoundedQuilt(long, tall, lxbound, lybound, uxbound, uybound, colorlist):
    """ This function takes in a length, width, lower bounds, upper bounds, and a color list and then
    randomly draws rectangles in a variety of sizes, orientations, and colors that respect the boundaries by first deciding
    whether to draw a tall or fat rectangle, then checking that the far corner of the rectangle would be in bounds
    before starting to draw it. if it won't be in bounds, we determine how it will go out of bounds and instead make the rectangle
    go to that bound but not past it."""

    for _ in range(20): #draw 20 rectangles
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

    #bluesquilt
    #initializeTurtle(800, 800, navy)
    #DrawBoundedQuilt(800, 800, -400, -400, 400, 400, bluesquilt_list)

    #redgreyquilt <-lol perhaps these should be functions but
    #initializeTurtle(800, 800, black)
    #DrawBoundedQuilt(800, 800, -400, -400, 400, 0, redgreyquilt_list) #draw lower half
    #DrawBoundedQuilt(800, 800, -400, 0, 400, 400, redgreyquilt_list) #draw upper half
    #setx(-400) #draw dividing line
    #sety(0)
    #drawNewRectangle(800, 20, lightgrey)

    #sandhilllazygal quilt
    SandyHillQuilt(800, lipstick, sandyhilllazygalquilt_list)


    #having sandyhillquilt not have the same colors next to itself would be cool 
    #technically speaking, they shouldn't overlay but fit together <- no idea how to tackle that
    #the only thing I can think of is cutting the quilt into artificial looking sections to minimize overlap <- could ask Chad
    exitonclick()
