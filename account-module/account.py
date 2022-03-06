class Account:

    def __init__(self, balance):
        self._balance = balance

    def pay(self, amount):
        self._balance += amount

    def take(self, amount):
        if self._balance < amount:
            print("Niewystarczajaca liczba srodkow na koncie.")
        else:
            self._balance -= amount

    def show_balance(self):
        return self._balance

    def __str__(self):
        return f"Srodki na koncie: {self._balance}"
