from tkinter import *


food = ["A", "B", "C", "D"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index],
        variable=x,
        value=index,
        padx=25,
        font=("Arial", 50),
        indicatoron=0,
        width=25
        )


    radiobutton.pack(anchor="w")

window.mainloop()
