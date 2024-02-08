from customtkinter import CTk, CTkLabel, CTkButton, CTkImage
import customtkinter
from tkinter import Menu
from PIL import Image, ImageTk
import webbrowser
import sys
import os


class PythonQuizApp(CTk):
    width = 1100
    height = 1200

    def __init__(self):

        self.title("Python Quiz App")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # Load background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        bg_image_path = os.path.join(current_path, "test_images/bg_gradient.jpg")
        bg_image = Image.open(bg_image_path).resize((self.width, self.height))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        # Create background label
        self.bg_label = CTkLabel(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Setup Menu
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        self.fileMenu = Menu(self.menubar, tearoff=0, font=("Helvetica Neue", 16))
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.fileMenu.add_command(label="Restart", command=self.restart)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.close)
        self.fileMenu.add_command(label="GitHub", command=self.github)

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
        self.skill_level = [
            "Newbie",
            "Beginner",
            "Beginner Intermediate",
            "Beginner Advanced",
            "Intermediate",
            "Intermediate Advanced",
            "Advanced Beginner",
            "Advanced Intermediate",
            "Expert"
        ]

    def close(self):
        sys.exit()

    def github(self):
        webbrowser.open_new_tab('https://github.com/rorschach3/cs50p_project')

    def setup_gui(self):
        self.update_question()
        self.mainloop()

    def update_question(self):
        if self.current_question_index < len(self.options):
            for widget in self.winfo_children():
                if widget is not self.bg_label:
                    widget.destroy()

            # Update the image
            image_path = self.image_urls[self.current_question_index]
            image = CTkImage(dark_image=Image.open(image_path), size=(30, 30))
            photo = Image.PhotoImage(image)

            image_label = CTkLabel(self, image=photo)
            image_label.image = photo
            image_label.pack()

            question_label = CTkLabel(
                self,
                text="If this code was to run what would the expected output be?",
                font=("Helvetica Neue", 25),
                text_color="white")
            question_label.pack(pady=6)

            option_dict = self.options[self.current_question_index]
            for key, value in option_dict.items():
                button = CTkButton(
                    self,
                    text=f"{key}: {value}",
                    command=lambda k=key: self.handle_answer(k),  
                    font=("Helvetica Neue", 16),
                    text_color="white",
                    hover_color="gray",
                    width=140) 
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
        # Clear previous content
        for widget in self.winfo_children():
            widget.destroy()

        # Display final score
        score_label = CTkLabel(
            self,
            text=f"Final Score: {self.count} / {len(self.options)} \n Your Python skill level is: {self.skill_level[max(0, self.count - 1)]}",
            font=("Helvetica Neue", 30),
            text_color="white",
            fg_color="black")
        score_label.pack(pady=20)

        # Optional: Add a button to restart the quiz
        restart_button = CTkButton(
            self,
            text="Restart Quiz",
            command=self.restart,
            font=("Helvetica Neue", 16),
            fg_color="white",
            bg_color="black",
            text_color="white",
            hover_color="gray",
            width=10,
            activeforeground="white",
            activebackground="gray")
        restart_button.pack(pady=20)

    def restart(self):
        self.current_question_index = 0
        self.count = 0
        self.update_question()


if __name__ == '__main__':
    python_quiz_app = PythonQuizApp()
    python_quiz_app.mainloop()
