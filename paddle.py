from turtle import Turtle

LENGTH_FACTOR = 5
WIDTH_FACTOR = 1
START_Y_POS = -300


class Paddle(Turtle):
    """
    Creates a paddle object.
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH_FACTOR, stretch_len=LENGTH_FACTOR)
        self.color("white")
        self.sety(START_Y_POS)

    def move_left(self):
        current_x = self.xcor()
        self.setx(current_x - 20)

    def move_right(self):
        current_x = self.xcor()
        self.setx(current_x + 20)
