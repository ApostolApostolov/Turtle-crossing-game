FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.update_scoreboard()

    def increase_level(self):
        self.clear()
        self.current_level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-290, y=260)
        self.write(f"Level: {self.current_level}", font=FONT)


    def player_game_over(self):
        game_over_text = Turtle()
        game_over_text.penup()
        game_over_text.hideturtle()
        game_over_text.goto(0,0)
        game_over_text.write("Game over", font=FONT)



