import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

window = tk.Tk()
window.geometry("400x400")
window.title("My Notepad")

file_name = ""

def write_to_file(file_name):
    content = content_text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)

def open_file():
    content_text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    file_label["text"] = "File: "+file_name
    with open(file_name) as file:
        content_text.insert(1.0, file.read())
        
def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    file_label["text"] = "File: " + file_name
    write_to_file(file_name)

def save_file():
    global file_name
    if file_name=="":
        save_as_file()
    else:
        write_to_file(file_name)
        #tkm.showinfo("Файл сохранен","Сохранения записаны в файл "+file_name)


def new_file():
    global file_name
    if tkm.askokcancel("Creating a new file,"
                       "Are you sure? Unsaved text will be deleted "):
        file_name = ""
        file_label["text"] = "File: " + file_name
        content_text.delete(1.0, "end")


content_text = tk.Text(window, wrap="word")
content_text.place(relx=0,rely=0, relwidth=1, relheight=1)

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

new_file_icon = tk.PhotoImage(file='Upward - GIPHY Clips_files/200w(2).gif')
open_file_icon = tk.PhotoImage(file="200w.gif")
save_file_icon = tk.PhotoImage(file="200w(1).gif") 

file_menu.add_command(label="New", compound='left', image=new_file_icon, command = new_file)
file_menu.add_command(label="Open", compound='left', image=open_file_icon, command = open_file)
file_menu.add_command(label="Save", compound='left', image=save_file_icon, command = save_file)
file_menu.add_command(label="Save as", compound='left', image=save_file_icon, command = save_as_file)

file_label = tk.Label(window, text="File: "+file_name)
file_label.place(relx=0, rely=1, anchor="sw")

#tkm.showinfo("Добро пожаловать!","Вас приветствует программа\"Мой блокнот\"")
window.mainloop()
