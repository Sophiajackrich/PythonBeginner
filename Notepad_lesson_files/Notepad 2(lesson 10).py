### open and reading files using "with open....as" and "read command"
##with open("games.txt") as file:
##    print(file.read())
##
### open files using "with open....as" and "a for loop"
##with open("games.txt") as file:
##    for line in file:
##        print(f"My favorite programming game is: {line}")
##
### writing to an empty file
##with open("blank.txt", "w") as file:
##    file.write("It’s already a new text")
##
### Appending to an existing file file
##with open("blank.txt", "a") as file:
##    file.write("\nI am appending a new line of text")
##with open("blank.txt") as file:
##    print(file.read())
##
### Example 2.
##with open("blank.txt", "a") as file:
##    file.write("\nMy students are blessed")
##with open("blank.txt") as file:
##    print(file.read())
##
##
##
##
### Using a new library - The tkinter.filedialog library
import tkinter.filedialog as tfd


### Creating a notepad widget with function of open and read file
import tkinter as tk
window = tk.Tk()
window.geometry("400x400")
window.title("My notepad")
context_text = tk.Text(window, wrap="word")
context_text.place(x=0, y=0, relwidth=1, relheight=1)

main_menu = tk.Menu(window)

window.configure(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)

main_menu.add_cascade(label="File", menu=file_menu)


### function for opening file
def open_file():
    context_text.delete(1.0, "end")
    file_name = tfd.askopenfilename()
    with open(file_name) as file:
        context_text.insert(1.0, file.read())
        context_text.delete(1.0, "end")

### for "open file"
open_file_icon =tk.PhotoImage(file="200w.gif")

file_menu.add_command(label="Open", image=open_file_icon, compound="right", command = open_file)




### Using function and python library to get file to "save as"
def save_as_file():
    file_name = tfd.asksaveasfilename()
    content = context_text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)

### for "save as"
save_as_file_icon = tk.PhotoImage(file="200w(1).gif")     
file_menu.add_command(label="Save as", image=save_as_file_icon, compound="right", command=save_as_file)



### Using function and python library to get file to "save"
def save_file():
    save_as_file()


save_file_icon = tk.PhotoImage(file="200w(1).gif")
file_menu.add_command (label="Save", image=save_file_icon, compound="right", command = save_file)




### Creating function for a new file
##def new_file():
##    file_name =  tfd.asksaveasfilename()
##    content = context_text.get(1.0, "end")
##    with open(file_name, "w") as file:
##        file.write(content)



##
##
###Global and local variable
##
##color = "red" 
##
##def function():
##    shape = "circle"
##    global color
##    color="green"
##    print(f"Inside the function the color is - "+color)
##print(f"In the main program the color is- "+color)
##
##result = function()
####print(color)
##print(result)
##
##print("In the main program the color is - "+color)
##

# Global "file_name" variable
window.title("My notepad")

file_name = ""

    
def open_file():
    context_text.delete(1.0, "end")
    global file_name
    file_name = tk.filedialog.askopenfilename()
    with open(file_name) as file:
        context_text.insert(1.0, file.read())



##def save_as_file():
##
##    global file_name 
##
##    file_name = tk.filedialog.asksaveasfilename() 
##
##    content = context_text.get(1.0, "end") 
##
##    with open(file_name, "w") as file:
##        file.write(content)
##
##
##
##
##def save_file():
##    global file_name
##    save_as_file()
##
##
###Correcting the "Save" function
##def save_file():
##    global file_name
##    if file_name=="":
##        save_as_file() 
##
##    else:
##        content = context_text.get(1.0, "end")
##        with open(file_name, "w") as file:
##            file.write(content)







# Supplementing the "new_file" function
import tkinter.filedialog as tfd

import tkinter.messagebox as tkm

def new_file(): 

    global file_name
    if tkm.askokcancel("Creating a new file,"
                       "Are you sure? Unsaved text will be deleted "):

     file_name = ""
         
     context_text.delete(1.0, "end")

new_file_icon = tk.PhotoImage(file='Upward - GIPHY Clips_files/200w(2).gif')
file_menu.add_command(label="New File", image=new_file_icon, compound="right", command=new_file)


def write_to_file(file_name):
    content = content_text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)


# call "write_to_file" function in the "save as and save" functions and replace their values
def save_as_file():

    global file_name

    file_name = tk.filedialog.asksaveasfilename()

    write_to_file(file_name)


def save_file(): 

    global file_name 

    if file_name=="": 

        save_as_file() 

    else: 

        write_to_file(file_name)

## The Open File Function

# making inscription on the window to display info on which file is currently open
file_label = tk.Label(window, text = "File: "+file_name)


# Placing the inscription
file_label.place(relx=0, rely=1, anchor="sw")

# adding the inscription to the following functions
def open_file():
    context_text.delete(1.0, "end")
    global file_name

    file_name = tfd.askopenfilename()

    file_label["text"] = "File: "+file_name

    with open(file_name) as file:
        context_text.insert(1.0, file.read())


# for save as file
def save_as_file():

    global file_name

    file_name = tk.filedialog.asksaveasfilename()

    file_label["text"] = "File: " + file_name

    write_to_file(file_name)


def new_file():

    global file_name

    if tkm.askokcancel("Saving a new file?", "Are you sure? Unsaved text will be deleted"):

        file_name = ""

        file_label["text"] ="File: "+ file_name

        context_text.delete(1.0, "end")

window.mainloop()
