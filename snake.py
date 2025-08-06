from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snake = []
        x = 0
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x, 0)
            self.snake.append(segment)
            x -= 20

        # Keyboard bindings
        self.head = self.snake[0]
        self.head.screen.listen()
        self.head.screen.onkey(self.up, "Up")
        self.head.screen.onkey(self.down, "Down")
        self.head.screen.onkey(self.left, "Left")
        self.head.screen.onkey(self.right, "Right")

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:

            self.snake[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.snake[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
           self.snake[0].setheading(RIGHT)
    def extend(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.snake[-1].position())
        self.snake.append(segment)



