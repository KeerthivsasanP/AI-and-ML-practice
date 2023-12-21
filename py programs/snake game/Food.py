from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.createFood()
        self.foodRefresh()
        
    def createFood(self):
        self.color("blue")
        self.shape("circle")
        self.up()
        self.shapesize(0.5,0.5)

    def foodRefresh(self):
        foodx = randint(-280,280)
        foody = randint(-280,280)
        self.goto(foodx,foody)
    
