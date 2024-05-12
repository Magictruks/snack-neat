import turtle
import time
import random

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("white")
win.setup(280 * 2, 280 * 2)

snake_speed = 1

font_style = ("Arial", 14, "bold")


class SnakeGame(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.setx(self.xcor() + 10)
        elif self.direction == "left":
            self.setx(self.xcor() - 10)
        elif self.direction == "up":
            self.sety(self.ycor() + 10)
        elif self.direction == "down":
            self.sety(self.ycor() - 10)

    def change_direction(self, direction):

        print("direction")
        print(direction)
        # direction can be 0, 1 or 2
        # 0 = turn left
        # 1 = do nothing
        # 2 = turn right

        if direction == 0:
            if self.direction == "left":
                self.direction = "down"
            elif self.direction == "down":
                self.direction = "right"
            elif self.direction == "right":
                self.direction = "top"
            elif self.direction == "top":
                self.direction = "left"

        if direction == 2:
            if self.direction == "left":
                self.direction = "top"
            elif self.direction == "top":
                self.direction = "right"
            elif self.direction == "right":
                self.direction = "bottom"
            elif self.direction == "bottom":
                self.direction = "left"

        # if direction == "right" and not self.direction == "left":
        #     self.direction = "right"
        # elif direction == "left" and not self.direction == "right":
        #     self.direction = "left"
        # elif direction == "up" and not self.direction == "down":
        #     self.direction = "up"
        # elif direction == "down" and not self.direction == "up":
        #     self.direction = "down"


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def refresh(self):
        self.clear()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(-350, 320)
        self.score = 0

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", font=font_style)


snake = SnakeGame()
food = Food()
score = Score()

score.update_score(0)

while True:
    win.update()
    # user_input = win.textinput("Snake Game", "Enter direction (w/a/s/d): ")

    list_input = ["up", "down", "right", "left"]

    # if user_input == "exit":
    #     break

    # snake.change_direction(random.choice(list_input))
    snake.move()

    if snake.xcor() > 280 or snake.xcor() < -280:
        break

    if snake.ycor() > 280 or snake.ycor() < -280:
        break

    distance = ((snake.xcor() - food.xcor()) ** 2 + (snake.ycor() - food.ycor()) ** 2) ** 0.5
    if distance < 10:
        score.update_score(score.score + 1)
        snake.color("red")
        snake.setx(food.xcor())
        snake.sety(food.ycor())
        snake.color("green")
        food.refresh()

    time.sleep(1 / snake_speed)

print("Game over!")


def turn_left():
    snake.change_direction(0)


win.listen()
win.onkeypress(turn_left, "q")
win.onkeypress(snake.change_direction(1), "d")

win.mainloop()
