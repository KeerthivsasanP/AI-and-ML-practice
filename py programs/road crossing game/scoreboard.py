from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-300,250)
        self.down()
        self.writelevel()

    def writelevel(self):
        self.write(f"Score : {self.level}",font=('Courier',12,'bold'))
        self.hideturtle()
        
    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Score : {self.level}",font=('Courier',12,'bold'))
        
