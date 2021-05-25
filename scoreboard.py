from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Arial", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = self.get_high_score()
        self.message = "score: "
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.build_message()

    def build_message(self):
        self.write(f"Score: {str(self.current_score)} High score: {self.high_score}", False, ALIGNMENT, FONT)

    @staticmethod
    def get_high_score():
        with open("data.txt", "r") as file:
            return int(file.read())

    @staticmethod
    def set_high_score(score):
        with open("data.txt", "w") as file:
            file.write(score)

    def update_score(self):
        self.clear()
        self.build_message()

    def increase_score(self):
        self.current_score += 1
        if self.current_score > self.high_score:
            self.set_high_score(str(self.current_score))

        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("blue")
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def restart(self):
        self.goto(x=0, y=-25)
        self.color("blue")
        self.write("press SPACE to RESTART", False, ALIGNMENT, FONT)
        self.goto(x=0, y=-50)
        self.write("CLICK screen to EXIT", False, ALIGNMENT, FONT)
