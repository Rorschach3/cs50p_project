
def problems():
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

    problems_data = {
        "problem1": ["A: 5", "B: 10", "C: 15", "D: 20"],
        "problem2": ["A: 0", "B: 0.4", "C: 2", "D: 2.5"],
        "problem3": ["A: .999", "B: 1.22", "C: 0.066", "D: 0.333"],
        "problem4": ["A: 10", "B: 40", "C: 01", "D: 5"],
        "problem5": ["A: PYTH", "B: YHN", "C: ynh", "D: PTO"],
        "problem6": ["A: python", "B: PYTHON", "C: ''", "D: 'python'"],
        "problem7": ["A: 0", "B: 1", "C: 4", "D: 3"],
        "problem8": ["A: Line 3", "B: 3", "C: Line 4", "D: 4"],
        "problem9": [
            "A: Marley says: Woof!",
            "B: Fido says: Woof!",
            "C: says: Woof!",
            "D: Woof!"
            ],
    }

    answers_data = [
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

    return problems_data, answers_data, image_urls
