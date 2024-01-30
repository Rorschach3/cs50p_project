from tkinter import *


def doSomething(event):
    print("You did a thing!" + str(event.x) + "," + str(event.y))


window = Tk()


window.bind("<Button-1>", doSomething)
window.bind("<Button-2>", doSomething)
window.bind("<Button-3>", doSomething)


window.mainloop()