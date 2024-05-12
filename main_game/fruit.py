import random


class Fruit:
    def __init__(self, x, y):
        # fruit position
        self.position = [random.randrange(1, (x // 10)) * 10,
                         random.randrange(1, (y // 10)) * 10]

        self.spawn = True

    def get_inputs(self):
        return [self.position]