### Make a list of 3 cells with 3 symbols
area = ["*","*","*"]
##
##area[0] = "X"
##
##area[1] = "0"
##for cell in area:
##    print(cell)
##
### Make a standard field 3 by 3. To do this, make a list of three mini-fields:
area = [["*","*","*"],["*","*","*"],["*","*","*"]]
##
##area[0][2] = "X" 
##
##area[2][1] = "0"
##for cell in area:
##    print(cell)



# Create a function of all possible combination
def check_winner():

    if area[0][0] == "x" and area[0][1] == "x" and area[0][2] == "x":

        return "x"

    if area[1][0] == "x" and area[1][1] == "x" and area[1][2] == "x":

        return "x"

    if area[2][0] == "x" and area[2][1] == "x" and area[2][2] == "x":

        return "x"

    if area[0][0] == "x" and area[1][0] == "x" and area[2][0] == "x":

        return "x"

    if area[0][1] == "x" and area[1][1] == "x" and area[2][1] == "x":

        return "x"

    if area[0][2] == "x" and area[1][2] == "x" and area[2][2] == "x":

        return "x"

    if area[0][0] == "x" and area[1][1] == "x" and area[2][2] == "x":

        return "x"

    if area[0][2] == "x" and area[1][1] == "x" and area[2][0] == "x":

        return "x"

    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":

        return "0"

    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":

        return "0"

    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":

        return "0"

    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":

        return "0"

    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":

        return "0"

    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":

        return "0"

    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":

        return "0"

    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":

        return "0"

    return "*"

# Making a cell selection and including a loop

for turn in range(1,10):
    print(f"Turn: {turn}")
    row = input("Enter the row number(0, 1 or 2): ")
    row = int(row)

    column = input("Enter the column number(0, 1 or 2): ") 

    column=int(column)

    # check the parity using the remainder of dividing turn by 2 if the remainder is zero:
    if turn % 2 == 0:
        turn_char = "0"
        print("Turn of zero")
    # Otherwise  the remainder of the division is not equal to 0, the number is odd (Cross turn)
    else:
        turn_char = "x"
        print("Turn of cross")
    

    ## Fill cell at their intersection
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("The cell is already occupied, you miss a turn")
        if turn == 9:
            print("Tie")
        continue
    for cell in area:
        print(cell)
    if check_winner() == "x":
        print("The victory of the crosses")
        break
    if check_winner() == "0":
        print("The victory of the zeroes")
        break
    if turn == 9 and check_winner() == "*":
        print("Tie")
    ## Determining winner
