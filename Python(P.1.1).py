# Student materials:
https://drive.google.com/drive/folders/1ZD5QQI0rAfxOmNr6m4I-FfqDM6JC5dQW?usp=drive_link

""" In the materials we find the file PEP.pdf,
ask the student to open it and together analyze the rules for writing code correctly.
Tell the student that there is a PEP8 standard and
in front of him is a file that describes the requirements for this standard.
Professional programmers write code based on this standard. """

# Complete video presentation below:
https://vimeo.com/678274756/e26d3e519b

# What were the things studied in the last class?


### START OF CLASS ACTIVITY;
## Things to do in class:

#  Lists
#  in/not in commands
#  Boolean variables, True, False
#  for loop
#  else condition
#  The end parameter in the print command


# 1. LISTS

""" What are lists??
LISTS are ordered collection of items that can be stored,
just like 'variables'and also be manipulated.
They are also called special variables,
because it allows us to store several values at once"""

# Examples 1. 

fruits = ["apple", "banana", "orange"] #Run this line of code & see what happens. 
#How can we display results on the screen?
print(fruits) #Run this line of code & see what happens.

# Example 2.
numbers = [1, 2, 3] #Run this line of code & see what happens.
#How can we display results on the screen?
print(numbers)#Run this line of code & see what happens.




# 2. APPEND COMMAND

"""An append command is used to add new or existing records into a list, etc."""

# Example 1.

fruits.append("peach") 
print(fruits)  #Run this line of code & see what happens.

# Example 2

numbers.append(4) 
print(numbers) #Run this line of code & see what happens.



# IN/NOT-IN COMMANDS AND BOOLEAN VARIABLES
""" This helps to check if a value exists 'IN' our LIST. This same as word
ENGLISH word 'IN'. For example,
let's find out if the word "apple" is in our list
(or any other value that is definitely there):"""

# Example 1.

answer =  "apple" in fruits

print(answer)  #Run this line of code & see what happens.

""" 
After running the code,  we can see that the word 'True' appears on the screen,
this means that "apple" is correctly in our 'fruits' LIST.
-> Note: 'True' & False in python are called a Boolean  variable
-> Boolean variables helps to tell us if something is 'True' or 'False',
when using the 'IN or NOT-IN' Command."""

# Example 2. Now let’s check a value that is 'not in' our list:

numbers =  8 in numbers

print(numbers)

""" 
After running the code,  we can see that the word 'False' appears on the screen,
this means that '8' is wrong and not in our 'numbers' LIST."""


# Example 3.

answer = "apple" not in fruits

print(answer) 

answer = "carrot" not in fruits

print(answer)

""" -> A boolean variable can store only one of the two values; 'True'
   or False, like the above example."""





# CREATING GAME OF "GALLOWS"

"""
Just like in previous lesson we guessed the number.

Here we will guess the word by letter i.e the 'FIELD OF MIRACLES' or 'GALLOWS';

This game is about spelling the right letters that the computer thought about.
"""

# Steps of the game are:

## First step, create a variable that stores the 'Hidden word'

## Second step: Empty list
"""-> An empty list: To store the letters we enter"""

## Third step: Creating a loop: While - > For loop -> IF & ELSE Command 
""" This is to run our game multiple times if a certain condition is met,
like in the previous lesson. Here, it we would contain other python syntax
in the loop, like; 'For loop', 'IF & Else command'"""


#### For loop ->
"""The for loop in Python is used to continuosly look through values in
    things like a list, or string.
    In the game, the for loop will go through all the letters in our word,
    writing them one by one to the char variable.
    """

#### IF & ELSE condition
"""
There are two conditions here.
'if & else' is used to check if a code is either 'True' or 'False'.

-> (Else statement is same as 'otherwise' or 'in another way' do this.
This command is executed(run) only if the 'If' fails to work.
i.e 'Else' command comes only after 'If' command isnt correct)


Example; *if a letter is in the list(true)*, then 'If block',
would display the letters,
but *if the letter is not in the list*, then the 'else block' would
display asterisk(*)."""

#### PRINT LETTERS ONE AFTER THE OTHER, still in the 'while loop
""" Here, 'end' parameter is used to add any string,
at the end of the output of the 'print' statement in python.
-> usually, the print statement takes us to a new line.
-> let us add a 'whitespace' to the end parameter in 'print' statement"""



print("Let's play. I thought of a word, you need to spell it")

hidden_word = "wolverine"

letters = [] 

attempts = 3

# FIRST CODE STEP: Create code
##while attempts > 0:
##    letter = input("Enter a letter: ")
##    letters.append(letter)
##    # FOR LOOP
##    for char in hidden_word:
##        # IF & ELSE condition
##        if char in letters: # checks if char in letters, is also in 'hidden_word'
##            print(char, end=" ") # displays the char and puts whitespace in btw each char.
##        else:
##            #displays (*) for the rest letters not guessed yet.
##            print("*", end=" ")
##    # takes 'Enter a letter to next line" after char is displayed.
##    print()
##    # Checks if the letter displayed, is in 'hidden_word' 
##    if letter not in hidden_word:
##        attempts = attempts - 1 # number of attempts left
##        print ("No such letter in the word. You have attempts left: " + str(attempts))
##    # checks if 'attempts' is 0
##    if attempts == 0:
##        print("You lost!") # displays 'You lost'

        

# NEXT STEP: Add 'Victory =True immediately after while loop', 'victory=False' inside Else
while attempts > 0:
    victory = True # stores the boolean 'True' in a variable.
    letter = input("Enter a letter: ")
    letters.append(letter)
    # FOR LOOP
    for char in hidden_word:
        # IF & ELSE condition
        if char in letters: # checks if char in letters, is also in 'hidden_word'
            print(char, end=" ") # displays the char and puts whitespace in btw each char.
        else:
            #displays (*) for the rest letters not guessed yet.
            print("*", end=" ")
            victory = False # meaning until there is no (*), then we havent't yet won. 
    # takes 'Enter a letter to next line" after char is displayed.
    print()
    # Checks if the letter displayed, is in 'hidden_word' 
    if letter not in hidden_word:
        attempts = attempts - 1 # number of attempts left
        print ("No such letter in the word. You have attempts left: " + str(attempts))
    
    if attempts == 0: # checks if 'attempts' is 0
        print("You lost!") # displays 'You lost'
        
    if victory == True: # checks if 'victory' is True
        print("You win!") # Stops the game and display 'You lost'
        break

             

### Things we are going to learn in todays class are;
"""
1. List
2. Append
3. IN/NOT-IN COMMANDS AND BOOLEAN VARIABLES
4. Creating a guessing game called 'Guess the word by letter' (using;
While loop -> for loop -> If & Else statement -> end etc.
"""

### Homework: If they are slow in typing;
"""To make us create alot of fun games, i would love you to learn to type faster, so i would
 send you a video to test your typing speed, okay?."""

# This are the instructions to follow;
https://www.ratatype.com/ru/?lang=ru

# Site below is where the student test typing speed.
https://drive.google.com/file/d/1fRkOuJbCvfsdXLiM2R9i7zw-HtqdWIGP/view?usp=drive_link
