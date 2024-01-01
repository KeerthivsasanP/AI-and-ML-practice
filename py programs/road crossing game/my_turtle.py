from turtle import Turtle

STEPS = 20

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
        
    def move_up(self):
        self.fd(STEPS)

    def move_dn(self):
        self.bk(STEPS)

    def move_rt(self):
        new_x =  self.xcor() + STEPS
        self.goto(new_x,self.ycor())

    def move_lt(self):
        new_x =  self.xcor() - STEPS
        self.goto(new_x,self.ycor())

    def reset_game(self):
        self.goto(0,-280)
