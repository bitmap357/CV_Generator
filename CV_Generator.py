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

label_phone = Label(window, text="Phone: ")
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()

label_address = Label(window, text="Address: ")
label_address.pack()
entry_address = Entry(window)
entry_address.pack()


window.mainloop()
