from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#ff293f")
        self.speed(1)
        self.shapesize(1, 1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.level = 0.125

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # self.level *= 0.9

    def reset_position(self):
        self.goto(0, -200)
        self.level = 0.125

    def move(self):
        curr_x = self.xcor()
        curr_y = self.ycor()
        new_x = curr_x + self.x_move
        new_y = curr_y + self.y_move
        self.goto(new_x, new_y)