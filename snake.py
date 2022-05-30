from turtle import Turtle
"CONSTANTS"
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_TO_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the body of snake"""
        for position in STARTING_POSITIONS:
            self.add_head(position)

    def add_head(self, position):
        """Add a new head or segment to body"""
        new_head = Turtle("square")
        new_head.color("white")
        new_head.penup()
        new_head.goto(position)
        self.segments.append(new_head)

    def extend(self):
        """Extend the body of snake"""
        self.add_head(self.segments[-1].position())

    def move(self):
        """Movement snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_TO_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def check_food_collision(self, food):
        """Detect collision with food"""
        if self.head.distance(food) < 14:
            return True

    def check_wall_collision(self):
        """Detect collision with wall"""
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return True

    def check_tail_collision(self):
        """Detect collision with tail"""
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
