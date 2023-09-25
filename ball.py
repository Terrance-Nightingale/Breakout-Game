import time
from turtle import Turtle
from paddle import Paddle
from wall import WallManager
from scoreboard import Scoreboard


class Ball(Turtle):
    """
    Creates a ball.
    """
    def __init__(self):
        super().__init__()
        self.move_speed = 10
        self.penup()
        self.shape("circle")
        self.color("white")
        self.seth(225)

    def move(self):
        self.forward(self.move_speed)

    def ud_bounce(self):
        if self.heading() < 90 or 180 < self.heading() < 270:
            self.right(90)
        elif self.heading() < 180 or 270 < self.heading() < 360:
            self.left(90)

    def lr_bounce(self):
        if self.heading() < 90 or 180 < self.heading() < 270:
            self.left(90)
        elif self.heading() < 180 or 270 < self.heading() < 360:
            self.right(90)

    def reset(self):
        self.move_speed = 10
        self.setpos(0, 0)
        self.setheading(225)

    def detect_hit(self, paddle=Paddle, wm=WallManager, scoreboard=Scoreboard):
        paddle_r = paddle.xcor() + 18
        paddle_l = paddle.xcor() - 18

        right_wall = 280
        left_wall = -280
        ceiling = 380
        floor = -380

        x_cor = self.xcor()
        y_cor = self.ycor()

        # Detect hit with top or bottom of screen
        if y_cor > ceiling:
            self.ud_bounce()
        # Detect hit with sides
        if x_cor > right_wall or x_cor < left_wall:
            self.lr_bounce()
        # Detect hit with paddle
        if self.distance(paddle) < 30 or self.distance(paddle_r, -300) < 35 or self.distance(paddle_l, -300) < 35:
            self.ud_bounce()
        # TODO Add if statement for when ball approaches from either side of the paddle to instead lr_bounce()
        # Detect hit against wall pieces
        for item in wm.wall_list:
            wall = item.wall
            for piece in wall:
                piece_r = piece.xcor() + 9
                piece_l = piece.xcor() - 9
                y = piece.ycor()
                if self.distance(piece) < 35 or self.distance(piece_r, y) < 35 or self.distance(piece_l, y) < 35:
                    self.ud_bounce()
                    scoreboard.score_point()
                    piece_pos = wall.index(piece)
                    piece.color("black")
                    del wall[piece_pos]
