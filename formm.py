from tkinter import *
from tkinter import messagebox

def valcheck():
    name = name_entry.get()
    passw = pwdentry.get()
    if name == "abc" and passw == "123":
        messagebox.showinfo("Answer", "Valid Input!")
    else:
        messagebox.showinfo("Answer", "Invalid Input.")

root = Tk()
root.geometry("250x250")
root.title("Registration Form")
root.configure(bg="#FFE4E1") 

heading_label = Label(text="Login Page", font=('bold', 12), bg="#FFE4E1")  
heading_label.place(x=60, y=25)

name_label = Label(root, text="User ID", bg="#FFE4E1")
name_label.place(x=30, y=60)
name_entry = Entry(root)
name_entry.place(x=95, y=60)

pwd = Label(root, text="Password", bg="#FFE4E1")
pwd.place(x=30, y=80)
pwdentry = Entry(root)
pwdentry.place(x=95, y=80)

submit_button = Button(root, text="Submit", command=valcheck, fg="black", bg="#4CAF50", bd=0) 
submit_button.place(x=10, y=110)

root.mainloop()
