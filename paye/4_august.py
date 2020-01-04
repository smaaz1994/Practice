from tkinter import *
from tkinter import messagebox

entry_name = None
entry_fname = None

def save_student():
    messagebox.showinfo('Confirmation',entry_name.get())

root = Tk()
frame_1 = Frame(root)
lbl_name = Label(frame_1, text="Student's Name")
lbl_name.pack(side=LEFT)
entry_name = 
frame_1.pack()

frame_2 = Frame(root)
lbl_fname = Label(frame_2, text="Student's Name")
lbl_fname.pack(side=LEFT)
frame_2.pack()
