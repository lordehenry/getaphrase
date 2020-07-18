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
def pickWordTeens():
    nameLabel.configure(text=random.choice(teens))
def pickWordKids():
    nameLabel.configure(text=random.choice(kids))
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
pickButton = tkinter.Button(text="Pick Teens!", command=pickWordTeens)
pickButton.pack()
pickButton.place(relx=0.3, rely=0.9, anchor=CENTER)

#add a label for displaying the name.
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()
nameLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
#add a 'pick name' button
pickButton = tkinter.Button(text="Pick Kids!", command=pickWordKids)
pickButton.pack()
pickButton.place(relx=0.6, rely=0.9, anchor=CENTER)

#start the GUI
root.mainloop()
