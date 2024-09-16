## Python loops: Python has two primitive loops("while" & "For")
#Starting with a while loop
 This loop repeats a set of statements untill a condition is met.

 E.g: create a variable counter:
counter = 7
# while loop when counter > 0
while counter > 0:
    print(counter, end="")
    counter = counter - 1

print()
# E.g.2: change counter value
counter = 10
# while loop when counter > 0
while counter > 0:
    print(counter, end="")
    counter = counter - 2   
print()


 INFINITE LOOP:
 This is a loop that goes on forever aslong as the condition is true.
 E.g of an infinite loop
while True:
    print("It's an infinite loop")


# STOP AND CONTINUE IN LOOPS
# BREAK/STOP
# To be able to interrupt or stop infinite loops, we use a command called "break"
while True:
    print("It's an infinite loop")
    stop = input("Stop the loop? (yes/no): ")
    if stop == "yes":
        print("The loop is stopped")
        break

# CONTINUE command
##New command called "continue" can be used to stop present iteration and
##continue with the next iteration

counter = 0 

while counter < 10:

    counter += 1

    print(counter)

print()
print()

#Example 2:
counter = 0 

while counter < 10:

    counter += 1
    if counter % 2 == 0:
        continue

    print(counter)


# FOR LOOP
## in this loop, the number of repetitions is set by a sequence - numbers or symbols.

### Example 1.

word = "cuckoo" 

for char in word:
    print(char, end="")

print()

# Example 2: create a numeric sequence using "I" variable
## N/b: i.   One repetition of code in the loop is called an iteration
###     ii.  A variable in a "For loop" is called an iterator,
###            so a variable is often named as "i".
###     iii. To create a numerical sequence, we use the " range " command.

for i in range(5):
    print("Hello")

# Now, print the variable i to see what values ​​it takes

for i in range(5):
    print(i) # this counts from 0 for us by default

# lets set the range to count from 1, instead of 0
for i in range( 1, 5):
    print(i) # when we specify a range, the last number isnt included




# MAKING A PIGGY BANK PROGRAM
## create a seperate python file, name it moneybox.py.
## This is to cal. our savings and understand how long we will be able to accumulate the desired amount.

print ("This is a program for calculating your savings.")

# let's create a variable for savings to know how much is saved so far
saved_dollars = input("How much have you saved up so far?") 

saved_dollars = int(saved_dollars) # convert string to integer

# let's create a variable in which we specify how much we plan to save each day.
added_dollars = input("How much do you plan to save each day?") 

added_dollars = int(added_dollars) # convert string to integer

# let's set how many days we will calculate the savings
days = input("How many days will we calculate for?")

days = int(days)


# print
print(f"You already have {saved_dollars} dollars.")

# print
print(f"If you save {added_dollars} dollars every day, then in {days} days...")

# create a loop to find out how much will accumulate during this time
for i in range(days):
    saved_dollars = saved_dollars + added_dollars
    print(f"Day {i}, amount - {saved_dollars}")
print(f"... you will save up {saved_dollars} dollars!")

# GOAL CREATION
#Now, let's create a Goal to accumulate some specific amount
goal = input("How much do you want to save?") 
goal = int(goal)

saved_dollars = input("How much have you saved up so far?") 
saved_dollars = int(saved_dollars)

added_dollars = input("How much do you plan to save each day?") 
added_dollars = int(added_dollars)

days = 0
# using a while loop, because we dont have the exact no of repetitions
while goal > saved_dollars:
    saved_dollars = saved_dollars + added_dollars
    days = days + 1
    print(f"Day {days}, amount - {saved_dollars}")
print()
print(f"You will save {goal} dollars in {days} days")



# HOMEWORK

## Write a program that counts the sum of the numbers from 1 to 20 (inclusive)
## Write a program that counts the sum of all odd numbers from 0 to 10.
## Write a program that writes "hello" until the answer is "bye."

