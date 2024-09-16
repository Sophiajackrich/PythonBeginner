import tkinter as tk

window = tk.Tk()
window.title("My notepad")
window.geometry("400x400")

context_text = tk.Text(window, wrap="word")
context_text.place(x=0, y=0, relwidth=1, relheight=1)

main_menu = tk.Menu(window)
window.configure(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)

new_file_icon = tk.PhotoImage(file='Upward - GIPHY Clips_files/200w(2).gif')
file_menu.add_command(label="New File", image=new_file_icon, compound="right")

open_file_icon =tk.PhotoImage(file="Upward - GIPHY Clips_files/200w.gif")
file_menu.add_command(label="Open File", image=open_file_icon, compound="right")

save_file_icon = tk.PhotoImage(file="200w(1).gif")
file_menu.add_command(label="Save",image=save_file_icon, compound="right")

window.mainloop()
