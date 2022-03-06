import die


class Player:
    def __init__(self, sides, no_of_dice):
        self.dice = [die.Die(sides) for _ in range(no_of_dice)]
        self._value_of_dice = sum(current_die.get_value() for current_die in self.dice)

    def player_roll(self):
        for current_die in self.dice:
            current_die.roll()
            self._value_of_dice += current_die.get_value()

    def get_dice_value(self):
        return self._value_of_dice
