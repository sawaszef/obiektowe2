import minesweeper as m

if __name__ == '__main__':
    rows = m.get_number(8, 30, "Podaj liczbę wierszy.")
    columns = m.get_number(8, 24, "Podaj liczbę kolumn.")
    mines = m.get_number(10, (rows-1)*(columns-1), "Podaj liczbę min.")
    non_bombs = rows * columns - mines

    mine_cords = m.lay_mines(rows, columns, mines)
    board = m.create_board(rows, columns, mine_cords)
    hidden_board = m.create_hidden_board(rows, columns)

    m.print_board(hidden_board)

    is_won = False

    while not any("X" in row for row in hidden_board):
        guessed_fields = 0
        choice_str = input().split(",")
        try:
            choice = int(choice_str[0]), int(choice_str[1])
        except ValueError:
            print("Podaj dwie wspolrzedne, oddzielone przecinkiem.")
            continue
        try:
            m.reveal_fields(choice, board, hidden_board)
        except IndexError:
            print(f"Podaj wspolrzedne zgodne z rozmiarami planszy, wiersz od 0 do {rows-1}, kolumne od 0 do {columns-1}.")
        m.print_board(hidden_board)
        for row in hidden_board:
            for item in row:
                if type(item) == int:
                    guessed_fields += 1
        if guessed_fields == non_bombs:
            is_won = True
            break
    if is_won:
        print("You Won! Congratulations!")
    else:
        print("\nYou lost!")
        m.print_board(board)
