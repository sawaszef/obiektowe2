import pickle
import smartphone as sm

if __name__ == '__main__':

    erase = input("Czy chcesz wyczyscic obiekty z pliku 'phones.dat'? (T/N)\n").upper()
    if erase == "T":
        with open("phones.dat", "w") as file:
            file.write("")
    else:
        print("Podano komende 'N' lub bledna, plik nie zostal wyczyszczony.")

    while True:
        choice = input("Czy chcesz dodac obiekt 'smartphone' do pliku? (T/N)\n").upper()

        if choice == "N":
            break
        elif choice != "T":
            print("Podaj poprawna komende.")
            continue
        else:
            manufacturer = input("Podaj producenta telefonu.\n")
            model = input("Podaj model telefonu.\n")
            price = input("Podaj cene telefonu.\n")

            smartphone = sm.Smartphone(manufacturer, model, price)

            with open("phones.dat", "ab") as file:
                pickle.dump(smartphone, file)

    smartphones = []
    print("Nastepuje 'odpeklowanie' obiektow z pliku.\n")

    with open("phones.dat", "rb") as file:
        while True:
            try:
                smartphones.append(pickle.load(file))
            except EOFError:
                break

    for phone in smartphones:
        print(f"{phone}\n")
