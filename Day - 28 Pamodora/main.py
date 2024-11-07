from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 2
reps = 0
timer = None

# please create functions outside the windows. Reason is when create some logic without the functions, It's bug. Main part is UI of this project.

# ---------------------------- TIMER RESET ------------------------------- #
# What happen when click the reset button
def reset_btn_click():
    window.after_cancel(timer) # Clean the timer
    time["text"] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    check_mark["text"]= ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
# What happen when click the start button
def start_btn_click():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time["text"] = "Break"
        time["fg"] = RED
    elif reps % 2 == 0:
        count_down(short_break_sec)
        # time["text"] = "Break"
        # time["fg"] = PINK
        time.config(text="Break", fg=PINK) # Two ways to do it
    else:
        count_down(work_sec)
        time["text"] = "Work"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #




def count_down(count):
    count_min = math.floor(count/60) # get less number (5.8 = 5)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" # 5:09 instead of 5:9

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1) # count down is happening every 1000ms(1s) and reduce 1 sec(count-1).
    else:
        start_btn_click() # continuous the loop automatically
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)



time = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
time.grid(row=0, column=1)

canvas =Canvas(width=200, height=224, bg=YELLOW) # same width and height of the image
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)  # x=102 and y=112(center of the image) can change , and fix the image properly
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")) # It can change x and y
canvas.grid(row=1, column=1)


start_btn = Button(text="Start", command=start_btn_click)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command =reset_btn_click)
reset_btn.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)


window.mainloop()