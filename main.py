import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pd

data = pd.read_csv('mountain.csv')

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)

def analysis():
    path = filedialog.askopenfilename(title='Select A File')
    groups = data.groupby('Group')
    table = groups.agg({'Revenue':sum, 'Group': len})
    savename = filedialog.asksaveasfilename()
    
    savename = savename.split('.')[0] + '.csv'
    table.to_csv(savename)

root = tk.Tk(className='File Reader')
root.geometry("600x900")

frame = tk.Frame(root).grid(row=0, column=0, padx=70, pady=100)

# file opening frame
fileFrame = tk.Frame(frame).grid(row=0, column=0, padx=0, pady=20)

tk.Button(fileFrame, text='Open File',command=import_csv_data).grid(row=1, column=1)

tk.Label(fileFrame, text='File Path').grid(row=2, column=1)
v = tk.StringVar()
entry = tk.Label(fileFrame, textvariable=v).grid(row=2, column=2)

# stats frame
statsFrame = tk.Frame(frame).grid(row=3, column=0, padx=70, pady=20)

tk.Label(statsFrame, text='Statistics').grid(row=5, column=1, padx=0, pady=0)

def open():
    # new window
    top = Toplevel()
    top.title('hi')
    tk.Label(top, text='dsds')
tk.Button(fileFrame, text='Open New Window', command=open).grid(row=6, column=1)

# bottom frame
closeBtn = tk.Button(frame, text='Close',command=root.destroy).grid(row=10, column=1)


root.mainloop()