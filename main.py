BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random


current_card = {}
to_learn = {}
window = Tk()
window.title("FRENCH FLASH")






try:
    data = pandas.read_csv ("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv ("data/french_words.csv")
    to_learn = original_data.to_dict (orient="records")
else:
    to_learn = data.to_dict (orient="records")

def french_text():
    global current_card,flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(french_word, text=current_card["French"], fill="black")



def flip_card():
    canvas.itemconfig(french_title, text="English", fill="black")
    canvas.itemconfig(french_word, text=current_card["English"], fill="black")
    canvas.itemconfig(front_img, image=card_back)
    canvas.itemconfig(back_img, image=card_front)

def known_word():
    to_learn.remove(current_card)
    print(len(to_learn))
    french_text()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words to learn", index=False)


canvas = Canvas(width=800, height=526, highlightthickness=0)
window.minsize(width=800, height=525)
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
card_back = PhotoImage(file="images/card_back.png")
back_img = canvas.create_image(400, 263, image=card_back)

card_front = PhotoImage(file="images/card_front.png")
front_img = canvas.create_image(400, 263, image=card_front)

french_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "bold"), fill="black" )

french_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")





french_text()












canvas.config(background=BACKGROUND_COLOR)

canvas.grid(column=1, row=1, columnspan=2)
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, highlightthickness=0, border=0, command=known_word)

right_button.grid(column=2, row=2)
right_button.config(highlightbackground="green")

wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=french_text)
wrong_button.config(background=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=2)
























window.mainloop()