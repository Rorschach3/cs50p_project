import os
from functools import partial
from tkinter import Tk, Button, LEFT
import tkinter as tk
from PIL import Image, ImageTk
from flask import Flask, render_template
from supabase import create_client, Client

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

    def click(self, label, photo):
        if self.levels < 10:
            self.levels = (self.levels + 1)
            image_path = self.image_urls[self.levels]
            new_image = Image.open(image_path)
            new_photo = ImageTk.PhotoImage(new_image)
            label.configure(image=new_photo)
            label.image = new_photo

    def main(self):
        initial_image_path = self.image_urls[self.current_question_index]
        initial_image = Image.open(initial_image_path)
        initial_photo = ImageTk.PhotoImage(initial_image)
        label = tk.Label(self.window, image=initial_photo)
        label.pack()
        
        options = [
            ["A: 5", "B: 10", "C: 15", "D: 20"],
            ["A: 0", "B: 0.4", "C: 2", "D: 2.5"],
            ["A: .999", "B: 1.22", "C: 0.066", "D: 0.333"],
            ["A: 10", "B: 40", "C: 01", "D: 5"],
            ["A: PYTH", "B: YHN", "C: ynh", "D: PTO"],
            ["A: python", "B: PYTHON", "C: ''", "D: 'python'"],
            ["A: 0", "B: 1", "C: 4", "D: 3"],
            ["A: Line 3", "B: 3", "C: Line 4", "D: 4"],
            ["A: Marley says: Woof!", "B: Fido says: Woof!", "C: says: Woof!", "D: Woof!"]
        ]
        
        for index in range(len(options)):
            for index in range(len(options[index])):
                button = Button(
                    self.window,
                    text=options[index][index],
                    command=partial(self.click, label, initial_image),
                    font=("Helvetica Neue", 30),
                    fg="white",
                    bg="black",
                    activeforeground="white",
                    activebackground="black",
                    width=8,
                )
                button.pack(side="right", padx=5, pady=5)
            self.window.mainloop()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    quiz_app = QuizApp()
    quiz_app.main()
    app.run(debug=True, port=5500)