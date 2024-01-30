from tkinter import *


questions = ["A: 0.33", "B: 10", "C: 2.33", "D: 1.22"]

window = Tk()

x = IntVar()

for index in range(len(questions)):
    radiobutton = Radiobutton(
        window,
        text=questions[index],
        variable=x,
        value=index,
        padx=15,
        font=("Arial", 50),
        indicatoron=0,
        width=5
        )


    radiobutton.pack(anchor="w")

window.mainloop()
