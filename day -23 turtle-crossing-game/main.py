import time
from turtle import Screen

import car_manager
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(turtle.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    #Detect collision with car
    for car1 in car.all_cars:
        if car1.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car.level_up()
        scoreboard.increase_level()





screen.exitonclick()