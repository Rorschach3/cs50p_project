from tkinter import *


def doSomething(event):
    
    print("You did a thing!" + event.keysym)


window = Tk()
window.bind("<Button-1>", doSomething)

window.mainloop()