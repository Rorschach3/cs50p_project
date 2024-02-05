import tkinter as tk
from PIL import Image, ImageTk


class QuizApp:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1000x1200')
        self.window.title('Assessment Test')

        self.current_question_index = 0
        self.image_urls = [
            "./images/image1.jpg", "./images/image2.jpg",
            "./images/image3.jpg", "./images/image4.jpg",
            "./images/image5.jpg", "./images/image6.jpg",
            "./images/image7.jpg", "./images/image8.jpg", "./images/image9.jpg"
        ]
        self.count = 0
        self.answer_data = [
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
        self.options = [
            {"A": "5", "B": "10", "C": "15", "D": "20"},
            {"A": "0", "B": "0.4", "C": "2", "D": "2.5"},
            {"A": ".999", "B": "1.22", "C": "0.066", "D": "0.333"},
            {"A": "10", "B": "40", "C": "01", "D": "5"},
            {"A": "PYTH", "B": "YHN", "C": "ynh", "D": "PTO"},
            {"A": "python", "B": "PYTHON", "C": "''", "D": "'python'"},
            {"A": "0", "B": "1", "C": "4", "D": "3"},
            {"A": "Line 3", "B": "3", "C": "Line 4", "D": "4"},
            {"A": "Marley says: Woof!", "B": "Fido says: Woof!", "C": "says: Woof!", "D": "Woof!"}
            ]

    def setup_gui(self):
        self.update_question()
        self.window.mainloop()

    def update_question(self):
        # Clear previous content
        for widget in self.window.winfo_children():
            widget.destroy()

        # Update the image
        image_path = self.image_urls[self.current_question_index]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.window, image=photo)
        label.image = photo
        label.pack()

        # Update options buttons
        option_dict = self.options[self.current_question_index]

        for key, value in option_dict.items():
            button = tk.Button(
                self.window,
                text=f"{key}: {value}",
                command=lambda k=key: self.handle_answer(k),
                font=("Helvetica Neue", 20),
                fg="white",
                bg="black",
                width=10,
                activeforeground="white",
                activebackground="black")
            button.pack(side="left", padx=6, pady=6, anchor="center")

    def handle_answer(self, answer):
        # Handle the logic to check answer, update score, and move to the next question
        self.current_question_index += 1
        if self.current_question_index < len(self.options):
            self.update_question()
        else:
            # Handle quiz completion
            print("Quiz Completed")
            self.window.destroy()


if __name__ == '__main__':
    quiz_app = QuizApp()
    quiz_app.setup_gui()
