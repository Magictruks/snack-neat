import random

class Maze:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.maze = [[' ' for _ in range(width)] for _ in range(height)]
        self.start_x = random.randint(0, width-1)
        self.start_y = random.randint(0, height-1)
        self.end_x = random.randint(0, width-1)
        self.end_y = random.randint(0, height-1)
        self.maze[self.start_y][self.start_x] = 'S'
        self.maze[self.end_y][self.end_x] = 'E'

    def print_maze(self):
        for row in self.maze:
            print(' '.join(row))

    def is_valid_move(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        if self.maze[y][x] == 'W' or self.maze[y][x] == 'E':
            return False
        return True

    def make_move(self, x, y):
        if not self.is_valid_move(x, y):
            return False
        self.maze[self.start_y][self.start_x] = ' '
        self.start_x = x
        self.start_y = y
        self.maze[self.start_y][self.start_x] = 'S'
        return True

    def is_goal_reached(self):
        if self.start_x == self.end_x and self.start_y == self.end_y:
            return True
        return False

class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.x = maze.start_x
        self.y = maze.start_y

    def get_possible_moves(self):
        moves = []
        if self.maze.is_valid_move(self.x-1, self.y):  # left
            moves.append((self.x-1, self.y))
        if self.maze.is_valid_move(self.x+1, self.y):  # right
            moves.append((self.x+1, self.y))
        if self.maze.is_valid_move(self.x, self.y-1):  # up
            moves.append((self.x, self.y-1))
        if self.maze.is_valid_move(self.x, self.y+1):  # down
            moves.append((self.x, self.y+1))
        return moves

    def make_move(self, x, y):
        self.maze.make_move(x, y)
        self.x = x
        self.y = y

    def get_distance_to_goal(self):
        return abs(self.x-self.maze.end_x) + abs(self.y-self.maze.end_y)

class Game:
    def __init__(self, maze):
        self.maze = maze
        self.agent = Agent(maze)
        self.game_over = False

    def play_turn(self):
        if not self.game_over:
            possible_moves = self.agent.get_possible_moves()
            if len(possible_moves) == 0:
                print("No moves available. Game over.")
                self.game_over = True
            else:
                move = random.choice(possible_moves)
                self.agent.make_move(*move)
                print(f"Agent moved to ({self.agent.x}, {self.agent.y})")
                if self.maze.is_goal_reached():
                    print("Goal reached!")
                    self.game_over = True

    def play(self):
        while not self.game_over:
            self.maze.print_maze()
            self.play_turn()

maze = Maze()
game = Game(maze)
game.play()