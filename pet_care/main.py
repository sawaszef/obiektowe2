import pet

if __name__ == '__main__':

    pet1 = pet.Pet()

    while not pet1.name:
        name_pet = input("Podaj imie jakim chcesz nazwac swojego pupila.\n")
        pet1.name = name_pet
    print(f"Nazwales zwierzaka {pet1.name}!")

    while True:
        activity = int(input("\nPodaj czynnosc ktora chcesz wykonac:\n1. Nakarm\n2. Pobaw sie\n"
                             "3. Porozmawiaj\n4. Wyswietl poziom glodu i znudzenia\n"
                         "5. Zakoncz program\n"))
        if activity not in range(1, 6):
            print("Podaj poprawny numer czynnosci.")
        elif activity == 1:
            food = input(f"Podaj liczbe smakolykow ktore chcesz dac {pet1.name}. (Domyslnie 4)\n")
            if food.isdigit():
                pet1.eat(int(food))
            else:
                pet1.eat()
        elif activity == 2:
            play_time = input(f"Podaj czas ktory chcesz spedzic na zabawie z {pet1.name}. (Domyslnie 4)")
            if play_time.isdigit():
                pet1.play(int(play_time))
            else:
                pet1.play()
        elif activity == 3:
            pet1.talk()
        elif activity == 4:
            print(pet1)
        elif activity == 5:
            break
        else:
            print("Podaj poprawny numer czynnosci.")
        input("\nWcisnij dowolny przycisk by kontynuowac.")
