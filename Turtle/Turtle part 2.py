import turtle 

t = turtle.Turtle()

t.speed(0)

# create move function
def move(x, y):

    t.up()

    t.goto(x, y)

    t.down()

# create circle function
def circle():

    for i in range(60):

        t.forward(5)

        t.left(6)

# create a spiral function
def spiral():

    for i in range(160):
        print(i)

        t.forward(i/10)

        t.left(15)

#spiral()


# HOW TO DRAW A STAR
def star():

    for i in range(5):

        t.forward(100)

        t.left(144)

#star()

# HOW TO DRAW AN OLYMPIC LOGO
def olympic_circle(x, y, color):
    t.color(color)

    t.width(10)

    move(x, y)

    circle()

# create olympic logo function
def olympic_logo():
    olympic_circle(-120, 60, "blue")

    olympic_circle(0, 60, "black") 

    olympic_circle(120, 60, "red")  

    olympic_circle(-60, 0, "yellow")  

    olympic_circle(60, 0, "green")

# call the function
#olympic_logo()


# HOW TO DRAW USING THE KEYBOARD

# "up" function (setheading)
def up():

    t.setheading(90)

    t.forward(10)

# "down" function (setheading)
def down():

    t.setheading(-90)

    t.forward(10)

# "left" function (setheading)
def left():

    t.setheading(180)

    t.forward(10)

# "right" function (setheading)
def right():

    t.setheading(0)

    t.forward(10)

# CREATE A FUNCTION THAT DRAWS LINE IN A DIFFERENT PLACE
def up_or_down():

    if t.isdown():

        t.up()

    else:

        t.down()

# create a red color function
def red():

    t.color("red")

# To assign a function to a key, we need the "screen.onkeypress" command.
t.screen.onkeypress(up, key = "Up")

t.screen.onkeypress(down, "Down")

t.screen.onkeypress(left, "Left")

t.screen.onkeypress(right,"Right")

# assign the function to a space bar
t.screen.onkeypress(up_or_down, "space")

# assign "red" color to screen
t.screen.onkeypress(red, "r")

# assign "spiral" function to screen

t.screen.onkeypress(spiral,"s") 

#write the "screen.listen" command,
#which allows the program to "listen" to the keyboard and
#wait for the required key to be pressed

t.screen.listen()

t.screen.mainloop()




