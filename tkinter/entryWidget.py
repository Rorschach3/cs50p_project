from tkinter import *

def Submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)
    
    
def delete():
    entry.delete(0, END)
    
    
def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(
    window,
    font=("Arial",50),
    fg="#00FF00",
    bg="black",
    show="*"
    )


entry.insert(0, 'SpongeBob')
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=Submit)  
submit_button.pack(side=RIGHT)

submit_button = Button(window, text="delete", command=delete)
submit_button.pack(side=RIGHT)

submit_button = Button(window, text="backspace", command=backspace)  
submit_button.pack(side=RIGHT)

window.mainloop()