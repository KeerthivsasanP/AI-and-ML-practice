from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = '✓'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    myWindow.after_cancel(timer)
    myCanvas.itemconfig(timer_text,text="00:00")
    tick.config(text="")
    myLabel.config(text="Timer",fg=GREEN)
    reps=0
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_time():
    global reps
    reps = reps+1
    work_sec=WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    if reps % 2 == 1 and reps < 8:
        myLabel.config(text="Work",fg=GREEN)
        count_down(work_sec)
        
    elif reps % 2 == 0 and reps < 8:
        myLabel.config(text="Break",fg=PINK)
        count_down(short_break_sec)
        
    elif reps==8:
        myLabel.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
        
        reps=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps,timer
    marks = ""
    time_min = count // 60
    time_sec = count%60
    if time_sec < 10:
             time_sec = f"0{time_sec}"
    if count >= 0:
        timer = myWindow.after(1000,count_down,count-1)
        myCanvas.itemconfig(timer_text,text=f"{time_min}:{time_sec}")
    else:
        for _ in range(reps//2):
            marks=marks+TICK
        tick.config(text=marks)
        start_time()
        
            
    
         
# ---------------------------- UI SETUP ------------------------------- #
myWindow = Tk()
myWindow.title("Pomodaro")
myWindow.config(padx=100,pady=50,bg=YELLOW)

myLabel = Label(bg=YELLOW,text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN)
myLabel.grid(row=0,column=1)

myCanvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
myCanvas.create_image(100,112,image=tomato_image)
timer_text=myCanvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

    
myCanvas.grid(row=1,column=1)

startButton = Button(text="Start",command=start_time)
startButton.grid(row=2,column=0)

restartButton = Button(text="Restart",command=reset_timer)
restartButton.grid(row=2,column=2)

tick = Label(fg=GREEN)
tick.grid(row=3,column=1)

myWindow.mainloop()

