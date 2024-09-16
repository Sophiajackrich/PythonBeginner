import tkinter as tk

import random 

import time

window = tk.Tk()

window.geometry("650x500")

window.title("Colored shapes")

# create a canvas variable
canvas = tk.Canvas(window, bg="white", width=500, height=500)

canvas.place(x=0, y=0)

colors = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange',  'purple', 'brown']

# Initial stop value for loop
stop = False


# Function to make "stop" command "True"
def stop_draw(): 

    global stop 

    stop = True

# create a function for drawing circle
def draw_circle(): 
    color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500-d) 
    y = random.randint(0, 480-d)
    canvas.create_oval(x, y, x+d, y+d, fill=color)

# create a function for drawing an OVAL
def draw_oval(): 

    color = random.choice(colors) 

    d1 = random.randint(1, 100) 

    d2 = random.randint(1, 100)

    x = random.randint(0, 500-d1) 

    y = random.randint(0, 500-d2) 

    canvas.create_oval(x, y, x + d1, y + d2, fill=color)

# Create a function for drawing square
def draw_square(): 

    color = random.choice(colors) 
    color_border = random.choice(colors)

    d = random.randint(1, 100) 

    x = random.randint(0, 500-d) 

    y = random.randint(0, 500-d) 

    canvas.create_rectangle(x, y, x + d, y + d, fill=color, outline=color_border)

# endless loop function of circles
def draw_circles(): 
    global stop
    while True: 

        draw_circle() 

        window.update()

        time.sleep(1)
        if stop:
            stop = False
            break

# Create an animate circle function
def animate_circle():

    color = random.choice(colors) 

    d = random.randint(1, 100) 

    x = random.randint(0, 500-d) 

    y = random.randint(0, 500-d)

    circle = canvas.create_oval(x, y, x + d, y + d, fill=color)
    
    dx = 2

    dy = 2

    while True: 
        coords = canvas.coords(circle) 

        # rewrite coordinates of animated circle
        print(coords) 

        left = coords[0] 

        top= coords[1] 

        right = coords[2] 

        bottom = coords[3] 

        # use coordinates to set dimensions to be a particular range
        if left <= 0 or right >= 500: 

            dx = -dx 

        if top <= 0 or bottom >= 500:
            dy = -dy       

        canvas.move(circle, dx, dy) 
        # add a delay
        time.sleep(0.01)
        window.update()

# Make a button to draw circle on canvas
button_circle = tk.Button(window, width=17, text="Draw a circle", command=draw_circle)

#Place the button
button_circle.place(x=510, y=20)

# Make a button to draw OVAL on canvas
button_oval = tk.Button(window, text="Draw the oval", width=17, command=draw_oval)


# Make a button to draw SQUARE on canvas
button_oval.place(x=510, y=90)

button_square = tk.Button(window, text="Draw the square", width=17, command=draw_square)

button_square.place(x=510, y=150)

# button for new function
button_circles = tk.Button(window, text="Endless circles", width=17, command=draw_circles)

button_circles.place(x=510, y=220)

# Button to stop endless loop function
stop_button = tk.Button(window, text="Stop animation", bg="orange", width=17, command=stop_draw)

stop_button.place(x=510, y=360)

# Button for animated circle
button_circle_a = tk.Button(window, text="Animate the circle", width=17, command=animate_circle)

button_circle_a.place(x=510, y=290)

window.mainloop()