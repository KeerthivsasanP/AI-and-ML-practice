from turtle import Turtle

STEPS = 20

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.up()
        self.shape("square")
        self.color("white")
        self.shapesize(4,0.75)
        self.goto(pos)
        
    def move_up(self):
        new_y = self.ycor()+STEPS
        self.goto(self.xcor(),new_y)
        
    def move_down(self):
        new_y = self.ycor()-STEPS
        self.goto(self.xcor(),new_y)
        
    
