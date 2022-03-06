import player

if __name__ == '__main__':

    pc = player.Player(6, 2)
    user = player.Player(6, 2)

    print(f"Witaj w grze 'Oczko'!\n"
          f"Celem gry jest wyrzucenie wiekszej liczby od twojego przeciwnika, lecz nie wiekszej niz 21."
          f" Rzucasz {len(user.dice)} {user.dice[0].get_sides()}-sciennymi kostkami.")

    while pc.get_dice_value() < 17:
        pc.player_roll()

    print("Rzucasz koścmi po raz pierwszy.")
    user.player_roll()

    while True:
        if user.get_dice_value() > 21:
            break
        print(f"Aktualna liczba wyrzuconych przez Ciebie oczek to {user.get_dice_value()}.")
        to_roll = input("Czy chcesz rzucic ponownie? T/N\n").upper()
        if to_roll == "T":
            user.player_roll()
        else:
            break

    print(f"Wyrzucone przez Ciebie oczka: {user.get_dice_value()}\n"
          f"Wyrzucone oczka przez Komputer: {pc.get_dice_value()}")

    has_player_won: bool

    if user.get_dice_value() > 21:
        has_player_won = False
    elif pc.get_dice_value() > 21:
        has_player_won = True
    elif user.get_dice_value() > pc.get_dice_value():
        has_player_won = True
    else:
        has_player_won = False

    if has_player_won:
        print("Gratulacje, Wygrales!")
    else:
        print("Przykro mi, przegrales. :c")
