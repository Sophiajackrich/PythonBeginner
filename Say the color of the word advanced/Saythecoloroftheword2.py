import tkinter as tk
import random
import recog2

window = tk.Tk()

window.title("Say the color of the word")

window.geometry("350x250")



# declare instructions
instructions = tk.Label(
    window, text="Input color of the word, not the word! Push Enter to play",
    font=("Helvetica", 10))

# place the instructions on the window
instructions.place(x=10, y=10)

# create text field for answer
entry = tk.Entry(window, font=('Helvetica', 10)) 

# place entry
entry.place(x=10, y=180)

# to make the text field immediatetly get focus(cursor blinks)
entry.focus_set()

##MAKING A COLORED WORD

# make a list of colors
colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown", "white"]

# make a list of words
words = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange', 'white', 'purple', 'brown']
# create variable for 'score'
score = 0 

# create variable for 'fail'
fails = 0

# create variable for timer
time_left = 30

# display color
color_label = tk.Label(window,text=random.choice(words), font=('Helvetica', 40))

# place color
color_label.place(x=10, y=80)

# SCORE
# Add an inscription to show number for correct amswers
score_label = tk.Label(window, text=f"Right answers: {score}", font=("Helvetica", 10))

score_label.place(x=10, y=40)

# FAILURE
# Add an inscription to show number for wrong amswers
fails_label = tk.Label(window, text=f"Wrong answers: {fails} ", font=("Helvetica", 10))

fails_label.place(x=10, y=60)

# Create label inscription for window
time_label = tk.Label(window, text=f"Seconds left: {time_left}")

time_label.place(x=10, y=210)

# create a timer function
def timer():

    global time_left

    if time_left > 0:

        time_left -= 1

        time_label["text"] = f"Seconds left : {time_left}"
        time_label.after(1000, timer)

# Create a functio for a new word
def new_word(): 

    color_label["fg"] = random.choice(colors)

    color_label["text"] = random.choice(words)

# Functions to check events
def check(event):
    #print("Checking")
    # add global(main program) score
    global score
    # add global(main program) fail
    global fails

    # condition for time_left
    if time_left > 0:
        #user_color = entry.get()
        word_color = color_label["fg"] # getting the colour of the text
        i = colors.index(word_color) # getting the index of the word from the list of colours
        
        color = words[i] # getting the name of the colour from the list of the words

        response = recog2.speech() # recognizing, analyzing and return the text

        #print(color, response) 

        if color == word_color: # comparing the colour and the text
            print("yes")
            score += 1
            score_label["text"] = f"Correct: {score}"

        else:
            print("no")
            fails += 1
            fails_label["text"] = f"Wrong: {fails}"

        new_word()   
        entry.delete(0, "end")




new_word() 
# bind function to action
window.bind("<Return>", check)

# call timer fuction
#timer()
time_label.after(1000,timer)

# get the value from the text field and the value of the font color


window.mainloop()
