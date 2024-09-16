word = "wolverine"
letters = []
attempts = 3
while attempts > 0:
    victory = True
    message = input("Write the letter: ")
    letters.append(message)
    print(letters)
    for char in word:
        if char in letters:
            print(char, end = " ")
            
        
        else:
            print("X", end = " ")
            victory = False
    print()

    if message not in word:
        attempts = attempts - 1
        print ("There is no such letter in the word. You have so many attempts left: "+ str(attempts))
        if attempts == 0:
            print()
            print("You've lost!")

    
    if victory == True:
        print("You won!")
        break


# The issue was alot. Look closely at the code, i would be sending a video along to explain everything.

