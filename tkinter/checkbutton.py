from tkinter import *


def display():
    if (X.get() == 1):
        print("You agree :")
    else:
        print("You don't agree :")


window = Tk()
X = IntVar()

check_button = Checkbutton(
    window,
    text="I agree to something",
    variable=X,
    onvalue=1,
    offvalue=0,
    command=display
)

check_button.pack()
window.mainloop()