import os
import tkinter as tk
import subprocess
import time


'''MIT License

Copyright (c) 2020 SpicyTakis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 350, height = 400, bg = 'gray90', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Type Package:', bg = 'gray90')
label1.config(font=('helvetica', 14))
canvas1.create_window(175, 80, window=label1)

label1 = tk.Label(root, text='©Copyright 2020 Hentai#8349 / Spicytakis', bg = 'gray90')
label1.config(font=('helvetica', 10))
canvas1.create_window(225, 390, window=label1)

entry1 = tk.Entry (root, width=27)
canvas1.create_window(175, 120, window=entry1)

def installPackage ():
    global installPythonPackage
    installPythonPackage = 'python -m pip install ' + entry1.get()
    
    os.system('start cmd /k ' + installPythonPackage)


def uninstallPackage ():
    global uninstallPythonPackage
    uninstallPythonPackage = 'python -m pip uninstall ' + entry1.get()
    
    os.system('start cmd /k ' + uninstallPythonPackage)

def updatePip ():
    global updatePipVar
    updatePipVar = 'python -m pip install --upgrade pip '
      
    os.system('start cmd /k ' + updatePipVar)

    time.sleep(5)
    
    subprocess.call("taskkill /f /im cmd.exe", shell=True)


    
button1 = tk.Button(text='      Install Package    ', command=installPackage, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 300, window=button1)


button2 = tk.Button(text='   Uninstall Package  ', command=uninstallPackage, bg='coral3', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 350, window=button2)


button3 = tk.Button(text='         Update Pip         ', command=updatePip, bg='deep sky blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 250, window=button3)

root.mainloop()

