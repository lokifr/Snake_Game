from turtle import Turtle
alignment = "center"
style = ("Arial", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        try:
            with open("current_high_score", "r") as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=alignment, font=style)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=alignment, font=style)

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("current_high_score", "w") as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.update_score()


