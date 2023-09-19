from turtle import Turtle
from paddle import Paddle


class Ball(Turtle):
    """
    Creates a pong ball.
    """

    def __init__(self):
        super().__init__()
        self.move_speed = 20
        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        self.forward(self.move_speed)

    def bounce(self):
        self.move_speed += 1
        self.right(90)

    def reset(self):
        self.move_speed = 20
        self.setpos(0, 0)
        self.setheading(45)
