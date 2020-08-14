import os
import tkinter as tk
import subprocess
import time

root = tk.Tk()

canvas1 = tk.Canvas(root, width=350, height=560, bg='gray90', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Type Package:', bg='gray90')
label1.config(font=('helvetica', 14))
canvas1.create_window(175, 80, window=label1)

label1 = tk.Label(root, text='©Copyright Hentai#8349 / Spicytakis', bg='gray90')
label1.config(font=('helvetica', 10))
canvas1.create_window(240, 550, window=label1)

entry1 = tk.Entry(root, width=27)
canvas1.create_window(175, 120, window=entry1)


def installPackage():
    global installPythonPackage
    installPythonPackage = 'python -m pip install ' + entry1.get()

    os.system('start cmd /k ' + installPythonPackage)


def installPackage_w_2020_resolver():
    global installPythonPackage
    installPythonPackage = 'python -m pip install --use-feature=2020-resolver ' + entry1.get()


def installPackage_w_fast_deps():
    global installPythonPackage
    installPythonPackage = 'python -m pip install --use-feature=fast-deps ' + entry1.get()


def installPackage_w_2020_resolver_and_fast_deps():
    global installPythonPackage
    installPythonPackage = 'python -m pip install --use-feature=2020-resolver --use-feature=fast-deps ' + entry1.get()


def uninstallPackage():
    global uninstallPythonPackage
    uninstallPythonPackage = 'python -m pip uninstall ' + entry1.get()

    os.system('start cmd /k ' + uninstallPythonPackage)


def updatePip():
    global updatePipVar
    updatePipVar = 'python -m pip install --upgrade pip '

    os.system('start cmd /k ' + updatePipVar)

    time.sleep(5)

    subprocess.call("taskkill /f /im cmd.exe", shell=True)


button1 = tk.Button(text='      Install Package    ', command=installPackage, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 200, window=button1)

button2 = tk.Button(text='      Install Package\nUsing Feature: 2020-resolver    ', command=installPackage_w_2020_resolver, bg='green',
                    fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 300, window=button2)

button3 = tk.Button(text='    Install Package\nUsing Feature: fast-deps    ', command=installPackage_w_fast_deps, bg='green',
                    fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 365, window=button3)

button4 = tk.Button(text='      Install Package\nUsing Feature: 2020-resolver & fast-deps   ', command=installPackage_w_2020_resolver_and_fast_deps,
                    bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 435, window=button4)

button5 = tk.Button(text='   Uninstall Package  ', command=uninstallPackage, bg='coral3', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 490, window=button5)

button6 = tk.Button(text='         Update Pip         ', command=updatePip, bg='deep sky blue', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 250, window=button6)

root.mainloop()
