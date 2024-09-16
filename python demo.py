##print(5)
##print(5+5)
##print(5*5)
##print("Hello Dad, its Yana")
##print("Hello Dad" + " its Yana")
##print("Yana" + " Loves Python!")
##
##
##name = "Yana"
##
##print(name + " is very gorgeous!")

# Input command
##username = input("Enter your name: ")
##print(username)

# A computer thought of a number from 1 - 10. Try to guess it.
##secret_number = 7
##user_number = int(input("Enter your number: "))
##print(user_number)
##if secret_number > user_number:
##    print("Secret number greater than user number")
##if secret_number < user_number:
##    print("Secret number less than user number")
##if secret_number == user_number:
##    print("You got it!")


# Add a library
import random

##print("A computer thought of a number from 1 - 10. Try to guess it.")
##secret_number = random.randint(1,10)
##user_number = int(input("Enter your number: "))
##print(user_number)
##if secret_number > user_number:
##    print("Secret number greater than user number")
##if secret_number < user_number:
##    print("Secret number less than user number")
##if secret_number == user_number:
##    print("You got it!")
##
### Duplicate
##import random
##secret_number = random.randint(1,10)
##user_number = int(input("Enter your number: "))
##print(user_number)
##if secret_number > user_number:
##    print("Secret number greater than user number")
##if secret_number < user_number:
##    print("Secret number less than user number")
##if secret_number == user_number:
##    print("You got it!")


# Loops
import math
print("A computer thought of a number from 1 - 10. Try to guess it.")

attempts = 3
while attempts > 0:
    secret_number = random.randint(1,10)
    user_number = int(input("Enter your number: "))
    print(user_number)
    if secret_number > user_number:
        print("Secret number greater than user number")
    if secret_number < user_number:
        print("Secret number less than user number")
    if secret_number == user_number:
        print("You got it!")
        break
    attempts = attempts - 1
    print("Number of attempts left: " + str(attempts))
if attempts == 0:
   print("You failed!")
   print("Secret number is: " + str(secret_number))
