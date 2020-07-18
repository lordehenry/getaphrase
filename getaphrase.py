#Get a phrase for english students
#Author: Vinicius Silva da Cruz - Lordehenry
#Git: github.com/lordehenry


from tkinter import *
import tkinter
import random

#putting the txt in a list
names=[line.strip() for line in open('words.txt')]
teens=[line.strip() for line in open('teens.csv')]
kids=[line.strip() for line in open('kids.csv')]

#a function that will pick (and display) a word.
def pickWord():
    nameLabel.configure(text=random.choice(names))
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
pickButton = tkinter.Button(text="Pick!", command=pickWord)
pickButton.pack()
pickButton.place(relx=0.5, rely=0.6, anchor=CENTER)

#start the GUI
root.mainloop()
