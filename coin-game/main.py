import coin as c

# Symulacja 15 rzutow moneta
def throw_15():
    coin_list = []
    for _ in range(15):
        coin_list.append(c.Coin())

    counter = {"orzel": 0, "reszka": 0}

    for coin in coin_list:
        coin.throw()
        if coin.side == "orzel":
            counter["orzel"] += 1
        else:
            counter["reszka"] += 1
        print(coin.show_side())

    print(f"Liczba orlow: {counter['orzel']}\nLiczba reszek: {counter['reszka']}")


if __name__ == "__main__":

    #throw_15()

    wins_losses = {"wins": 0, "losses": 0}
    coin_list = []
    for i in [1, 2, 5]:
        coin_list.append(c.Coin(i))

    for i in range(100):
        balance = 0
        while balance < 20:
            for coin in coin_list:
                coin.throw()
                if coin.side == "orzel":
                    balance += coin.value
        if balance == 20:
            print("Wygrales!")
            wins_losses["wins"] += 1
        else:
            wins_losses["losses"] += 1

    print(f"Zwyciestwa: {wins_losses['wins']}\nPorazki: {wins_losses['losses']}")