import random
import turtle

import colorgram
from turtle import Turtle,Screen

##Got the color list using the image
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle.colormode(255)

t = Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5),
              (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]

t.setheading(225)
t.forward(300)
t.setheading(0)
line_size = 10
dot_count = 10

for _ in range(line_size):
    for _ in range(dot_count):
        t.dot(20, random.choice(color_list))
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(360)




screen = Screen()
screen.exitonclick()