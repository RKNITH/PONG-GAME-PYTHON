from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.color("green")
        self.penup()
        self.l_score =0
        self.r_score =0
        self.hideturtle()
        self.update_scoreboard()
        


    def update_scoreboard(self):
        self.goto(-100, 370)
        self.write(self.l_score, align="center", font=("arial", 24, "bold"))    
        self.goto(100, 370)
        self.write(self.r_score, align="center", font=("arial", 24, "bold"))    

    def l_point(self):
        self.l_score +=1
        self.clear()
        self.update_scoreboard()  

    def r_point(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()    