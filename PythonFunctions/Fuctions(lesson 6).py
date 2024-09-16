##def say_hello():
##    print("Hello")
##
##say_hello()
##
##say_hello()

def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Sophia")

say_hello("John")

say_hello("Jane")

say_hello("Peter")

#   Taking one parameter
def area_square(side):
    area = side * side
    print(f"The area of ​​the square with side {side} = {area}")


area_square(5)

area_square(7)


# Taking two parameter
def area_rectangle(side_a, side_b):
    area = side_a * side_b
    print(f"The area of ​​the rectangle with sides {side_a} and {side_b} = {area}" )

area_rectangle(2, 4)

area_rectangle(4, 6)

#Returning function
import random
def lottery():
    tickets = [13,54,23,1,5,3]
    ticket = random.choice(tickets)
    return ticket

winner = lottery()
print(f"Winning tiket # - {winner}")


# return multiple values
def multi_lottery():
    tickets = [13, 54, 23, 1, 5, 3]
    ticket1 = random.choice(tickets)
    ticket2 = random.choice(tickets)
    return ticket1, ticket2

first_winner, second_winner = multi_lottery()
print(f"Winning tickets - {first_winner} and {second_winner}")


# Eliminate repetitions from multiple functio values
def multi_lottery():
    tickets = [13, 54, 23, 1, 5, 3]
    ticket1 = random.choice(tickets)
    tickets.remove(ticket1)
    ticket2 = random.choice(tickets)
    return ticket1, ticket2

first_winner, second_winner = multi_lottery()
print(f"Winning tickets - {first_winner} and {second_winner}")


## Receiving and returning functions at the same time
def factorial(n):
    result = 1
    for I in range(1, n+1):
        result *= I
    return result

# call function
print(f"Factorial 5 = {factorial(5)}")


## Now let's calculate the factorial for all numbers from 1 to 10, using a loop
for i in range(1, 11):
    print(f"Factorial {i} = {factorial(i)}")


# Lambda Function
sum = lambda a: a*a

print(sum(2))

# Multiple lambda function
sum = lambda a, b: a*b

print(sum(2, 4))

# Assignment try
smallest = lambda a, b, c: min(a, b, c)
smallest = smallest(5, 4, -1)
print(f"The smallest number is: {smallest}")


##find_smallest = lambda num1, num2, num3: min(num1, num2, num3)
##
### Example usage
##smallest_number = find_smallest(5, -2, 3)
##print(f"The smallest number is: {smallest_number}")
