from tkinter import *


def openFile():
    print("File has been opened!")


def saveFile():
    print("File has been saved!")
    
    
def cut():
    print("You cut some text!")


def copy():
    print("You copy some text!")


def paste():
    print("You paste some text!")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)


openImage = PhotoImage(file="file.png")

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound="left")
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


editMenu = Menu(menubar,tearoff=0)
menubar.add_cascase(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="copy", command=copy)
editMenu.add_command(label="paste", command=paste)


window.mainloop()