import tkinter as tk

import tkinter.messagebox as tmb

import random 

window = tk.Tk()

window.title("Guess the word") 

window.geometry("300x200")

# Create a "New game" tpo "re-select" a new word from the list
def new_game():

    global word

    global letters

    letters = []

    word = random.choice(words)

    label_word["text"] = "Here will be the word"
    

# create a function to check entered letter
def check_letter():

    letter = entry_letter.get()

    letters.append(letter)

    # erase old entry
    entry_letter.delete(0, "end")

    print(letter)
    
    show_word = ""
    
    for char in word:

        if char in letters:

            show_word += char

        else:

            show_word += "*"

    # Display word in the inscription
    label_word["text"] = show_word

    # create "if" condition for "victory
    if show_word == word:

        print("Victory!")

        # function of new game
        new_game()

        # show message using tkinter messagebox
        tmb.showinfo("Victory", "You guessed the word!")



# read "text file" to window
with open("words.txt") as file:

    data = file.read()

# split the list of words created using "split" command
words = data.split()  
print(words)

# create a variable
word = random.choice(words)

# create an empty list
letters = []

# inscription to spell hidden word
label_word = tk.Label(window, text= "Here will be the word", font=("Arial", 15))

# place label
label_word.place(x=70, y=20)

# enter letter
entry_letter = tk.Entry(window, width=8, font=("Arial", 10)) 

# place entry field
entry_letter.place(x=130, y=80)

# create button
check_button = tk.Button(window, text="Check the letter", font=("Arial", 10), command = check_letter) 

# place button
check_button.place(x=100, y=120)






tk.mainloop()
