from turtle import Turtle
import time


class Welcome_board(Turtle):
    def __init__(self):
        super().__init__()
        self.text = ["Welcome to pong","GET","SET","GO"]
        self.hideturtle()
        self.color("white")

    def write_text(self):
        for index in range(0,len(self.text)):
            self.write(self.text[index],align='center',font=("Ariel",20,'bold'))
            time.sleep(1)
            self.clear()

    def finish_text(self,name):
        self.write(f"{name} won",align='center',font=("Ariel",20,'bold'))
        
        
