from turtle import Turtle
start_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 10
Up = 90
Right = 0
Left = 180
Down = 270
class Snake:

    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):
        # This for loop use turn the snake
        for position in start_position:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snake.append(snake)

    def extend(self):
        self.add_snake(self.all_snake[-1].position())  # all_snake[-1] is last part of the snake
    def move(self):
        for snake_num in range(len(self.all_snake) - 1, 0, -1):  # range(start,end,step)
            new_x = self.all_snake[snake_num - 1].xcor()  # go forward by one step
            new_y = self.all_snake[snake_num - 1].ycor()  # go forward by one step
            self.all_snake[snake_num].goto(new_x, new_y)

        self.head.forward(move_distance)  # first snake part not move forward, stop all the part of the snake in the position 0

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)