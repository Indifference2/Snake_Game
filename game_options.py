from turtle import Turtle, Screen

STYLE = ("Courier", 15, "bold")


class Settings:
    def __init__(self):
        """INITIALIZATION SCREEN AND GAME OPTIONS"""
        self.screen = Screen()
        self.screen_options()
        self.t = Turtle()
        self.score = 0
        self.scoreboard()

    def screen_options(self):
        """Create the screen and title"""
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.listen()
        self.screen.tracer(0)

    def scoreboard(self):
        """Create the scoreboard"""
        self.t.color("white")
        self.t.penup()
        self.t.goto(0, 250)
        self.t.write(f"Score: {self.score}", False, font=STYLE, align="center")
        self.t.hideturtle()

    def key_movement(self, snake):
        """KEY BINDING"""
        self.screen.onkey(snake.up, "Up")
        self.screen.onkey(snake.down, "Down")
        self.screen.onkey(snake.left, "Left")
        self.screen.onkey(snake.right, "Right")

    def game_over(self):
        """Write a game over message"""
        self.t.goto(0, 0)
        self.t.write("GAME OVER", False, font=STYLE, align="center")

