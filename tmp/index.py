# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech
import os
import turtle
import time
import random
import neat

delay = 0.1

# Score
# score = 0
# high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates


class Snake:
    def __init__(self):
        self.head = None
        self.segments = []
        self.score = 0
        self.stamina = 20
        self.alive = True

        self.init_head()

    def init_head(self):
        # Snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "right"

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def print_current_position(self):
        print((self.head.xcor(), self.head.ycor()))

    def move(self, direction):

        # list_move = ["up", "down", "left", "right"]
        # random_move = random.choice(list_move)

        next_move = self.head.direction

        if direction == 0:
            # self.head.direction = "left"
            # nothing
            next_move = self.head.direction
        elif direction == 1:
            # self.head.direction = "right"
            next_move = self.get_direction_turn_left()
        elif direction == 2:
            # self.head.direction = "top"
            next_move = self.get_direction_turn_right()
        # else:
        #     self.head.direction = "bottom"

        # self.head.direction = random_move

        # self.head.direction = next_move

        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

        self.stamina -= 1

        # if self.head.direction == "up":
        #     y = self.head.ycor()
        #     self.head.sety(y + 20)
        #
        # if self.head.direction == "down":
        #     y = self.head.ycor()
        #     self.head.sety(y - 20)
        #
        # if self.head.direction == "left":
        #     x = self.head.xcor()
        #     self.head.setx(x - 20)
        #
        # if self.head.direction == "right":
        #     x = self.head.xcor()
        #     self.head.setx(x + 20)

    def get_direction_turn_left(self):
        print("turn left")

        current_direction = self.head.direction
        next_direction = current_direction

        if current_direction == "left":
            self.go_down()
            next_direction = "down"

        elif current_direction == "down":
            self.go_right()
            next_direction = "right"

        elif current_direction == "right":
            self.go_up()
            next_direction = "up"

        elif current_direction == "up":
            self.go_left()
            next_direction = "left"

        return next_direction


    def get_direction_turn_right(self):
        print("turn right")

        current_direction = self.head.direction
        next_direction = current_direction

        if current_direction == "left":
            self.go_up()
            next_direction = "up"

        elif current_direction == "up":
            self.go_right()
            next_direction = "right"

        elif current_direction == "right":
            self.go_down()
            next_direction = "down"

        elif current_direction == "down":
            self.go_left()
            next_direction = "left"

        return next_direction

    def segments_update(self):
        # Move the end segments first in reverse order
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

    def border_collision(self):
        self.head.goto(0, 0)
        self.head.direction = "stop"
        # Hide the segments
        for segment in self.segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        self.segments.clear()

        # Reset the score
        self.score = 0
        self.game_over()

    def food_collision(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        self.segments.append(new_segment)
        self.score += 10
        self.stamina += 50

    def has_segments_collision(self):
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                return True
        return False

    def segments_collision(self):
        self.game_over()

    def has_stamina(self):
        return self.stamina > 0

    def no_more_stamina(self):
        self.game_over()

    def game_over(self):
        self.alive = False
        # time.sleep(1)
        # self.head.goto(0, 0)
        # self.head.direction = "stop"

        # self.head = None
        # Hide the segments
        for segment in self.segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        self.segments.clear()

        # Reset the score
        self.score = 0
        self.stamina = 0
        self.head.color("white")

    def is_alive(self):
        return self.alive


class Food:
    def __init__(self):
        self.instance = None
        self.init_instance()

    def init_instance(self):
        self.instance = turtle.Turtle()
        self.instance.speed(0)
        self.instance.shape("circle")
        self.instance.color("red")
        self.instance.penup()
        self.instance.goto(0, 100)

    def has_snake_collision(self, snake: Snake):
        return snake.head.distance(self.instance) < 20

    def snake_collision(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.instance.goto(x, y)


class Board:
    def __init__(self):
        self.instance = None

    def init_instance(self):
        self.instance = turtle.Turtle()
        self.instance.speed(0)
        self.instance.shape("square")
        self.instance.color("white")
        self.instance.penup()
        self.instance.hideturtle()
        self.instance.goto(0, 260)
        self.instance.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    def has_border_collision(self, snake: Snake):
        # Check for a collision with the border
        return snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290


def choose_move(
        head: turtle.Turtle,
        segments: list[turtle.Turtle],
        food: turtle.Turtle,
        border: list[int],
        score: int
):
    print(head)
    print(segments)
    print(food)
    print(border)
    print(score)


# Keyboard bindings
# wn.listen()
# wn.onkeypress(go_up, "z")
# wn.onkeypress(go_down, "s")
# wn.onkeypress(go_left, "q")
# wn.onkeypress(go_right, "d")


# Main game loop
# def game(board: Board, snakes: list[Snake], foods: list[Food]):
#     while True:
#         wn.update()
#
#         for idx, snake in enumerate(snakes):
#             if not snake.is_alive():
#                 continue
#
#             if board.has_border_collision(snake):
#                 snake.border_collision()
#                 continue
#
#             food = foods[idx]
#
#             # Check for a collision with the food
#             if food.has_snake_collision(snake=snake):
#                 food.snake_collision()
#                 snake.food_collision()
#
#             # Move the end segments first in reverse order
#             # Move segment 0 to where the head is
#             snake.segments_update()
#
#             # Choose move here and move
#             snake.move()
#
#             # Check for head collision with the body segments
#             snake.check_segments_collision()
#
#         time.sleep(delay)

def eval_genomes(genomes, config):
    print("New generation")
    nets = []
    ge = []
    foods = []
    snakes = []
    board = Board()

    snakes_alive = 0

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)
        snakes.append(Snake())
        foods.append(Food())
        snakes_alive += 1

    while True:

        wn.update()

        for idx, snake in enumerate(snakes):

            if not snake.is_alive():
                continue

            if board.has_border_collision(snake):
                snake.border_collision()
                snakes_alive -= 1
                continue

            food = foods[idx]

            print('Snake :', idx)
            snake.print_current_position()

            # Check for a collision with the food
            if food.has_snake_collision(snake=snake):
                food.snake_collision()
                snake.food_collision()
                ge[idx].fitness += 0.1

            # Move the end segments first in reverse order
            # Move segment 0 to where the head is
            snake.segments_update()

            # Choose move here and move

            inputs = [
                snake.head.xcor(), snake.head.ycor(),
                food.instance.xcor(), food.instance.ycor(),
                -290 - abs(snake.head.xcor()),  # left x
                290 - abs(snake.head.xcor()),  # right x
                -290 - abs(snake.head.ycor()),  # top x
                290 - abs(snake.head.ycor()),  # bottom x
            ]

            output = nets[idx].activate(inputs)

            print(output)

            direction_index = output.index(max(output))

            snake.move(direction_index)

            if not snake.has_stamina():
                snake.no_more_stamina()
                snakes_alive -= 1
                continue


            # Check for head collision with the body segments
            if snake.has_segments_collision():
                snake.segments_collision()
                snakes_alive -= 1
                continue

        time.sleep(delay)

        if snakes_alive == 0:
            break


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes)

    print("Best fitness -> {}".format(winner))


if __name__ == "__main__":
    print("Start")
    local_dir = os.path.dirname(__file__)
    print(local_dir)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)

# wn.mainloop()
