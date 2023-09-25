import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from wall import WallManager

screen = Screen()
screen.title("Breakout")
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
player = Paddle()
walls = WallManager()
ball = Ball()

screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.listen()

playing = True
while playing:
    screen.update()
    ball.move()
    ball.detect_hit(player, walls, scoreboard)

    if not walls.wall_list:
        walls.reset()
        scoreboard.reset()
        ball.reset()

    if ball.ycor() < -380:
        scoreboard.game_over()
        playing = False

    time.sleep(0.03)

screen.exitonclick()
