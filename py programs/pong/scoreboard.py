from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.score = 0
        self.up()
        self.color("white")
        self.hideturtle()
        self.goto(pos)
        self.printScore()

    def printScore(self):    
        self.write(self.score,font=('Courier',12,'bold'))
    
    def updateScore(self):
        self.clear()
        self.score += 1
        self.printScore()

    
            
