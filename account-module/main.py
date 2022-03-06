import account as a

if __name__ == '__main__':

    print("Tworze konto z saldem 50.")
    account1 = a.Account(50)
    print(account1)
    print("Dodaje 25 srodkow do konta.")
    account1.pay(25)
    print(account1)
    print("Zabieram 50 srodkow z konta.")
    account1.take(50)
    print(account1)
    print("Zabieram 30 srodkow z konta, ale jako ze mam mniej niz chce zabrac, zostaje o tym poinformowany i transakcja jest anulowana.")
    account1.take(30)
    print(account1)