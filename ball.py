import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_speed = 10
        self.y_speed = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def rebound_y(self):
        self.y_speed *= - 1

    def rebound_x(self):
        self.x_speed *= - 1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.rebound_x()
