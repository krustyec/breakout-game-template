from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BlockManager:
    def __init__(self):
        self.all_blocks = []
        self.x_start = -525
        self.y_start = 100

    def create_block(self, num):
        new_block = Turtle("square")
        new_block.penup()
        new_block.color(random.choice(COLORS))
        new_block.shapesize(stretch_wid=1, stretch_len=2)
        self.x_start += 55
        new_block.x_cor = self.x_start
        new_block.y_cor = self.y_start
        new_block.goto(new_block.x_cor, new_block.y_cor)
        self.all_blocks.append(new_block)
        # print(self.all_blocks)

    def blocks(self, num):
        for block in range(num):
            self.create_block(block)
