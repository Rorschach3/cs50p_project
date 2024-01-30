from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
from questions import problems

current_question_index = 0
score = 0
user_answers = {}


def next_question():
    global current_question_index
    current_question_index += 1
    update_question()


def select_option():
    selected_option = selected_option.get()
    user_answers[current_question_index] = selected_option
    check_answer()


def check_answer():
    selected_answer = user_answers.get(current_question_index, "")
    correct_answer = problems[1][current_question_index]
    if selected_answer == correct_answer:
        global score
        score += 1
    next_question()


def update_question():
    if current_question_index < len(problems[0]):
        image_data = problems[2][int(current_question_index)]
        image = Image.open(image_data)
        image_display = ImageTk.PhotoImage(image)
        label.configure(image=image_display)
        label.image = image_display

        for i, answer in enumerate(problems[0][current_question_index]):
            radio_buttons[i].config(text=answer, value=answer)

    else:
        show_result()


def show_result():
    result_label.config(text=f"Your Score: {score}/{len(problems[0])}")

window = tk.Tk()
window.geometry('1600x1000')
window.title('Assessment Test')

selected_option = tk.StringVar()

# Create a frame to hold the image
image_frame = tk.Frame(window)
image_frame.pack(side=tk.LEFT)


# Display the initial image
image_data = problems[2][current_question_index]
image = Image.open(image_data)
image_display = ImageTk.PhotoImage(image)
label = tk.Label(image_frame, image=image_display)
label.pack()

# Create a frame to hold the radio buttons
radio_frame = tk.Frame(window)
radio_frame.pack(side=tk.RIGHT)

# Create radio buttons in the second frame
radio_buttons = []
for _ in range(4):
    radio_button = tk.Radiobutton(
        radio_frame,
        variable=selected_option,
        font=("Comic Sans", 20),
        indicatoron=0,  # Turn off the indicator
    )
    radio_button.pack(anchor="w")
    radio_buttons.append(radio_button)

# Create a button to check the answer
check_button = tk.Button(
    window,
    text="Check Answer",
    command=select_option,
    font=("Comic Sans", 20),
)
check_button.pack()

# Create a label to display the result
result_label = tk.Label(window, font=("Comic Sans", 20))
result_label.pack()

# Start with the first question
update_question()

window.mainloop()
