from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
start_position = [(0, 0), (-20, 0), (-40, 0)]
all_snake = []
screen.tracer(0) # update drawing

for position in start_position:
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    all_snake.append(snake)

game_is_on = True
while game_is_on:
    screen.update() #all the snake parts move together
    time.sleep(0.2) #time space between the snake parts

    # This for loop use turn the snake
    for snake_num in range(len(all_snake) - 1, 0, -1):  #range(start,end,step)
        new_x = all_snake[snake_num - 1].xcor()  # go forward by one step
        new_y = all_snake[snake_num - 1].ycor()  # go forward by one step
        all_snake[snake_num].goto(new_x, new_y)

    all_snake[0].forward(20)  # first snake part not move forward, stop all the part of the snake in the position 0





























screen.exitonclick()