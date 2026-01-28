from turtle import Turtle

HIGH_SCORE_FILD ="assets/data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=self.load_high_score()
        self.color("green")
        self.penup()
        self.goto(30,320)
        self.hideturtle()
        self.update_scoreboard()
    def  load_high_score(self):
        try:
            with open(HIGH_SCORE_FILD,mode="r") as file : 
                return int(file.read())  
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score:{self.high_score}",font=("Arial",16,"normal"))
    def increase(self):
        self.score+=1
        self.update_scoreboard()
    def  save_score(self):
        if self.score > self.high_score:
            self.high_score = self.score 
            with open(HIGH_SCORE_FILD,mode="w") as file:
                file.write(str(self.high_score))


