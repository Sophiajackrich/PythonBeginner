##print(5)
##print(5+5)
##print('Hello world')
##print('Hello world' + ' from Yana')
##
##name = 'its Yana'
##print('Hello world ' + name)
##
##
##name = 9
##print('Hello world ' + name)

# Input command
##user_name = input('Enter your name: ')
##print(user_name)

##print('The computer thought of a number from 1 - 10. Try to guess it')
##secret_number = 8
##print('Computer number: ', str(secret_number))
##user_number = int(input('Enter your number: '))
##print(user_number)
##
##if secret_number > user_number:
##    print('secret_number is greater than user_number')
##
##if secret_number < user_number:
##    print('secret_number is less than user_number')
##
##if secret_number == user_number:
##    print('You got it')

# Add library
print('The computer thought of a random number from 1 - 10. Try to guess it')
import random
secret_number = random.randint(1,10)
user_number = int(input('Enter your number: '))
print(user_number)

if secret_number > user_number:
    print('secret_number is greater than user_number')

if secret_number < user_number:
    print('secret_number is less than user_number')

if secret_number == user_number:
    print('You got it')

# Duplicate code
secret_number = random.randint(1,10)
user_number = int(input('Enter your number: '))
print(user_number)

if secret_number > user_number:
    print('secret_number is greater than user_number')

if secret_number < user_number:
    print('secret_number is less than user_number')

if secret_number == user_number:
    print('You got it')


