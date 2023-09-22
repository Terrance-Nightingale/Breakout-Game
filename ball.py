from turtle import Turtle
from paddle import Paddle
from wall import WallManager


class Ball(Turtle):
    """
    Creates a ball.
    """

    def __init__(self, paddle=Paddle, wm=list):
        super().__init__()
        self.paddle = paddle
        self.wall_list = wm
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

    def detect_hit(self):
        right_wall = 280
        left_wall = -280
        ceiling = 380
        floor = -380

        x_cor = self.xcor()
        y_cor = self.ycor()

        # Detect hit with top or bottom of screen
        if y_cor < floor or y_cor > ceiling:
            self.ud_bounce()

        # Detect hit with sides or paddle
        if x_cor > right_wall or x_cor < left_wall:
            self.lr_bounce()
        elif self.distance(self.paddle) < 50:
            self.ud_bounce()

        # Detect hit against wall pieces
        for wall in self.wall_list:
            for piece in wall.wall:
                if self.distance(piece) < 40:
                    piece_pos = wall.wall.index(piece)
                    self.ud_bounce()
                    piece.color("black")
                    del wall.wall[piece_pos]
