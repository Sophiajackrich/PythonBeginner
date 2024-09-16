import turtle
##t = turtle.Turtle()
##t.forward(100)
##t.left(90) 
##t.forward(100)
##t.left(90) 
##t.forward(100)
##t.left(90) 
##t.forward(100)
##t.screen.mainloop()

# Or another way to improve is adding a loop
##t = turtle.Turtle()
##
##for i in range(4):
##
##    t.forward(100)
##
##    t.left(90)
##
##t.screen.mainloop()

### Create a function for drawing a square
t = turtle.Turtle()
def square():
    for i in range(4):

        t.forward(100)

        t.left(90)

# Using CANVAS to draw shapes in different places.

# create a "move" funtion
def move(x,y):
    ## to raise pencil up
    t.up()

    ## to move to the point with the coordinates specified in brackets,
    t.goto(x,y)

    ## to lower the "pencil"
    t.down()

### call move function
##move(150,150)
##
### call square funtion
##square()


# CREATE A PENTAGON FUNCTION
def pentagon():
    for i in range(5):

        t.forward(100)

        t.left(72)

### call move function
##move(150,-150)
##
### call the pentagon function
##pentagon()


# CREATE A POLYGON FUNCTION FOR THE SHAPES
def polygon(sides):
    for i in range(sides):
        t.speed(10)
        t.shape("turtle")
        t.forward(50)
        t.right(360/sides)

### call the polygon function for hexagon
##
##move(-150,150) 
##
##polygon(6)
##
##
### call the polygon function for hexagon
##move(160,-160)
##
##polygon(12) 
##
##
##
### call the polygon function for hexagon
##move(-180,-180)
## 
##polygon(9)


# DRAWING SHAPES VIA POLYGONS
##
##for i in range(24):
##
##    polygon(10)
##
##    t.left(15)
##
##
### using loop to draw shapes for polygon of 6
##move(-200,-200)  
##for i in range(10):
##
##    polygon(6)
##
##    t.left(36) 
##
##
### using loop to draw shapes for polygon of 6
##move(200,200)
##
##for i in range(6):
##    polygon(4)
##    t.left(60) 
##
##
### using loop to draw shapes for polygon of 7
##move(200,-200) 
##
##for i in range(6):
##
##    polygon(7)
##
##    t.left(60) 
##
##
### using loop to draw shapes for polygon of 5
##move(-200,200) 
##
##for i in range(60):
##
##    polygon(5)
##
##    t.left(6)


# DRAWING A CIRCLE
def circle():

    for i in range(60):

        t.forward(10)

        t.left(6)

# using loop to draw circle shapes for polygon of 5
for i in range(120):
    
    circle()
    polygon(5)

    t.left(3)

#move(0,200) 



t.screen.mainloop()
