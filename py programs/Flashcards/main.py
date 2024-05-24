from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

def change_word():
    words_db = pd.read_csv("data/french_words.csv")
    words_count = words_db.shape[0]
    

window=Tk()
window.title("flash card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file='images/card_front.png')
canvas.create_image(400,263,image=card_front_img)
canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image,command=change_word)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file='images/right.png')
known_button=Button(image=check_image,command=change_word)
known_button.grid(row=1,column=1)

window.mainloop()
