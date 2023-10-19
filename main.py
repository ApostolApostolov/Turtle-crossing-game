import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
#scoreboard = Scoreboard()

cars = CarManager()
screen.listen()
scoreboard =Scoreboard()

screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    cars.car_creation()
    cars.movement()

    if player.level_passed():
        cars.increase_speed()


    for car in cars.cars_list:
        if car.distance(player) < 20:
            scoreboard.player_game_over()
            game_is_on = False


    screen.update()

screen.exitonclick()
