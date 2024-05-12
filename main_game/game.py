import os
import random
import time

import pygame

from main_game.fruit import Fruit
from main_game.snake import Snake


change_to = 'RIGHT'

class Game:
    def __init__(self, display_screen=True, snake_speed=1000):
        # Display Screen
        self.display_screen = display_screen

        # Snake speed
        self.snake_speed = snake_speed

        # Window size
        self.window_x = 100
        self.window_y = 100

        self.max_moves = self.window_x * self.window_y
        self.moves = 0

        # defining colors
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        # Initialising pygame
        pygame.init()

        if display_screen:
            os.environ["SDL_VIDEODRIVER"] = "dummy"

        # Initialise game window
        pygame.display.set_caption('GeeksforGeeks Snakes')

        if display_screen:
            self.game_window = pygame.display.set_mode((self.window_x, self.window_y), pygame.HWSURFACE)

        else:
            pygame.display.init()

        self.fps = pygame.time.Clock()

        self.snake = Snake(max_x=self.window_x, max_y=self.window_y)
        self.fruit = Fruit(x=self.window_x, y=self.window_y)

        self.change_to = 'RIGHT'

    def start(self, net):
        # print('Play !')
        # Main Function
        while True:

            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change_to = 'UP'
                        # self.snake.change_direction('UP')
                    if event.key == pygame.K_DOWN:
                        self.change_to = 'DOWN'
                        # self.snake.change_direction('DOWN')
                    if event.key == pygame.K_LEFT:
                        self.change_to = 'LEFT'
                        # self.snake.change_direction('LEFT')
                    if event.key == pygame.K_RIGHT:
                        self.change_to = 'RIGHT'
                        # self.snake.change_direction('RIGHT')

            # print(self.snake.get_inputs())

            # snake_input = self.snake.get_inputs()
            # fruit_input = self.fruit.get_inputs()

            inputs = self.generate_inputs()
            # print('Inputs -> {}'.format(inputs))
            output = net.activate(inputs)
            self.change_to = self.get_direction(output)

            self.snake.change_direction(self.change_to)
            self.moves += 1

            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            self.check_fruit_collision()

            # Game Over conditions
            if self.check_game_over():
                return self.game_over()

            # displaying score continuously
            # show_score(1, self.white, 'times new roman', 20)

            # Refresh game screen
            if self.display_screen:
                pygame.display.update()

            # Frame Per Second /Refresh Rate
            self.fps.tick(self.snake_speed)

    def generate_inputs(self):
        snake_input = self.snake.get_inputs()

        # print ('Snake input length -> {}'.format(len(snake_input)))

        fruit_input = self.fruit.get_inputs()

        # print ('Fruit input length -> {}'.format(len(fruit_input)))

        inputs = []
        for i in snake_input:
            # inputs.append(i)
            # add all snake inputs
            for j in i:
                inputs.append(j)
        for i in fruit_input:
            # inputs.append(i)
            # add all fruit inputs
            for j in i:
                inputs.append(j)
        # print('Inputs length -> {}'.format(len(inputs)))

        return inputs

    def get_output(self, net):
        inputs = self.generate_inputs()
        output = net.activate(inputs)

        return output

    def get_direction(self, output):

        # print('Output -> {}'.format(output))

        if output[0] > 0.5:
            return 'UP'
        if output[1] > 0.5:
            return 'DOWN'
        if output[2] > 0.5:
            return 'LEFT'
        if output[3] > 0.5:
            return 'RIGHT'

        return self.snake.direction

    def check_fruit_collision(self):
        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        self.snake.body.insert(0, list(self.snake.position))
        if self.snake.position[0] == self.fruit.position[0] and self.snake.position[1] == self.fruit.position[1]:
            self.snake.score += 1
            self.fruit.spawn = False
            self.moves = 0
        else:
            self.snake.body.pop()

        if not self.fruit.spawn:
            self.fruit.position = [random.randrange(1, (self.window_x // 10)) * 10,
                                   random.randrange(1, (self.window_y // 10)) * 10]

        self.fruit.spawn = True

        if self.display_screen:
            self.game_window.fill(self.black)

            for pos in self.snake.body:
                pygame.draw.rect(self.game_window, self.green,
                                 pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(self.game_window, self.white, pygame.Rect(
                self.fruit.position[0], self.fruit.position[1], 10, 10))

    def check_game_over(self):
        # Game Over conditions
        if self.snake.position[0] < 0 or self.snake.position[0] > self.window_x - 10:
            # self.game_over()
            return True
        if self.snake.position[1] < 0 or self.snake.position[1] > self.window_y - 10:
            # self.game_over()
            return True

        # Touching the snake body
        for block in self.snake.body[1:]:
            if self.snake.position[0] == block[0] and self.snake.position[1] == block[1]:
                # self.game_over()
                return True

        if self.moves > self.max_moves:
            return True

        return False

    # def show_score(self, choice, color, font, size):
    #     # creating font object score_font
    #     score_font = pygame.font.SysFont(font, size)
    #
    #     # create the display surface object
    #     # score_surface
    #     # score_surface = score_font.render('Score : ' + str(self.score), True, color)
    #
    #     # create a rectangular object for the text
    #     # surface object
    #     score_rect = score_surface.get_rect()
    #
    #     # displaying text
    #     self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        # print('Game over !')
        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        # creating a text surface on which text
        # will be drawn
        # game_over_surface = my_font.render(
        #     'Your Score is : ' + str(score), True, red)

        # create a rectangular object for the text
        # surface object
        # game_over_rect = game_over_surface.get_rect()

        # setting position of the text
        # game_over_rect.midtop = (window_x / 2, window_y / 4)

        # blit will draw the text on screen
        # self.game_window.blit(game_over_surface, game_over_rect)
        if self.display_screen:
            pygame.display.flip()

        # after 2 seconds we will quit the program
        time.sleep(0)

        # deactivating pygame library
        # pygame.quit()

        # quit the program
        # quit()
        return self.snake.score