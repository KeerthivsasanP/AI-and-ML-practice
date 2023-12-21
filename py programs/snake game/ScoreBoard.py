from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,300)
        self.color("white")
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.write(f"Score : {self.score}",align="center",font=("Courier",12,"bold"))

    def addScore(self):
        self.score+=1
        self.clear()
        self.updateScore()
        
    def gameover(self):
        self.penup()
        self.goto(0,0)
        self.write("Game over", align = "center",font=("Courier",12,"bold"))
