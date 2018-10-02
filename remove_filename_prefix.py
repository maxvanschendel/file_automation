from os import listdir,rename
from tkinter import filedialog

directory = filedialog.askdirectory()+'/'
files = listdir(directory)

for i in files:
    rename(directory+i,directory+i[9:])

