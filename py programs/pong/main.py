from turtle import Screen
from paddle import Paddle
from welcomeboard import Welcome_board
from scoreboard import Scoreboard
from ball import Ball
import time

game_on = True

screen = Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")

r_score = Scoreboard((50,280))
l_score = Scoreboard((-50,280))

playerl = screen.textinput("Left player name","Enter the name of player 1")
playerr = screen.textinput("Right player name","Enter the name of player 2")

ball = Ball()
welcome_board = Welcome_board()
welcome_board.write_text()
screen.update()

l_paddle = Paddle((-370,0))
r_paddle = Paddle((370,0))

screen.listen()
if r_paddle.ycor() < 50 and r_paddle.ycor() > -50:
    screen.onkeypress(r_paddle.move_up,"Up")
    screen.onkeypress(r_paddle.move_down,"Down")
if l_paddle.ycor() < 30:
    screen.onkeypress(l_paddle.move_up,"w")
    screen.onkeypress(l_paddle.move_down,"s")

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.hit()

    if ball.xcor() > 370:
        ball.reset_pos()
        l_score.updateScore()

    if ball.xcor() < -370:
        ball.reset_pos()
        r_score.updateScore()

    if r_score.score == 1:
        welcome_board.finish_text(playerr)
        game_on = False

    if l_score.score == 1:
        welcome_board.finish_text(playerl)
        game_on = False
    
        
        


