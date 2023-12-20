from turtle import Turtle,Screen
from Snake import Snake,Wall,Food
import time


game_on = True
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

wall = Wall()
wall.drawWall()

snake = Snake()
food = Food()

screen.listen()

while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    
    screen.onkey(snake.move_lt,"Left")
    screen.onkey(snake.move_rt,"Right")
    screen.onkey(snake.move_up,"Up")
    screen.onkey(snake.move_dw,"Down")
