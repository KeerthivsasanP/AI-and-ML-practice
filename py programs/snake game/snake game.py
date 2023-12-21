from turtle import Turtle,Screen
from Snake import Snake,Wall
import time
from Food import Food
from ScoreBoard import ScoreBoard


game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(600,800)
screen.tracer(0)

wall = Wall()
wall.drawWall()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.move_lt,"Left")
screen.onkey(snake.move_rt,"Right")
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_dw,"Down")

while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.foodRefresh()
        snake.add_tail()
        scoreboard.addScore()
        
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_on = False
        scoreboard.gameover()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            scoreboard.gameover()
            
