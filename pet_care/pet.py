class Pet:

    def __init__(self):
        self._name = ""
        self.hunger = 0
        self.tiredness = 0

    @property
    def name(self):
        return self._name

    @property
    def mood(self):
        overall = self.hunger + self.tiredness
        if overall < 5:
            return "szczesliwy"
        elif overall < 11:
            return "zadowolony"
        elif overall < 16:
            return "poddenerwowany"
        else:
            return "wsciekly"

    @name.setter
    def name(self, new_name):
        if new_name.isalpha() and len(new_name) >= 3:
            self._name = new_name
        else:
            print("Imie zwierzaka powinno zawierac co najmniej 3 znaki i skladac sie tylko z liter.")

    def _passage_of_time(self):
        self.tiredness += 1
        self.hunger += 1

    def talk(self):
        print(f"{self.name} jest {self.mood}.")
        self._passage_of_time()

    def eat(self, food=4):
        if food > 0 and self.hunger - food >= -1:
            self.hunger -= food
            print(f"Karmisz zwierzaka {food} smakolykami.")
        else:
            print("Liczba smakolykow powinna byc wieksza od 0 i mniejsza lub"
                  " rowna aktualnego stanu glodu pomniejszonego o 1.")
        self._passage_of_time()

    def play(self, fun=4):
        if fun > 0 and self.tiredness - fun >= -1:
            self.tiredness -= fun
        else:
            print("Wartosc czasu zabawy powinna byc wieksza od 0"
                  " i mniejsza lub rowna aktualnego stanu znudzenia pomniejszonego o 1.")
        self._passage_of_time()

    def __str__(self):
        return f"Imie: {self.name}\nGlod: {self.hunger}\nZnudzenie: {self.tiredness}"
