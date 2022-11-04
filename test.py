import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

import pandas as pd

data = pd.read_csv('mountain.csv')

class MyWindow:
    def __init__(self, win) -> None:
        self.lbl1 = Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')

        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract', command=self.sub)

        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)

        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

window = tk.Tk(className='ur mom')
mywin = MyWindow(window)
window.geometry("600x600")

# Code to add widgets will go here...
def msgWarning(): 
    messagebox.showinfo("WARNING", "YOU HAVE ANGERED THE GODS. THERE IS NO SALVATION.")

def msgQuestion():
    messagebox.askquestion("Are you sure about that?", "Are you sure about that?")

def analysis():
    path = filedialog.askopenfilename()
    savename = filedialog.asksaveasfilename()

frame_a = tk.Frame()
frame_a.place(x=0, y=300)

msgBtn = tk.Button(frame_a, text="eat the cheese", command=msgWarning)
msgBtn.pack()

qBtn = tk.Button(frame_a, text="Would you like a free lawnmower?", command=msgQuestion)
qBtn.pack()

fileBtn = tk.Button(frame_a, text='Generate Table', command=analysis)
fileBtn.pack()

button = tk.Button(frame_a, text='Stop', width=25, command=window.destroy)
button.pack()

window.mainloop()