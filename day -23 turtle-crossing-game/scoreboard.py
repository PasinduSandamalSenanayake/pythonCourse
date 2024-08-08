from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.updateScoreboard()


    def increase_level(self):
        self.level += 1
        self.clear()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"level: {self.level}", align="left", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)