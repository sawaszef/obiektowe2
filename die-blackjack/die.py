import random


class Die:
    def __init__(self, sides):
        self._sides = sides
        self._value = 0

    def roll(self):
        self._value = random.randint(1, self._sides)

    def get_sides(self):
        return self._sides

    def get_value(self):
        return self._value
