from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} - High score : {self.high_score}",  align="center", font=("Arial", 12, "normal"))

    def increase_board(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", align="center", font=("Arial", 20, "normal") )
