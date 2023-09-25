from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    """
    A Scoreboard object that keeps track of stage number and score.
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.stage = 1
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 330)
        self.write(f"Stage:{self.stage}", align="center", font=FONT)
        self.goto(150, 330)
        self.write(f"Score:{self.score}", align="center", font=FONT)

    def next_stage(self):
        self.stage += 1
        self.update_scoreboard()

    def score_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
