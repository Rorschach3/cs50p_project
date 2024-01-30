from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

levels = 9
current_question_index = 0
score = 0
user_answers = {}
current_photo = None
label = None

image_urls = [
	"./images/image1.jpg",
	"./images/image2.jpg",
	"./images/image3.jpg",
	"./images/image4.jpg",
	"./images/image5.jpg",
	"./images/image6.jpg",
	"./images/image7.jpg",
	"./images/image8.jpg",
	"./images/image9.jpg"
	]


def click(label, photo):
    global current_question_index, current_photo, levels
    if levels > 0:
        current_question_index = (current_question_index + 1) % len(image_urls)

        # Load the new image
        image_path = image_urls[current_question_index]
        new_image = Image.open(image_path)
        new_photo = ImageTk.PhotoImage(new_image)

        # Update the label and photo with the new image
        label.configure(image=new_photo)
        label.image = new_photo

        levels -= 1

window = tk.Tk()
window.geometry('1000x1200')
window.title('Assessment Test')

def main():
    # Load the initial image
    initial_image_path = image_urls[current_question_index]
    initial_image = Image.open(initial_image_path)
    initial_photo = ImageTk.PhotoImage(initial_image)

    # Create a label to display the image
    label = tk.Label(window, image=initial_photo)
    label.pack()

    options = ["A", "B", "C", "D"]


    for index in range(len(options)):
        button = Button(
            window,
            text=options[index],
            command=lambda: click(label, initial_image),
            font=("Helvetica Neue", 25),
            fg="white",
            bg="black",
            activeforeground="white",
            activebackground="black",
            width=5,
            )
        button.pack(side=LEFT)

    window.mainloop()

if __name__ == "__main__":
    main()
