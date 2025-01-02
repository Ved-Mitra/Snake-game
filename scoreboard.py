from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,330)
        self.display_score()

    def display_score(self):
        self.write(f"Score : {self.score}",align="center",font=("Arial",12,"bold"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 15, "bold"))