from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) # update drawing

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    screen.update() #all the snake parts move together
    time.sleep(0.2) #time space between the snake parts

    snake.move()






























screen.exitonclick()