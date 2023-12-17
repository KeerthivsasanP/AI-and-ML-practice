from turtle import Turtle,Screen
from random import randint
canvas = Screen()
canvas.setup(width=700,height=700)
color_list = ["purple","blue","green","orange","yellow"]
all_turtle = []
ypos = [-100,-50,0,50,100]

startline = Turtle()
startline.hideturtle()

startline.up()
startline.goto(-340,-200)
startline.down()
startline.goto(-340,200)

endline=Turtle()
endline.hideturtle()
endline = Turtle()

endline.up()
endline.goto(210,-200)
endline.down()
endline.goto(210,200)
endline.hideturtle()

for t_index in range(0,5):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(color_list[t_index]) 
    tim.penup()
    tim.goto(-330,ypos[t_index])
    all_turtle.append(tim)

user_turtle = canvas.textinput("User bet","Guess the color of turtle that will win!!!")
race_on = False
if user_turtle:
    race_on = True
    
while race_on:
    
    for my_turtle in all_turtle:
        if my_turtle.xcor() > 200:
            race_on = False
            winning_color = my_turtle.pencolor()
            if user_turtle == winning_color:
                print(f"You won. {winning_color} color turtle won")
            else:
                print(f"You lose. {winning_color} color turtle won")
                
        steps = randint(0,30)
        my_turtle.fd(steps)

def close_screen():
    canvas.bye()
canvas.listen()
canvas.onkeypress(close_screen,'x')
    
