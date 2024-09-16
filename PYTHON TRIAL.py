print("A computer thought of a number from 1 - 10. Try to guess it.")
secret_number = 7
user_number = int(input("Enter your number: "))
print(user_number)
if secret_number > user_number:
    print("Secret number greater than user number")
