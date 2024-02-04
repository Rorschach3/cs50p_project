import os
from functools import partial
from tkinter import Tk, Button, LEFT
import tkinter as tk
from PIL import Image, ImageTk
from flask import Flask, render_template
import sys

class QuizApp:
    def __init__(self):
        self.levels = 0
        self.current_question_index = 0
        self.score = 0
        self.answers = [
            "D",
            "D",
            "B",
            "A",
            "B",
            "B",
            "C",
            "C",
            "A"
        ]
        self.current_photo = None
        self.label = None
        # Images
        self.image_urls = [
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
        self.window = tk.Tk()
        self.window.geometry('1000x1200')
        self.window.title('Assessment Test')

    # Click function
    def click(self, label):
        if self.levels < 10:
            self.levels += 1
            image_path = self.image_urls[self.levels]
            new_image = Image.open(image_path)
            new_photo = ImageTk.PhotoImage(new_image)
            label.configure(image=new_photo)
            label.image = new_photo
        else: # once the quiz is done
            sys.exit() # exit the program


    # Main function
    def main(self):
        # from where the initial image is located
        initial_image_path = self.image_urls[self.current_question_index]
        # creates image
        initial_image = Image.open(initial_image_path)
        initial_photo = ImageTk.PhotoImage(initial_image)
        # creates label
        label = tk.Label(self.window, image=initial_photo)
        label.pack()
        
        options = [  # options for each question
            {"D": "20", "C": "15", "B": "10", "A": "5"},
            {"D": "2.5", "C": "2", "B": "0.4", "A": "0"},
            {"D": "0.333", "C": "0.066", "B": "1.22", "A": ".999"},
            {"D": "5", "C": "01", "B": "40", "A": "10"},
            {"D": "PTO", "C": "ynh", "B": "YHN", "A": "PYTH"},
            {"D": "'python'", "C": "''", "B": "PYTHON", "A": "python"},
            {"D": "3", "C": "4", "B": "1", "A": "0"},
            {"D": "4", "C": "Line 4", "B": "3", "A": "Line 3"},
            {"D": "Woof!", "C": "says: Woof!", "B": "Fido says: Woof!", "A": "Marley says: Woof!"}
        ]
        # Buttons
        option_dict = options[self.current_question_index]
        for key, value in option_dict.items():
            button = Button(
                self.window,
                text=f"{key}:{value}",
                command=partial(self.click, label),
                font=("Helvetica Neue", 20),
                fg="white",
                bg="black",
                width=10,
                activeforeground="white",
                activebackground="black"
            )

            button.pack(side="right", padx=5, pady=5, anchor="e")
        self.window.mainloop()

app = Flask(__name__)

# Routes based on index.html
@app.route('/')
def home():
    return render_template('index.html')

# helps to run the app
if __name__ == '__main__':
    quiz_app = QuizApp()
    quiz_app.main()
    app.run(debug=True, port=5000)