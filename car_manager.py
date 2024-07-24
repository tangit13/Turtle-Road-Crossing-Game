COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            newcar = Turtle("square")
            newcar.shape("square")
            newcar.color(COLORS[random.randint(0,5)])
            newcar.shapesize(1, 2)
            newcar.penup()
            random_y = random.randint(-250, 250)
            newcar.goto(300, random_y)
            self.all_cars.append(newcar)

    def move_forward(self):
        for car in self.all_cars:
            car.forward(-10)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT