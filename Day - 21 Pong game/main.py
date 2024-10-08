from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

winning_score = 5

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()  # move to the ball
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # missed the r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()

    # missed the l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()

    if (scoreboard.r_score == winning_score or
            scoreboard.l_score == winning_score):
        game_is_on = False


turtle = Turtle()
turtle.goto(0, 0)
turtle.color("green")
if scoreboard.r_score == winning_score:
    turtle.write("Right is winner", align="center", font=("Courier", 40, "normal"))
elif scoreboard.l_score == winning_score:
    turtle.write("Left is winner", align="center", font=("Courier", 40, "normal"))











screen.exitonclick()