import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
car_manager = CarManager()
player = Player()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard.update_scoreboard()
screen.listen()
screen.onkey(player.go, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_forward()
    for car in car_manager.all_cars:
      if player.distance(car) < 20:
        game_is_on = False
        scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()