import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open ("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score_board()

    # def read_txt(self):
    #     with open("data.txt") as file:
    #         self.highscore= file.read()

    def score_board(self):
        self.table = self.write(f"Score: {self.points} High Score: {self.highscore}", align="center", font=("Arial", 20, "normal"))

    def update_board(self):
        self.points += 1
        self.clear()
        self.score_board()

    # def last_board(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER. FINAL SCORE: {self.points}", align="center",font=("Arial", 25, "normal"))
    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
            with open("data.txt","w") as file:
                file.write(str(self.highscore))
        self.points = 0
        self.score_board()