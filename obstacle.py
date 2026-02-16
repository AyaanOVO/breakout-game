from turtle import Turtle, Screen
import random

class Obstacle():
    x, y = (0, 0)
    all_obstacle = []
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'grey']
    def __init__(self):
        for i in range(0, 4):
            for j in range(0, 10):
                tim = Turtle("square")
                tim.speed(0)
                tim.hideturtle()
                tim.penup()
                tim.color(random.choice(Obstacle.colors))
                tim.shapesize(stretch_wid=1, stretch_len=4)
                tim.goto(-410+Obstacle.x, 250-Obstacle.y)
                tim.showturtle()
                tim._tracer(100)
                Obstacle.x += 90

                self.all_obstacle.append(tim)

            Obstacle.y += 50
            Obstacle.x = 0