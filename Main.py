from tkinter import *
import tkinter.messagebox 
from PvsCPU import game

def gameStart():
    box.destroy()
    game()
# creates a tkinter box window 
box = tkinter.Tk() 
 
# box window title and dimension 
box.title("Simple Wordle Version 1.0.0") 
box.geometry('500x300') 

Title = Label(box, text="Welcome to Simple Wordle!")
Title.pack()

Cpu_Button = tkinter.Button(box, text="1 vs 1", width=25, command=gameStart)
Cpu_Button.pack()

box.mainloop()