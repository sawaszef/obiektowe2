import account as a

if __name__ == '__main__':

    balance = float(input("Podaj ilosc srodkow jakie chcesz poczatkowo miec na koncie.\n"))
    account1 = a.Account(balance)
    print(account1)

    while True:
        amount = float(input("Podaj ilosc srodkow ktora chcesz dac lub zabrac z konta.\n"))
        choice = input("Chcesz dodac czy zabrac srodki z konta? (add/take). '0' Konczy program.\n")

        if choice == 0:
            break
        elif choice not in ["add", "take"]:
            print("Podaj poprawna komende.")
            continue

        if choice == "add":
            account1.pay(amount)
        elif choice == "take":
            account1.take(amount)

        print(account1)
