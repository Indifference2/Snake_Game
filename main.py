from turtle import Screen
from snake import Snake
from food import Food
from game_options import Settings
import time

# Calling classes#
food = Food()
snake = Snake()
screen = Screen()
game = Settings()

game.key_movement(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.check_food_collision(food):
        food.spawn_food()
        game.t.clear()
        game.score += 1
        game.scoreboard()
        snake.extend()
    if snake.check_wall_collision():
        game.game_over()
        game_is_on = False
    if snake.check_tail_collision():
        game.game_over()
        game_is_on = False

screen.exitonclick()
