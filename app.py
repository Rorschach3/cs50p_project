import tkinter as tk
from tkinter import Menu  # Import Menu
from PIL import Image, ImageTk

class PythonQuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.menubar = Menu(self.window)  # Access Menu from tkinter object
        self.window.config(menu=self.menubar)
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)  # Separate label and menu
        self.fileMenu.add_command(label="Restart", command=self.restart_quiz)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.window.quit)
        self.window.geometry('1100x1200')
        self.window.title('Python Quiz App')
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
            "D", "D", "B", "A", "B", "B", "C", "C", "A"
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
        self.skill_level = [
            "Newbie", "Beginner", "Beginner Intermediate",
            "Beginner Advanced", "Intermediate", "Intermediate Advanced",
            "Advanced Beginner", "Advanced Intermediate", "Expert"
        ]

    def setup_gui(self):
        self.update_question()
        self.window.mainloop()

    def update_question(self):
        if self.current_question_index < len(self.options):
            for widget in self.window.winfo_children():
                widget.destroy()

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
                fg="black"
            )
            question_label.pack(pady=6)

            option_dict = self.options[self.current_question_index]
            for key, value in option_dict.items():
                button = tk.Button(
                    self.window,
                    text=f"{key}: {value}",
                    command=lambda k=key: self.handle_answer(k),
                    font=("Helvetica Neue", 16),
                    fg="white",
                    bg="black",
                    width=16,
                    activeforeground="white",
                    activebackground="black"
                )
                button.pack(side="left", padx=4, pady=4, anchor="center")
        else:
            self.show_final_score()

    def handle_answer(self, answer):
        correct_answer = self.answer_data[self.current_question_index]
        if answer == correct_answer:
            self.count += 1

        self.current_question_index += 1
        self.update_question()

    def show_final_score(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        score_label = tk.Label(
            self.window,
            text=f"Final Score: {self.count} / {len(self.options)} \n Your Python skill level is: {self.calculate_skill_level()}",
            font=("Helvetica Neue", 30),
            fg="black"
        )
        score_label.pack(pady=20)

        restart_button = tk.Button(
            self.window,
            text="Restart",
            command=self.restart_quiz,
            font=("Helvetica Neue", 16),
            fg="white",
            bg="black",
            width=10,
            activeforeground="white",
            activebackground="gray"
        )
        restart_button.pack(pady=20)

    def restart_quiz(self):
        self.current_question_index = 0
        self.count = 0
        self.update_question()

    def calculate_skill_level(self):
        percentage_correct = (self.count / len(self.options)) * 100
        if percentage_correct >= 90:
            return self.skill_level[-1]
        elif percentage_correct >= 75:
            return self.skill_level[-2]
        elif percentage_correct >= 60:
            return self.skill_level[-3]
        elif percentage_correct >= 50:
            return self.skill_level[-4]
        elif percentage_correct >= 40:
            return self.skill_level[-5]
        elif percentage_correct >= 30:
            return self.skill_level[-6]
        elif percentage_correct >= 20:
            return self.skill_level[-7]
        elif percentage_correct >= 10:
            return self.skill_level[-8]
        else:
            return self.skill_level[0]

if __name__ == '__main__':
    python_quiz_app = PythonQuizApp()
    python_quiz_app.setup_gui()
