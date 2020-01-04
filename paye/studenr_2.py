from tkinter import *
from pymongo import MongoClient

root = Tk()
frame_1 = Frame(root)
label_1 = Label(frame_1, text='Search')
entry_search = Entry(frame_1, bd=5)
btn_search = Button(frame_1, text='Search', command=set)

entry_new_name = Entry(root)
entry_new_fname = Entry(root)
btn_notify = Button(root, text='Update')
label_1.pack(side=LEFT)
entry_search.pack(side=LEFT)
btn_search.pack(side=LEFT)

frame_1.pack()
entry_new_name.pack()
entry_new_fname.pack()
btn_notify.pack()