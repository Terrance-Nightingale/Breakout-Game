from turtle import Turtle

LENGTH_FACTOR = 4.7
WIDTH_FACTOR = 0.6
START_Y_POS = 300
START_X_POS = -255
COLOR_LIST = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class WallManager:
    """
    Holds multiple instances of Wall objects.
    """
    def __init__(self):
        self.wall_list = []
        y_position = 0
        for color in COLOR_LIST:
            new_wall = Wall(y_position, color)
            self.wall_list.append(new_wall)
            y_position += 15

    def reset(self):
        """
        Clears and redraws walls
        """
        # Reset wall starting position and wall list
        y_position = 0
        for wall in self.wall_list:
            for piece in wall.wall:
                piece.clear()
        self.wall_list = []
        # Establish wall list again
        for color in COLOR_LIST:
            new_wall = Wall(y_position, color)
            self.wall_list.append(new_wall)
            y_position += 15


class Wall:
    """
    Holds multiple instances of Piece objects. Color is randomly assigned across the entire
    wall.
    """
    def __init__(self, y_position, color):
        self.wall = []
        x_position = 0
        for _ in range(0, 6):
            new_piece = Piece(x_position, y_position, color)
            self.wall.append(new_piece)
            x_position += 100


class Piece(Turtle):
    """
    Individual segment of a wall. Is deleted when hit by the ball.
    """
    def __init__(self, x_position, y_position, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH_FACTOR, stretch_len=LENGTH_FACTOR)
        self.color(color)
        self.sety(START_Y_POS - y_position)
        self.setx(START_X_POS + x_position)
