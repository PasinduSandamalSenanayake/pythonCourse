from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)  # update drawing

snake = Snake()
food = Food()
score_board = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:  #if snake near by 15, It eat the food
        food.refresh()
        score_board.increase_board()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        # game_is_on = False
        # score_board.game_over()
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.all_snake:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # game_is_on = False
            # score_board.game_over()
            score_board.reset()
            snake.reset()































screen.exitonclick()