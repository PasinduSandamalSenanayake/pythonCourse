import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.color("red")
# tim.forward(200)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)

# for n in range(0, 10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.43)
#
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
#
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
#
# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape in range(3,11):
#     draw_shape(shape)

# colors = ["red", "green", "blue"]
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
#
# for _ in range(100):
#     tim.forward(40)
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(directions))

# Python tuple

turtle.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r, g, b)
#     tim.color(my_tuple)
#
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
#
# for _ in range(100):
#     tim.forward(40)
#     random_color()
#     tim.setheading(random.choice(directions))


# # draw a Spirograph
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r, g, b)
#     tim.color(my_tuple)
#
# tim.speed("fastest")
#
# def spirograph(degree):
#     d = 360/degree
#     for _ in range(int(d)):
#         random_color()
#         tim.circle(100)
#         tim.setheading(tim.heading()+degree)
#
# spirograph(1)




screen = Screen()
screen.exitonclick()

