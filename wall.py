from turtle import Turtle
from random import randint

LENGTH_FACTOR = 4.5
WIDTH_FACTOR = 0.5
START_Y_POS = 250
START_X_POS = -250
COLOR_LIST = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class WallManager:
    """
    Holds multiple instances of Wall objects.
    """
    def __init__(self):
        self.wall_list = []
        y_position = 0
        for wall_number in range(0, 4):
            new_wall = Wall(y_position)
            self.wall_list.append(new_wall)
            y_position += 15


class Wall:
    """
    Holds multiple instances of Piece objects. Color is randomly assigned across the entire
    wall.
    """
    def __init__(self, y_position):
        self.wall = []
        x_position = 0
        color = COLOR_LIST[randint(0, len(COLOR_LIST) - 1)]
        for _ in range(0, 6):
            new_piece = Piece(x_position, y_position, color)
            self.wall.append(new_piece)
            x_position += 100


class Piece(Turtle):
    def __init__(self, x_position, y_position, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH_FACTOR, stretch_len=LENGTH_FACTOR)
        self.color(color)
        self.sety(START_Y_POS - y_position)
        self.setx(START_X_POS + x_position)
