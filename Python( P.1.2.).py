# P.1.2:  TODAY'S LESSON WE WOULD COMBINE WHAT WE HAVE LEARNT ON "VARIABLES"

# 1. What do you know about programming?, 2. what is python programming?

# Share your screen

# Share these student material at the begining of the class:
https://drive.google.com/drive/folders/1ttjxcKywXFcJubSGprmPU33TOdJ2_jPv?usp=drive_link

""" In the material you would;

-> find the file PEP.pdf, (This is a document that contains instructions on how to write
   codes correctly)

-> Now open it and

-> lets analyze the rules for writing code correctly.

# To write codes correctly:

-> Firstly, there is a PEP8 standard (This document that shows you the best way,
   to write python codes)

-> Secondly, at the open file, there is a file that tells you the requirements for this
PEP8 standard. *Professional programmers write code based on this standard.*

"""

# Share this video presentation below to the student - > the file consist of today's project:
https://vimeo.com/678274756/e26d3e519b

# Can you tell me what you learnt in previous lesson ?
"""
In previous lesson we learnt alot of new things like;

#  Lists
#  in/not in commands
#  Boolean variables, True, False
#  for loop
#  else condition
#  The end parameter in the print command

"""


### ACTIVITIES ;

"""

-> What we would do in todays lesson is to;

-- > Repeat the things we learnt previously, focusing on VARIABLES.
   
"""

# TODAYS ACTIVITY: VARIABLES

""" Can  you remember what a variable is ?

# Ways to writing variables, with examples:

- > 1. Variables  are containers used to store values like strings, integers(i.e numbers) etc.

       - > number = 2

- > 2. Variables can be given any name, but we must give a name that describes,

       what we are storing in the variable...*GIVE EXAMPLE*:

       - > Car = "Benz"

- > 3. Variable names must not be the same as the command example:

       - > You cant name a variable; e.g 'print', 'input', 'if' etc... Example:

         if = 5

         if if == 5:
             print('Yes')
    
- > 4. Variable names are written with a small letter, if it is a single word...

       - > Example: name = 'Alex'

- > 5. If a Variable name consists of two or more words, put an underscore(_) btw the word.

       - > Example: first_name = 'Alex'
       
- > 6. Variables can store different types of data. For example, it can store:

       -> Some words or sentence. In programming language, these are called strings -

          strings are written inside of quotes, that is  double or single quotes                   

"""

# Example 1. Create a variable name that stores a string:

city = 'Penza'

print(city + 'very beautiful city')#When we use '+' to add strings it is called concatenation



# Example 2. Create a variable name that stores an integer or a number:

current_year = 2020 # An integer

print("It is "+current_year+" year")#Run this line of code & see what happens.

"""

To correct the error, use the 'str' command gotten from 'string' to convert, that is;

*str(current_year)* to a string and rerun the code above.

"""



# Example 3.

""" Lets create another variable called 'birth_year' ,

where we would ask for the year you were born. (use the input command ),

Do you remember the input command ??

"""

birth_year = input("What year were you born?: ") # put your birth year

print(birth_year)  #Run code 


## Get AGE: To get your age, we would subtract your birth year from current year.

age = current_year - birth_year

print(age) #lets Run this code and see what happens.

"""

- > Recall int and str dont work together,

    unless you convert them to either 'int and int' or 'str and str'.

- > To correct the error, use the 'int' command gotten from 'Integer number',

    to convert string to integer;

    write; *birth_year= int(birth_year), below the input command* and rerun the code above.

"""

# Example 3. continuation on age

birth_year = input("What year were you born?") # old code

birth_year  = int(birth_year) # new code

age = current_year - birth_year # old code

print("This year you are turning - "+ str( age ))#Displays a sentence that tells you your age


## Different Datatype: Boolean datatype (True or False): 
"""
- > Do you know what is a datatype??

    - > A datatype in python tells the type of data that a variable can store,

        that is strings and integers etc

        Example; name = "Alex is smart"... This tells python, that it is a string datatype.

- > Do you know what is a Boolean datatype??

    - > A boolean datatype: This represents a value of either 'True or False'.

        It is used to check if something is True, in logical expressions like (>, <, ==)
 
"""

# Example 4: Let's create a boolean variable and check if the expressions is 'True'

boolean = 5 > 3 

print(boolean) # Run the code to check if the expression is correct


# Example 5. Now let’s check if the expression is 'False'(i.e if it is wrong):

boolean = 6 < 1 

print(boolean)


#Example6: lets add a boolean and a string value, make sure to convert boolean to string(str):

print("First result:" + str(boolean)) 


### DIFFERENT WAY TO WRITE STRINGS:

"""
 - > There are other ways to write strings,

     without using concatenation i.e (addition symbol)
     
 - > New method in adding strings is called 'F-LINES':

     To do this, we put f before the quotes( i.e f"")
     
     and place the variable that we want to add to the F-line in curly braces

     (example; print(f"I want to visit {city} next year")

      - > This method is easy because we don't have to,

         directly convert numbers to include them in a string:

    """
         
# Example 7

print(f"I want to visit {city} in {current_year+1} ")




### SECOND PART OF THE LESSON: PERIMETERS AND AREAS OF FIGURES

"""
Here, we will create;

- > A separate geometry program: Do you know what a geometry is?

      - > (Geometry is a part of mathematics that measures angles, shapes,

           sizes of different things we see everyday e.g;

           doors, bed, chairs and many more) -
   
- > Here we want to use geomerty for calculating the

    areas, perimeters of squares and rectangles.
    
"""


##### LET US SOLVE EXPLES RELATED ON SQUARES

#### First, Let us get the square side - we would ask the length of its sides.

square_side = input("Enter the length side of the square: ")
print(square_side) # can you fix the error?

# Fixing the error
square_side = int(square_side) # Let us Convert the string value (square_side) to a number:
print(square_side)

### QUESTION 1. Let us Calculate the perimeter of the square:
perimeter = square_side * 4
# lets use the 'f-string' to display our result
print(f"The perimeter of a square with side {square_side} is {perimeter}") 

### QUESTION 2. Now let's calculate the area of ​​the square:
area = square_side * square_side 
# lets use the 'f-string' to display our result
print(f"The area of ​​a square with side {square_side} is {area}")



##### LET US SOLVE EXPLES ON RECTANGLES

#### First, Let us get the Rectangle sides - we would ask the length of its sides.

# For First rectangle side
rectangle_side1 = input("Enter the length of the first side of the rectangle: ")
# Before we display our results, let us Convert the values ​​to numbers:
rectangle_side1=int(rectangle_side1)
print(rectangle_side1)


# For Second rectangle side.
rectangle_side2 = input("Enter the length of the second side of the rectangle: ")         
# Before we display our results, let us Convert the values ​​to numbers:
rectangle_side2=int(rectangle_side2)
print(rectangle_side2)

# QUESTION 1. Let us calculate the perimeter and display its value:
perimeter = (rectangle_side1+rectangle_side2)*2 
print(f"The perimeter of a rectangle with sides {rectangle_side1} and {rectangle_side2} is {perimeter}")


# QUESTION 2. let us also calculate and display the area:
area = rectangle_side1*rectangle_side2 
print(f"The area of ​​a rectangle with sides {rectangle_side1} and {rectangle_side2} is {area}")



##### FINAL STAGE OF THE LESSON

"""

Here we want to calculate the Diagonal of a square and rectangle.

- > Do you know what a diagonal in mathematics is?

    - > it is a straight part of a line that connects two non-adjacent

        (i.e different sides) vertces of a polygon,

        usually inside a shape.

- > GOAL:  To create a separate geometry program

           - for calculating the areas and perimeters of squares and rectangles.

"""
##### 1. ADD A PYTHON LIBRARY;

## Do you know what a Python library is used for?
## Do you know the python statement we use to get get a python library

import math # import the functions of mathematics from python library

#### 2.  NOW LET US CALCULATE THE DIAGONAL FOR A SQUARE:

# Type;
diagonal = math.sqrt(2*square_side*square_side)
# let us use the f-string to display the result:
print(f"The diagonal of a square with side {square_side} is {diagonal}")

#### 3.  NOW WE CAN CALCULATE THE DIAGONAL FOR A RECTANGLE: 
diagonal = math.sqrt(rectangle_side1*rectangle_side1+rectangle_side2*rectangle_side2) 

print(f"The diagonal of a rectangle with sides {rectangle_side1} and {rectangle_side2} is {diagonal}")


##### HOMEWORK
"""
1. Add to the program the input of the length of the base and the height of the triangle and

   calculate the area of ​​the triangle using the formula: S=(b*h)/2 ,

   where S is the area of ​​the triangle;

   b - side-base of the triangle; h is the height of the triangle.

2. Increased complexity: add to the program the input of the lengths of the

   sides of the triangle and calculate the area using the formula:

   S= √ (p * (p - a)*(p - b)*(p - c)) , where S is the area of ​​the triangle;

   p - semi-perimeter of the triangle, p=(a+b+c)/2 ; a,b,c -

   lengths of the sides of the triangle.

   To calculate the square root, use math.sqrt from the math library.

3. Print the line f "Programming is very interesting. After all,

                     only in programming you can add truth to truth and get {True+True}."


"""
