from tkinter import *


def click():
    print("You clicked the button!")


window = Tk()

photo = PhotoImage(file='../images/image1.jpg')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state='active',
                image=photo)
button.pack()


window.mainloop()