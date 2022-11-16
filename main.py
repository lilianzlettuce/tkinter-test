import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def import_data():
    global v
    file_path = askopenfilename(title='Select A File')
    print(file_path)
    v.set(file_path)

    global gamesPlayed
    gamesPlayed.set(10)
    global avgDur
    avgDur.set('4.5 hrs')
    global type
    type.set('Strategy')
    global idk
    idk.set('idk')

    df = pd.read_json(file_path)

root = tk.Tk(className='File Reader')
root.geometry("900x600")

frame = tk.Frame(root).grid(row=0, column=0, padx=70, pady=50)

# file opening frame
fileFrame = tk.Frame(frame).grid(row=0, column=0, padx=0, pady=20)

tk.Button(fileFrame, text='Open File', command=import_data).grid(row=2, column=1, pady=5)
v = tk.StringVar()
entry = tk.Label(fileFrame, textvariable=v, width="50", bg="gray80", anchor="w").grid(row=2, column=2)

# stats frame
statsFrame = tk.Frame(frame).grid(row=3, column=0, padx=70, pady=30)

tk.Label(statsFrame, text='Summary').grid(row=5, column=1, pady=10, sticky=E)

tk.Label(statsFrame, text='Games Played:').grid(row=6, column=1, pady=0, sticky=E)
gamesPlayed = tk.StringVar()
tk.Label(fileFrame, textvariable=gamesPlayed, width="15", anchor="w").grid(row=6, column=2, sticky=W)
tk.Label(statsFrame, text='Average Duration:').grid(row=7, column=1, pady=0, sticky=E)
avgDur = tk.StringVar()
tk.Label(fileFrame, textvariable=avgDur, width="15", anchor="w").grid(row=7, column=2, sticky=W)
tk.Label(statsFrame, text='Type:').grid(row=8, column=1, pady=0, sticky=E)
type = tk.StringVar()
tk.Label(fileFrame, textvariable=type, width="15", anchor="w").grid(row=8, column=2, sticky=W)
tk.Label(statsFrame, text='Idk:').grid(row=9, column=1, pady=0, sticky=E)
idk = tk.StringVar()
tk.Label(fileFrame, textvariable=idk, width="15", anchor="w").grid(row=9, column=2, sticky=W)

# graph button

def graphSomething():
    fakeData = np.random.normal(200000, 25000, 5000)
    plt.hist(fakeData, 100)
    plt.show()

tk.Button(fileFrame, text='Graph', command=graphSomething).grid(row=4, column=1, pady=5)

# dropdown frame
dropdownFrame = tk.Frame(frame).grid(row=10, column=0, padx=70, pady=30)

def runFunc():
    if clicked.get() == "Function 1" :
        func1()
    elif clicked.get() == "Function 2" :
        func2()

def func1():
    # new window
    top = tk.Toplevel(root)
    top.title('Enter Parameters')
    top.geometry("400x300")

    tk.Label(top, text=clicked.get()).grid(row=0, column=2, padx=30, pady=20, sticky=W)

    tk.Label(top, text='Margin:').grid(row=1, column=1, padx=30, pady=10, sticky=E)
    p1 = Entry(top, width=20)
    p1.grid(row=1, column=2)
    tk.Label(top, text='Other Param:').grid(row=2, padx=30, pady=10, column=1, sticky=E)
    p2 = tk.Entry(top, width=20)
    p2.grid(row=2, column=2)
    tk.Label(top, text='Blah:').grid(row=3, padx=30, pady=10, column=1, sticky=E)
    p3 = tk.Entry(top, width=20)
    p3.grid(row=3, column=2)

    def clearFields():
        p1.delete(0, END)
        p2.delete(0, END)
        p3.delete(0, END)

    tk.Button(top, text="Enter").grid(row=4, padx=30, pady=10, column=1, sticky=E)
    tk.Button(top, text="Clear Fields", command=clearFields).grid(row=4,column=2, sticky=W)
    tk.Button(top, text="Graph", command=graphSomething).grid(row=4, column=2, sticky=E)
    
    top.grab_set()

def func2():
    # new window
    top = tk.Toplevel(root)
    top.title('Enter Parameters')
    top.geometry("400x200")

    tk.Label(top, text=clicked.get()).grid(row=0, column=2, padx=30, pady=20, sticky=W)

    tk.Label(top, text='Margin:').grid(row=1, column=1, padx=30, pady=10, sticky=E)
    tk.Entry(top).grid(row=1, column=2)
    tk.Label(top, text='Other Param:').grid(row=2, padx=30, pady=10, column=1, sticky=E)
    tk.Entry(top).grid(row=2, column=2)
    tk.Label(top, text='Blah:').grid(row=3, padx=30, pady=10, column=1, sticky=E)
    tk.Entry(top).grid(row=3, column=2)

    top.grab_set()

# Dropdown menu options
options = [
    "Function 1",
    "Function 2",
    "Function 3",
    "Function 4"
]

# dropdown menu
clicked = StringVar()
clicked.set("Function 1")
drop = OptionMenu(dropdownFrame, clicked, *options).grid(row=11, column=1)
runFuncBtn = tk.Button(dropdownFrame, text = "Run Function" , command = runFunc ).grid(row=12, column=1)



root.mainloop()