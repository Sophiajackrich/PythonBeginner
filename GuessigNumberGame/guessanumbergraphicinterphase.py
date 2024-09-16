import tkinter as tk 

import random 

window = tk.Tk() 

window.geometry("200x150") 

window.title("Guess the number")

# Seting guessing number
secret_number = random.randint(1, 100)

# make attempts 
attempts = 10


# CREATING A FUNCTION WITH TWO CALL METHODS
## First lets test it with a print function
def guess(event):
    #print("It is working")

    # refer to attempts in the main program
    global attempts

    number = entry.get()

    if number == "":

        label["text"] = "Please enter the number from 1 to 100"
    else:
        if attempts > 0:
            reset_button.configure(state=tk.DISABLED)

            attempts -= 1

            attempts_label["text"] = f"Number of attempts: {attempts}"

            number = int(number)
        # shifting the code to the right
            if number == secret_number:

                label["text"] = "Congratulations, you guessed right!"
                attempts = 0

                guess_button.configure(state=tk.DISABLED)

                reset_button.configure(state=tk.NORMAL)

            if number < secret_number:

                label["text"] = "The hidden number is greater!"

            if number > secret_number:

                label["text"] = "The hidden number is less!"
            
            entry.delete(0, "end")
            
            
        else: 
            #attempts = 0
            reset_button.configure(state=tk.NORMAL)
            reset
     



# making label inscription for window
label = tk.Label(window, text="Guess the number from 1 to 100") 

label.place(x=30, y=0)


# attempts inscription 
attempts_label = tk.Label(window, text=f"Number of attempts: {attempts}") 

attempts_label.place(x=30, y=30)


# create text field to enter numbers
entry = tk.Entry(window) 

entry.place(x=60,y=50) 

entry.focus_set()

#Add the first button to the window 
guess_button = tk.Button(window, text="Check", width=17, command=lambda e="<Return>": guess(e)) 

guess_button.place(x=35, y=80)

# Reset function
def reset():

    global secret_number, attempts

    secret_number = random.randint(1, 100)

    attempts = 10

    attempts_label["text"] = f"Number of attempts: {attempts}"

    label["text"] = "Please enter the number from 1 to 100"
    entry.delete(0, "end")
    
    


#Add the second button to the window
reset_button = tk.Button(window, text="Play again",width=17, command=reset, state=tk.DISABLED) 

reset_button.place(x=35,y=110)

guess_button.configure(state=tk.NORMAL)

# using the "bind" command, to call the function with an "Enter key"
window.bind("<Return>", guess) 


window.mainloop() 