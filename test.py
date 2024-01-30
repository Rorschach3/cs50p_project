from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk



current_question_index = 0
score = 0
user_answers = {}


def click():
    print("You clicked the button!")


def main():
    window = tk.Tk()
    window.title("Image Viewer")

    # Load the image
    image_path = "./images/image3.jpg"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = tk.Label(window, image=photo)
    label.pack()

    options = ["A", "B", "C", "D"]


    for index in range(len(options)):
        button = Button(
            window,
            text=options[index],
            command=click,
            font=("Helvetica Neue", 30),
            fg="white",
            bg="black",
            activeforeground="white",
            activebackground="black",
            width=5
            )
        button.pack(side=LEFT)

    window.mainloop()

if __name__ == "__main__":
    main()
