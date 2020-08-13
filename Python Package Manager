import os
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 350, height = 400, bg = 'gray90', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Type Package:', bg = 'gray90')
label1.config(font=('helvetica', 14))
canvas1.create_window(175, 80, window=label1)

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

    
button1 = tk.Button(text='      Install Package    ', command=installPackage, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 300, window=button1)


button2 = tk.Button(text='   Uninstall Package  ', command=uninstallPackage, bg='coral3', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 350, window=button2)


button3 = tk.Button(text='         Update Pip         ', command=updatePip, bg='deep sky blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 250, window=button3)

root.mainloop()
