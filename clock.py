import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Clock")
root.geometry("750x150+0+0")
root.config(background="black")
def close():
    if messagebox.askokcancel("Close clock", "Do you want to close clock?"):
        root.destroy()
        print("closed")
def start():
    text = time.strftime("%I:%M:%S %p %m/%d/%Y")
    label.config(text=text)
    label.after(200, start)
label = Label(root, font=("ds-digital", 50, "bold"), bg="black", fg="yellow", bd=50)
label2 = Label(root, font=("ds-digital", 50, "bold"), bg="black", fg="yellow", bd=50)
label.grid(row=0, column=1)
start()
print("started")
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()