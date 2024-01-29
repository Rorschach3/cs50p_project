import requests


def main():
    problems()


def problems():
    questions = [
        {"Level_1": requests.get("https://i.ibb.co/HK75mN5/image1.jpg").content},
        {"Level_2": requests.get("https://i.ibb.co/SsyLNrM/image2.jpg").content},
        {"Level_3": requests.get("https://i.ibb.co/ZmQQFcf/image3.jpg").content},
        {"Level_4": requests.get("https://i.ibb.co/nm3Yxn3/image4.jpg").content},
        {"Level_5": requests.get("https://i.ibb.co/hsKjymp/image5.jpg").content},
        {"Level_6": requests.get("https://i.ibb.co/N2ZkGyK/image6.jpg").content},
        {"Level_7": requests.get("https://i.ibb.co/VDtxnQn/image7.jpg").content},
        {"Level_8": requests.get("https://i.ibb.co/qp0vyBR/image8.jpg").content},
        {"Level_9": requests.get("https://i.ibb.co/jVZ51dZ/image9.jpg").content}
    ]
    return questions

if __name__ == "__main__":
    main()
