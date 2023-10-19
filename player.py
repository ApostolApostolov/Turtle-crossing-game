from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
scoreboard = Scoreboard()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def level_passed(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            scoreboard.clear()
            scoreboard.increase_level()
            return True




