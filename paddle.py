from turtle import Turtle, Screen

class Paddle():
    def __init__(self):
        self.tim = Turtle('square')
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.color("#006dcc")
        self.tim.goto(0,-350)
        self.tim.showturtle()
        self.tim.shapesize(stretch_wid=1, stretch_len=7)

    def right_move(self):
        if int(self.tim.position()[0]) < 301:
            self.tim.forward(100)

    def left_move(self):
        if int(self.tim.position()[0]) > -301:
            self.tim.backward(100)