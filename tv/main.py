import television as tv

if __name__ == '__main__':

    tv1 = tv.Television()
    print("Wlaczono telewizor. Mozesz wybrac kanal i glosnosc.")

    while True:
        choice = input("Chcesz zmienic kanal(K), glosnosc(G), sprawdzic status telewizora(S) czy zakonczyc program(E)?\n").upper()
        if choice == "K":
            print(f"Aktualny kanal: {tv1.channel}")
            user_channel = int(input(f"Podaj kanal z zakresu {tv.Television.channels[0]}-{tv.Television.channels[-1]}.\n"))
            tv1.channel = user_channel
        elif choice == "G":
            print(f"Aktualna glosnosc: {tv1.volume}")
            user_volume = int(input(f"Podaj glosnosc z zakresu {tv.Television.volumes[0]}-{tv.Television.volumes[-1]}.\n"))
            tv1.volume = user_volume
        elif choice == "S":
            print(tv1)
        elif choice == "E":
            break
        else:
            print("Podano zla komende, sprobuj ponownie.")
