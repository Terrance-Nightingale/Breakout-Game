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

    # Detect if ball hits wall/paddles
    x_cor = ball.xcor()
    y_cor = ball.ycor()
    if x_cor > 280 or x_cor < -280:
        ball.bounce()
    elif ball.distance(player) < 50:
        ball.bounce()

    # Keep track of score
    if y_cor < -380 or y_cor > 380:
        ball.bounce()
        #TODO set the ball to reset() instead of bounce(), but only when it hits the -y axis.

    time.sleep(0.09)

screen.exitonclick()
