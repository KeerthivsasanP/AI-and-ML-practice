from turtle import Turtle,Screen
import time


WALL_LENGTH = 600
INITIAL_LENGTH = 3
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.drawSnake()
        self.head = self.segments[0]

    def drawSnake(self):
        for pos in STARTING_POS:
            self.grow(pos)
            
    def grow(self,pos):
        snake = Turtle("square")
        snake.up()
        snake.color("green")
        snake.goto(pos)
        self.segments.append(snake)

    def add_tail(self):
        self.grow(self.segments[-1].pos())
        
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            newx = self.segments[seg_num-1].xcor()
            newy = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(newx,newy)
        self.segments[0].fd(MOVE_DISTANCE)

    def move_lt(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_rt(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_dw(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

class Wall:
    def __init__(self):
        self.length = WALL_LENGTH
        self.drawWall()
        
    def drawWall(self):
        wall = Turtle()
        wall.pencolor("red")
        wall.speed("fastest")
        wall.hideturtle()
        wall.up()
        wall.goto(-300,300)
        wall.down()
        for _ in range(0,4):
            wall.fd(600)
            wall.rt(90)







        
