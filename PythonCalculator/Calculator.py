# function for getting first number
def get_num1():
    num1 = text_num1.get() 
    num1 = int(num1)
    return num1

# function for getting second number
def get_num2():
    num2 = text_num2.get() 
    num2 = int(num2)
    return num2

# function for calling pasting and clearing result
def set_answer(answer):
    text_answer.delete(0, "end")
    text_answer.insert(0, answer)
    
# create a function for addition
def add():
    print("Performing the addition") 
    # Get first number
    num1 = get_num1()
    # Get second number
    num2 = get_num2() 
    # Store (num1 - num2) in a variable
    result = num1 + num2
    set_answer(result)
    
 # create a function for subtraction
def sub():
    print("Performing the Subtraction") 
    # Get first number
    num1 = get_num1()
    # Get the second number
    num2 = get_num2()
    #Store (num1 - num2) in a variable
    result = num1 - num2
    set_answer(result)  
    
def mul():
    # Get first number
    num1 = get_num1()
    # Get the second number
    num2 = get_num2()
    #Store (num1 * num2) in a variable
    result = num1 * num2
    #print result
    set_answer(result)

    

def div():
    # Get first number
    num1 = get_num1()
    # Get the second number
    num2 = get_num2()
    # Store (num1 / num2) in a variable
    result = num1 / num2
    # print result
    set_answer(result)

import tkinter

# Instantiate tkinter library to a variable "window"
window = tkinter.Tk()
# create the title of the window
window.title("My calculator")
# fix the size of the window
window.geometry("300x300") 

# Add the addition text ("+") to the button
button_add = tkinter.Button(window , text="+", command = add, width=7, height=2, bg="gold") 
# Now place the added button at the right co-ordinates
button_add.place(x=95, y=110)

# Add the Subtraction text ("-") to the button
button_sub = tkinter.Button(window, text="-", command = sub,  width=7, height=2, bg="gold")
# Now place the added button at the right co-ordinates
button_sub.place(x=160, y=110)

# Add the multiplication text ("*") to the button
button_mul = tkinter.Button(window, text="*", command=mul,  width=7, height=2, bg="gold")
# Now place the added button at the right co-ordinates
button_mul.place(x=95, y=154)

# Add the multiplication text ("/") to the button
button_div = tkinter.Button(window, text="/", command=div,  width=7, height=2, bg="gold")
# Now place the added button at the right co-ordinates
button_div.place(x=160, y=154)


# Add a text field to the window, 
#using appending format to the "window" parameter and 
#save to a variable
text_num1 = tkinter.Entry(window, width=20, bg = "black", fg = "gold")
# Now place the text 1 at the right co-ordinates 
text_num1.place(x=95, y=40)
#create second text field, stating its width parameter
text_num2 = tkinter.Entry(window, width=20, bg = "black", fg = "gold")
# place co-ordinate for text 2
text_num2.place(x=95, y=81)
#create an answer for text field entered
text_answer = tkinter.Entry(window, width=20, bg = "silver", fg = "black")
# place co-ordinate for answer field
text_answer.place(x=95, y=221)

# ADDING LABELS
## Add label to first text
label_num1 = tkinter.Label(window, text="Input the first number", background= "blue")
label_num1.place(x=95, y=20)#place first text description

## Add label to Second text
label_num2 = tkinter.Label(window, text="Input the second number", background= "blue")
label_num2.place(x=95, y=61)#place Second text description

## Add label for "answer" text
label_answer = tkinter.Label(window, text="The answer", background= "blue") 
label_answer.place(x=95, y=200)#place "answer"text description

# THE APPEARANCE OF BUTTONS
""" refer to the buttons above"""

# CONFIGURE THE COLOR OF WINDOW
window.configure(bg="blue")

window.mainloop()


