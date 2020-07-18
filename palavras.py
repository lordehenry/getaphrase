
from tkinter import *
import tkinter
import random


import csv

words = []

with open('kids.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        words.append({'code': int(row[0]), 'word': row[1], 'phrase': row[2:]})

# names = [line.strip() for line in open('words.txt')]
# teens = [line.strip() for line in open('teens.txt')]
kids = [line.strip() for line in open('kids.txt')]

def pickWord():
    nameLabel.configure(text=random.choice(f))

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Word Picker")
#set the size.
root.geometry("420x420")

#add a label for displaying the name.
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()
nameLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

#add a 'pick name' button
pickButton = tkinter.Button(text="Pick!", command=pickWord)
pickButton.pack()
pickButton.place(relx=0.5, rely=0.6, anchor=CENTER)

#start the GUI
root.mainloop()
