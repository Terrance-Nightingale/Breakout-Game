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
        self.move_speed = 15
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
        self.move_speed = 15
        self.setpos(0, 0)
        self.setheading(225)

    def detect_hit(self, paddle=Paddle, wm=WallManager, scoreboard=Scoreboard):
        paddle_r_side = paddle.xcor() + 10
        paddle_l_side = paddle.xcor() - 10

        right_wall = 280
        left_wall = -280
        ceiling = 380
        floor = -380

        x_cor = self.xcor()
        y_cor = self.ycor()

        # Detect hit with top or bottom of screen
        if y_cor < floor or y_cor > ceiling:
            self.ud_bounce()
        # Detect hit with sides
        if x_cor > right_wall or x_cor < left_wall:
            self.lr_bounce()
        # Detect hit with paddle
        if self.distance(paddle) < 35 or self.distance(paddle_r_side, -300) < 35\
                or self.distance(paddle_l_side, -300) < 35:
            self.ud_bounce()
        # Detect hit against wall pieces
        for item in wm.wall_list:
            wall = item.wall
            for piece in wall:
                if self.distance(piece) < 40:
                    self.ud_bounce()
                    scoreboard.score_point()

                    piece_pos = wall.index(piece)
                    piece.color("black")
                    del wall[piece_pos]
