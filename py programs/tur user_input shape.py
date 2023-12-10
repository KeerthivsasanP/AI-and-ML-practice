import turtle

tim = turtle.Turtle()
canvas = tim.getscreen()


user_shape = int(canvas.textinput("User input","Enter the to no of sides of the polygon"))
tim.circle(100,None,user_shape)

user_num_input = int(canvas.numinput("User number input","Enter the no of sides of polygon(between 3 to 10)",minval=3,maxval=10))
tim.circle(50,None,user_num_input)

