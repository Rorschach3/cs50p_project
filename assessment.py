import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

questions = [
    {
        "question": "https://i.ibb.co/HK75mN5/image1.jpg",
        "answers": ["Option A", "Option B", "Option C", "Option D"],
        "correct_answer": "Option A"
    },
    {
        "question": "https://i.ibb.co/SsyLNrM/image2.jpg",
        "answers": ["Option X", "Option Y", "Option Z", "Option W"],
        "correct_answer": "Option X"
    },
    # Add more questions as needed
]

current_question_index = 0
correct_answers = 0


def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(questions):
        update_question()
    else:
        show_result()

def main():
    
    check_answer()


def check_answer():
    selected_answer = selected_option.get()
    correct_answer = questions[current_question_index]["correct_answer"]
    if selected_answer == correct_answer:
        global correct_answers
        correct_answers += 1
    next_question()


def update_question():
    question_data = questions[current_question_index]
    image_url = question_data["question"]
    answers = question_data["answers"]

    image_data = requests.get(image_url).content
    image_original = Image.open(BytesIO(image_data))
    image_display = ImageTk.PhotoImage(image_original)
    label.configure(image=image_display)
    label.image = image_display

    for i, answer in enumerate(answers):
        radio_buttons[i].config(text=answer, value=answer)


def show_result():
    result_label.config(text=f"Your Score: {correct_answers}/{len(questions)}")


window = tk.Tk()
window.geometry('1600x1000')
window.title('Assessment Test')

selected_option = tk.StringVar()

# Create a frame to hold the image
image_frame = tk.Frame(window)
image_frame.pack(side=tk.LEFT)

# Display the initial image
initial_image_data = questions[0]["question"]
initial_image = Image.open(BytesIO(requests.get(initial_image_data).content))
initial_image_display = ImageTk.PhotoImage(initial_image)
label = tk.Label(image_frame, image=initial_image_display)
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
    command=check_answer,
    font=("Comic Sans", 20),
)
check_button.pack()

# Create a label to display the result
result_label = tk.Label(window, font=("Comic Sans", 20))
result_label.pack()

# Start with the first question
update_question()

window.mainloop()
