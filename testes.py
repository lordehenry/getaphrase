import csv
from tkinter import *
import tkinter
import random

# Map row to dictionary (dictionary comprehension)
def wordObject(column_names, row):
    return {column_names[column]: data for column, data in enumerate(row) if column < len(column_names)}


# Map CSV file to list of dictionaries (list comprehension)
wordskids = [wordObject(['cod', 'word', 'phrase'], row) for row in csv.reader(open('kidsvirg.csv', 'r'))]
wordsteens = [wordObject(['cod', 'word', 'phrase'], row) for row in csv.reader(open('teens.csv', 'r'))]

# for x in range(wordskids.__len__()):
#     print(wordskids[x]['cod'])
# # for x in range(wordsteens.__len__()):
# #     print(wordsteens[x])

def pickWordKids():
    nameLabel.configure(text=(random.choice(wordskids[1:10])))

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Word Picker")
#set the size.
root.geometry("800x600")

#add a label for displaying the name.
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()
nameLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

#add a 'pick name' button
pickButton = tkinter.Button(text="Pick!", command=pickWordKids)
pickButton.pack()
pickButton.place(relx=0.5, rely=0.6, anchor=CENTER)

#start the GUI
root.mainloop()