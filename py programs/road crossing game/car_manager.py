from turtle import Turtle
import time
import random 

CAR_COLOR = ["red","blue","green","yellow","purple"]

class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        if random.randint(1,6) == 1:
            car = Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(CAR_COLOR))
            random_y = random.randint(-230,230)
            car.goto(400,random_y)
            self.all_cars.append(car)

    def move_car(self):
        time.sleep(0.1)
        for car in self.all_cars:
            car.bk(20)
