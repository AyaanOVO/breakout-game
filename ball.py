from turtle import Turtle, Screen

class Ball():
    def __init__(self):
        self.tim = Turtle("circle")
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.color("#E3E1D9")
        self.tim.goto(0,-329)
        self.tim.showturtle()


ball = Ball()
