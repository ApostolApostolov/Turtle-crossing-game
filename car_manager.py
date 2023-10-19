COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def car_creation(self):
        random_chance = random.randint(1,6)

        if random_chance == 1 :
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.x_speed = STARTING_MOVE_DISTANCE
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.cars_list.append(new_car)


    def movement(self):
        for car in self.cars_list:
            car.back(self.car_speed)


    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT