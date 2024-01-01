from turtle import Screen
from my_turtle import MyTurtle
from car_manager import Car_Manager
from random import randint


game_on = True
screen = Screen()
screen.setup(800,600)
screen.tracer(0)


myTurtle = MyTurtle()

car_manager = Car_Manager()


screen.listen()
screen.onkey(myTurtle.move_up,"Up")
screen.onkey(myTurtle.move_dn,"Down")
screen.onkey(myTurtle.move_rt,"Right")
screen.onkey(myTurtle.move_lt,"Left")

while game_on:
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    
    
   
    

