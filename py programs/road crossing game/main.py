from turtle import Screen
from my_turtle import MyTurtle
from car_manager import Car_Manager
from random import randint
from scoreboard import ScoreBoard


game_on = True
screen = Screen()
screen.setup(800,600)
screen.tracer(0)

scoreboard = ScoreBoard()


myTurtle = MyTurtle()

car_manager = Car_Manager()


screen.listen()
screen.onkeypress(myTurtle.move_up,"Up")
screen.onkeypress(myTurtle.move_dn,"Down")
screen.onkeypress(myTurtle.move_rt,"Right")
screen.onkeypress(myTurtle.move_lt,"Left")

while game_on:
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if myTurtle.distance(car) < 20:
            game_on = False

    if myTurtle.ycor() > 240.0:
        myTurtle.reset_game()
        scoreboard.update_score()
        
    
   
    

