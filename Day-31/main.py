from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/data.csv")
to_learn = data.to_dict(orient="records") # when used orient , change the data format like this, {'English': 'part', 'Sinhala': 'කොටස'} instead of {'English': {0: 'part', 1: 'history', 2: 'search', 3 ..........'Sinhala': {0: 'කොටස', 1: 'ඉතිහාසය', 2: 'සොයන්න', 3:............
# print(to_learn)
current_card = {}

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["English"])
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_card["English"], fill="black")
    canvas.itemconfig(image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card) # when click the button call delay 3s and move to sinhala meaning word.

def flip_card():
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(title_text, text="Sinhala", fill="white")
    canvas.itemconfig(word_text, text=current_card["Sinhala"], fill="white")

def is_right():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()


window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="image/card_front.png")
card_back_image = PhotoImage(file="image/card_back.png")
image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 54, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="image/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="image/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_right)
right_button.grid(row=1, column=1)

next_card()












window.mainloop()