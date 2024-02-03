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
    
    options = [Level1=["A: 5", "B: 10", "C: 15", "D: 20"]
        Level2=["A: 0", "B: 0.4", "C: 2", "D: 2.5"]
        Level3=["A: .999", "B: 1.22", "C: 0.066", "D: 0.333"]
        Level4=["A: 10", "B: 40", "C: 01", "D: 5"]
        Level5=["A: PYTH", "B: YHN", "C: ynh", "D: PTO"]
        Level6=["A: python", "B: PYTHON", "C: ''", "D: 'python'"]
        Level7=["A: 0", "B: 1", "C: 4", "D: 3"]
        Level8=["A: Line 3", "B: 3", "C: Line 4", "D: 4"]
        Level9=["A: Marley says: Woof!", "B: Fido says: Woof!", "C: says: Woof!", "D: Woof!"]
    ]


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

    root = Tk()
    app = MyApp(root)
    root.mainloop()
    window.mainloop()

if __name__ == "__main__":
    main()
