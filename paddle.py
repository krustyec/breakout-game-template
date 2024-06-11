from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(coordinates)
        self.shapesize(1, 8)

    def x_right(self):
        new_right = self.xcor() + 20
        self.goto(new_right, self.ycor())

    def x_left(self):
        new_left = self.xcor() - 20
        self.goto(new_left, self.ycor())
