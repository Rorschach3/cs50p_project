import tkinter as tk
from PIL import Image, ImageTk


class PythonQuizApp:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1100x1200')
        self.window.title('Assessment Test')

        self.current_question_index = 0
        self.image_urls = [
            "./images/image1.jpg", "./images/image2.jpg",
            "./images/image3.jpg", "./images/image4.jpg",
            "./images/image5.jpg", "./images/image6.jpg",
            "./images/image7.jpg", "./images/image8.jpg",
            "./images/image9.jpg"
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
            {"A": "python", "B": "PYTHON", "C": " '' ", "D": "'python'"},
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

        image_label = tk.Label(self.window, image=photo)
        image_label.image = photo
        image_label.pack()

        question_label = tk.Label(
            self.window,
            text="Running this code, what would the expected output be?",
            font=("Helvetica Neue", 25),
            fg="black")

        question_label.pack(pady=6)  # Added padding

        # Update options buttons
        option_dict = self.options[self.current_question_index]

        for key, value in option_dict.items():
            button = tk.Button(
                self.window,
                text=f"{key}: {value}",
                command=lambda k=key: self.handle_answer(k),
                font=("Helvetica Neue", 18),
                fg="white",
                bg="black",
                width=16,
                activeforeground="white",
                activebackground="black")
            button.pack(side="left", padx=4, pady=4, anchor="center")

    def handle_answer(self, answer):
        # check answer, update score, and move to the next question
        correct_answer = self.answer_data[self.current_question_index]
        if answer == correct_answer:
            self.count += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.options):
            self.update_question()
        else:
            # Handle quiz completion
            print(f"Score: {self.count}")
            self.window.destroy()


if __name__ == '__main__':
    python_quiz_app= PythonQuizApp()
    python_quiz_app.setup_gui()