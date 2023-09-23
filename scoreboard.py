from turtle import Turtle

FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    """
    Sets up scoreboard with Stage number and Score (Score keeps track of the total
    number of wall pieces hit.
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
        self.goto(-150, 300)
        self.write(f"Stage:{self.stage}", align="center", font=FONT)
        self.goto(150, 300)
        self.write(f"Score:{self.score}", align="center", font=FONT)

    def next_stage(self):
        self.stage += 1
        self.update_scoreboard()

    def score_point(self):
        self.score += 1
        self.update_scoreboard()
