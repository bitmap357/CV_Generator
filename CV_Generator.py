from tkinter import *

window = Tk()
window.title("CV Generator")

label_name = Label(window, text="Name: ")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email = Label(window, text="Email: ")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()


window.mainloop()
