from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


levels = 9
current_question_index = 0
score = 0
user_answers = {}
current_photo = None
label = None

# image_urls = [
# 	"./images/image1.jpg",
# 	"./images/image2.jpg",
# 	"./images/image3.jpg",
# 	"./images/image4.jpg",
# 	"./images/image5.jpg",
# 	"./images/image6.jpg",
# 	"./images/image7.jpg",
# 	"./images/image8.jpg",
# 	"./images/image9.jpg"
# ]


# options = [
#     ["A: 5", "B: 10", "C: 15", "D: 20"],
#     ["A: 0", "B: 0.4", "C: 2", "D: 2.5"],
#     ["A: .999", "B: 1.22", "C: 0.066", "D: 0.333"],
#     ["A: 10", "B: 40", "C: 01", "D: 5"],
#     ["A: PYTH", "B: YHN", "C: ynh", "D: PTO"],
#     ["A: python", "B: PYTHON", "C: ''", "D: 'python'"],
#     ["A: 0", "B: 1", "C: 4", "D: 3"],
#     ["A: Line 3", "B: 3", "C: Line 4", "D: 4"],
#     ["A: Marley says: Woof!", "B: Fido says: Woof!", "C: says: Woof!", "D: Woof!"]
# ]

def main():
    window = tk.Tk()
    window.geometry('1000x1200')
    window.title('Assessment Test')
    root = Tk()
    app = MyApp(root)
    root.mainloop()
    window.mainloop()

if __name__ == "__main__":
    main()
