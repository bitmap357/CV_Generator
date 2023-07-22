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

label_website = Label(window, text="Website: ")
label_website.pack()
entry_website = Entry(window)
entry_website.pack()

label_skills = Label(window, text="Skills(Enter one skill per line)")
label_skills.pack()
entry_skills = Text(window, height=5)
entry_skills.pack()

label_education = Label(window, text="Education(Enter one per line in format 'Degree':'University')")
label_education.pack()
entry_education = Text(window, height=5)
entry_education.pack()


label_experience = Label(window, text="Experience(Enter one per line in format 'Job Title':'Description')")
label_experience.pack()
entry_experience = Text(window, height=5)
entry_experience.pack()

window.mainloop()
