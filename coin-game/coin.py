import random

sides = ["orzel", "reszka"]


class Coin:

    def __init__(self, value=0):
        self.side = None
        self.value = value

    def throw(self):
        self.side = random.choice(sides)

    def show_side(self):
        return self.side
