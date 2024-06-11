# import libraries and classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
from block_manager import BlockManager
from scoreboard import Scoreboard
import time

# initialize the screen
screen = Screen()
# set up the screen
screen.setup(width=1000, height=600)
screen.bgcolor("#828282")
screen.title("Breakout")
screen.tracer(0)

# initialize the paddle on the bottom
paddle_b = Paddle((0, -250))
# initialize ball starting at the middle
gum = Ball()
# initialize block manager
block_manager = BlockManager()
# initialize scoreboard
scoreboard = Scoreboard()

# initialize screen listener
screen.listen()
screen.onkey(paddle_b.x_right, "Right")
screen.onkey(paddle_b.x_left, "Left")

block_manager.blocks(18)

play = True

while play:
    scoreboard.update_score(len(block_manager.all_blocks))
    time.sleep(gum.level)
    screen.update()
    gum.move()

    curr_x = gum.xcor()
    curr_y = gum.ycor()
    # detect collision with top wall
    if curr_y > 280:
        gum.bounce_y()
    # detect collision with right and left wall
    elif curr_x > 480 or curr_x < -480:
        gum.bounce_x()

    # debugging
    # distance between paddle and gum
    # print(gum.distance(paddle_b))
    # current coordinates of the gum
    # print(f'x: {curr_x}, y: {curr_y}')

    # detect collision with paddle_b
    if gum.distance(paddle_b) < 75 and curr_y < -230:
        gum.bounce_y()

    # detects if the ball goes out of bounds at the bottom
    if curr_y < - 260:
        print("You lose.")
        scoreboard.game_over()
        play = False

    # gum collision with block
    for block in block_manager.all_blocks:
        # print(gum.distance(block))
        if gum.distance(block) < 25:
            # hide block affected
            block.hideturtle()
            # debugging contact
            # print(f'x: {curr_x}, y: {curr_y}')
            # print("Boom!")
            # len before boom
            # print(len(block_manager.all_blocks))
            block_manager.all_blocks.remove(block)
            # len after boom
            # print(len(block_manager.all_blocks))

            gum.bounce_y()

screen.exitonclick()
