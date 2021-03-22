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
