from turtle import *
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
    def refresh(self,x):
        self.clear()
        self.write(f"score:{x}",align="center",font=("Arial",16,"normal"))
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial",24, "normal"))