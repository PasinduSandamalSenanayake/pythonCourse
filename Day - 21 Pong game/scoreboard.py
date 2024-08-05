from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScoreBoard()


    def updateScoreBoard(self):
        self.goto(-50, 230)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(50, 230)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def left_score(self):
        self.l_score += 1
        self.clear()
        self.updateScoreBoard()

    def right_score(self):
        self.r_score += 1
        self.clear()
        self.updateScoreBoard()
