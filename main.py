import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from wall import WallManager

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Paddle()
walls = WallManager()
ball = Ball()

screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

playing = True
while playing:
    screen.update()
    ball.move()
    ball.detect_hit(player, walls, scoreboard)

    time.sleep(0.09)

screen.exitonclick()
