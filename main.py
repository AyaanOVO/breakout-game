from turtle import Turtle, Screen
from paddle import Paddle
from obstacle import Obstacle
from ball import ball
import random
import time

# Setting a screen for turtle
screen = Screen()
screen.screensize(600, 800)
screen.title("Break Out")
screen.bgcolor("black")


# created a paddle
paddle = Paddle()

screen.listen()
screen.onkey(fun=paddle.right_move, key="Right")
screen.onkey(fun=paddle.left_move, key="Left")

# Moving the ball
side = "left"

# Obstacle
obstacle = Obstacle()
for ob in obstacle.all_obstacle:
    ob._tracer(1)
moving = "upward_left"


while True:
    ball.tim._tracer(1, 0)

    if moving == "upward_left":
        if ball.tim.position()[0] >= -466:
            ball.tim.setheading(135)
            ball.tim.forward(1)

        if ball.tim.position()[0] <= -466:
            moving = "upward_right"

        if ball.tim.position()[1] >= 392:
            moving = "downward_left"

    elif moving == "upward_right":
        if ball.tim.position()[1] <= 388:
            ball.tim.setheading(45)
            ball.tim.forward(1)

        if ball.tim.position()[1] >= 388:
            moving = "downward_right"

        if ball.tim.position()[0] >= 466:
            moving = "upward_left"

    elif moving == "downward_right":
        if ball.tim.position()[0] <= 466:
            ball.tim.setheading(-45)
            ball.tim.forward(1)

        if ball.tim.position()[0] >= 466:
            moving = "downward_bottom"

        if ball.tim.position()[1] <= -392:
            print("game over")
            break

    elif moving == "downward_bottom":
        if ball.tim.position()[1] >= -388:
            ball.tim.setheading(-135)
            ball.tim.forward(1)

        if ball.tim.position()[1] <= -388:
            print("game Over")
            break

    elif moving == "downward_left":
        if ball.tim.position()[0] >= -466:
            ball.tim.setheading(-135)
            ball.tim.forward(1)

        if ball.tim.position()[1] <= -388:
            print("game over")
            break

        if ball.tim.position()[0] <= -466:
            moving = "downward_right"

        if ball.tim.position()[1] <= -392:
            moving = "upward_left"

    if int(paddle.tim.position()[0]+75) >= int(ball.tim.position()[0]) and int(paddle.tim.position()[0]-75) <= int(ball.tim.position()[0]):
        if int(paddle.tim.position()[1]+20) >= int(ball.tim.position()[1]) and int(paddle.tim.position()[1]-20) <= int(ball.tim.position()[1]):
            if moving == "downward_left":
                moving = "upward_left"
            elif moving == "downward_bottom":
                moving = "upward_left"
            elif moving == "downward_right":
                moving = "upward_right"


    for ob in obstacle.all_obstacle:
        if int(ob.position()[0] + 40) >= int(ball.tim.position()[0]) and int(ob.position()[0] - 40) <= int(ball.tim.position()[0]):
            if int(ob.position()[1] + 25) >= int(ball.tim.position()[1]) and int(ob.position()[1] - 25) <= int(ball.tim.position()[1]):
                ob.reset()
                ob.hideturtle()
                ob.penup()
                ob.goto(1000,1000)
                if moving == "downward_left":
                    moving = "upward_left"
                elif moving == "downward_bottom":
                    moving = "upward_left"
                elif moving == "downward_right":
                    moving = "upward_right"
                elif moving == "upward_left":
                    moving = "downward_left"
                elif moving == "upward_right":
                    moving = "downward_right"

    ball.tim._tracer(1)

screen.mainloop()