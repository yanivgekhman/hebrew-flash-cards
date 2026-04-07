from tkinter import *
import pandas
import random
from data_prep import build_dataset

try:
    with open(file='data/hebrew_words.csv', mode='r', encoding='utf-8') as file:
        pass
except FileNotFoundError:
    build_dataset('data/hebrew_words.txt', 'data/hebrew_words.csv')

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial",40,"italic")
WORD_FONT = ("Heebo",60,"bold")
PRONOUNCE_FONT = ("Arial",13,"italic")
TIMER_FONT = ("Arial",30,"bold")

# data
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/hebrew_words.csv")
hebrew_words = df.to_dict(orient="records")
global timer, current_word

def stop_timer():
    global timer
    try:
        window.after_cancel(timer)
    except NameError:
        pass

def is_known():
    stop_timer()
    hebrew_words.remove(current_word)
    data = pandas.DataFrame(hebrew_words)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()
# ------------------------------------ Card Flipping ------------------------------------ #

def flip_card():
    canvas.itemconfig(language_text, text="English",fill="white")
    canvas.itemconfig(canvas_img,image=back_image)
    canvas.itemconfig(word_text, text=current_word["English"].title(),fill="white")
    canvas.itemconfig(pronunciation_text,text='')

def next_card():
    global current_word,timer
    new_word = random.choice(hebrew_words)
    try:
        while current_word == new_word:
            new_word = random.choice(hebrew_words)
    except NameError:
        current_word = new_word
    else:
        current_word = new_word
    stop_timer()
    canvas.itemconfig(canvas_img, image=front_image)
    canvas.itemconfig(language_text,text="hebrew",fill="black")
    canvas.itemconfig(word_text,text=new_word["Hebrew"],fill="black")
    canvas.itemconfig(pronunciation_text,text=f"/{new_word["Pronunciation"]}/")
    timer = window.after(ms=7000, func=flip_card)
# ------------------------------------ UI ------------------------------------ #
window = Tk()
window.minsize(width=900,height=700)
window.title("Hebrew Words")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

# Creating the UI
canvas = Canvas(bg=BACKGROUND_COLOR,width=800,height=526,highlightthickness=0)

# Image items
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400,263,image=front_image)

# Text items
language_text = canvas.create_text(400,150,text="hebrew",font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, font=WORD_FONT)
pronunciation_text = canvas.create_text(400,310,font=PRONOUNCE_FONT)

canvas.grid(column=0,row=0,columnspan=2,rowspan=2)

# Button items
right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)

right_button.grid(column=1,row=2)
wrong_button.grid(column=0,row=2)

next_card()


window.mainloop()