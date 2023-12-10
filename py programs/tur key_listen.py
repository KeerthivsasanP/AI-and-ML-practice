from turtle import Turtle,Screen

tim = Turtle()
canvas = tim.getscreen()

def move_fd():
    tim.fd(20)

def move_bk():
    tim.bk(20)

def turn_lt():
    tim.lt(20)

def turn_rt():
    tim.rt(20)

canvas.listen()
canvas.onkey(move_fd,"Up")
canvas.onkey(move_bk,"Down")
canvas.onkey(turn_rt,"Right")
canvas.onkey(turn_lt,"Left")
