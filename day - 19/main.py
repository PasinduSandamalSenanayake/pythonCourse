import random
from turtle import Turtle, Screen


screen = Screen()

# # Etch a sketch app
# tim = Turtle()
# def move_forwards():
#     tim.forward(20)
#
# def move_backwards():
#     tim.backward(20)
#
# def turn_letf():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.reset()
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_letf, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "space")
# # --------------------------------------------------------------

# Turtle race

is_race_on = False
screen.setup(width=500, height=400) # set width and height to the screen
user_input = screen.textinput(title="Make your bet", prompt="Who will win the race? Guest the color ?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-100, -60, -20 , 20, 60, 100]
all_turtle = []

for n in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[n])    #set the turtles for positions
    all_turtle.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()  # two colors have color() and I pic pencolor. Other one is fillcolor
            if winning_color == user_input:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()