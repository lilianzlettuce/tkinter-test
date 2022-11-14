import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pd

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
#tk.Label(fileFrame, text='File Path').grid(row=2, column=1, pady=5)
v = tk.StringVar()
entry = tk.Label(fileFrame, textvariable=v, width="50", bg="gray80", fg="white", anchor="w").grid(row=2, column=2)

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

# dropdown frame
dropdownFrame = tk.Frame(frame).grid(row=10, column=0, padx=70, pady=30)

def open():
    # new window
    top = tk.Toplevel(root)
    top.title('Enter Parameters')
    tk.Label(top, text='dsds')

    top.grab_set()

tk.Button(fileFrame, text='New Window', command=open).grid(row=4, column=1, pady=5)
  
# Dropdown menu options
options = [
    "Function 1",
    "Function 2",
    "Function 3",
    "Function 4",
]

def func1():
    print("Hi")

# run function
def runFunc():
    if clicked.get() == "Function 1" :
        func1()

# dropdown menu
clicked = StringVar()
clicked.set("Function 1")
drop = OptionMenu(root, clicked, *options).grid(row=11, col=1)

# Create button, it will change label text
button = tk.Button( root , text = "Run Function" , command = runFunc ).grid(row=11, col=0)

# bottom frame
closeBtn = tk.Button(frame, text='Close', command=root.destroy).grid(row=10, column=1, pady=60)


root.mainloop()