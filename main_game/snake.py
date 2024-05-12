class Snake:
    def __init__(self, max_x, max_y):
        # defining snake default position
        self.position = [50, 50]

        # defining first 4 blocks of snake body
        self.body = [
            [50, 50],
            [40, 50],
            [30, 50],
            # [20, 50]
        ]

        self.score = 0
        self.max_x = max_x
        self.max_y = max_y

        # setting default snake direction towards
        # right
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def get_inputs(self):
        # Get first obstacle position in 4 direction + 4 diagonal
        # Obstacle can be map limit or body element

        # Right
        right = [self.position[0] + 10, self.position[1]]
        while right not in self.body and right[0] < self.max_x:
            right = [right[0] + 10, right[1]]

        # Left
        left = [self.position[0] - 10, self.position[1]]
        while left not in self.body and left[0] > 0:
            left = [left[0] - 10, left[1]]

        # Up
        up = [self.position[0], self.position[1] - 10]
        while up not in self.body and up[1] > 0:
            up = [up[0], up[1] - 10]

        # Down
        down = [self.position[0], self.position[1] + 10]
        while down not in self.body and down[1] < self.max_y:
            down = [down[0], down[1] + 10]

        # Up Right
        up_right = [self.position[0] + 10, self.position[1] - 10]
        while up_right not in self.body and up_right[0] < self.max_x and up_right[1] > 0:
            up_right = [up_right[0] + 10, up_right[1] - 10]

        # Up Left
        up_left = [self.position[0] - 10, self.position[1] - 10]
        while up_left not in self.body and up_left[0] > 0 and up_left[1] > 0:
            up_left = [up_left[0] - 10, up_left[1] - 10]

        # Down Right
        down_right = [self.position[0] + 10, self.position[1] + 10]
        while down_right not in self.body and down_right[0] < self.max_x and down_right[1] < self.max_y:
            down_right = [down_right[0] + 10, down_right[1] + 10]

        # Down Left
        down_left = [self.position[0] - 10, self.position[1] + 10]
        while down_left not in self.body and down_left[0] > 0 and down_left[1] < self.max_y:
            down_left = [down_left[0] - 10, down_left[1] + 10]

        return right, left, up, down, up_right, up_left, down_right, down_left

    def change_direction(self, change_direction):
        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if change_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if change_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if change_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Moving the snake
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10