import tkinter as tk

import tkinter.messagebox as tkm 

window = tk.Tk()

window.title("Tic-tac-toe") 

window.geometry("300x300")

window.resizable(False, False)

area = []

turn=1

# Function for checking winner or tie

def winner():

    if area[0][0]["text"] == "X" and area[0][1]["text"] == "X" and area[0][2]["text"] == "X":

        return "X"

    if area[1][0]["text"] == "X" and area[1][1]["text"] == "X" and area[1][2]["text"] == "X":

        return "X"

    if area[2][0]["text"] == "X" and area[2][1]["text"] == "X" and area[2][2]["text"] == "X":

        return "X"

    if area[0][0]["text"] == "X" and area[1][0]["text"] == "X" and area[2][0]["text"] == "X":

        return "X"

    if area[0][1]["text"] == "X" and area[1][1]["text"] == "X" and area[2][1]["text"] == "X":

        return "X"

    if area[0][2]["text"] == "X" and area[1][2]["text"] == "X" and area[2][2]["text"] == "X":

        return "X"

    if area[0][0]["text"] == "X" and area[1][1]["text"] == "X" and area[2][2]["text"] == "X":

        return "X"

    if area[0][2]["text"] == "X" and area[1][1]["text"] == "X" and area[2][0]["text"] == "X":

        return "X"

    if area[0][0]["text"] == "0" and area[0][1]["text"] == "0" and area[0][2]["text"] == "0":

        return "0"

    if area[1][0]["text"] == "0" and area[1][1]["text"] == "0" and area[1][2]["text"] == "0":

        return "0"

    if area[2][0]["text"] == "0" and area[2][1]["text"] == "0" and area[2][2]["text"] == "0":

        return "0"

    if area[0][0]["text"] == "0" and area[1][0]["text"] == "0" and area[2][0]["text"] == "0":

        return "0"

    if area[0][1]["text"] == "0" and area[1][1]["text"] == "0" and area[2][1]["text"] == "0":

        return "0"

    if area[0][2]["text"] == "0" and area[1][2]["text"] == "0" and area[2][2]["text"] == "0":

        return "0"

    if area[0][0]["text"] == "0" and area[1][1]["text"] == "0" and area[2][2]["text"] == "0":

        return "0"

    if area[0][2]["text"] == "0" and area[1][1]["text"] == "0" and area[2][0]["text"] == "0":

        return "0"

    return ""

# Function for starting a new game, after a win or loss
def new_game():

    global area, turn

    turn = 1

    for x in range(3):

        for y in range(3):

            area[x][y]["text"] = "" 


# Function for designing and operating buttons
def push(button): 
    global turn

    print(turn)
    if turn % 2 == 0:

        turn_char = "0"

    else:

        turn_char = "X"

    print(f"Make a turn {turn_char}")

    if button["text"] is "":

        button["text"] = turn_char

        turn+=1
        if winner() == "X":

            print("The winner is X")
            tkm.showinfo(title="Winner", message="The winners are X")
            new_game()

        if winner() == "0":

            print("The winner is 0")
            tkm.showinfo(title="Winner", message="The winners are 0")
            new_game()

        if winner() == "" and turn == 10:

            print("Tie")
            tkm.showinfo(title="Game over", message="Tie")
            new_game()

for x in range(3):
    area.append([])
    for y in range(3):

        button = tk.Button(window, text="", width=13, height=6)

        area[x].append(button)

        area[x][y].place(x=x*100, y=y*100)
        area[x][y]["command"]=lambda selected_button=button: push(selected_button) 

print(area)  

window.mainloop()
