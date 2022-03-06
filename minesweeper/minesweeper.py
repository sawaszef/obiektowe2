import random

symbols = [chr(9556), chr(9559), chr(9562), chr(9565), chr(9574), chr(9577), chr(9568), chr(9571), chr(9580)]

def get_number(a, b, text):
    print(f"{text} (od {a} do {b})")
    while True:
        try:
            number = int(input())
            if a <= number <= b:
                return number
            else:
                print("Błędna liczba, spróbuj ponownie.")
                continue
        except ValueError:
            print("Błędna liczba, spróbuj ponownie.")


def lay_mines(rows, columns, no_of_mines):
    mines = set()
    while len(mines) < no_of_mines:
        x, y = random.randrange(rows), random.randrange(columns)
        mines.add((x, y))
    return mines


def number_of_neighboring_mines(field, mines):
    neighbors = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (field[0]+x, field[1]+y) in mines:
                neighbors += 1
    return neighbors


def create_board(rows, columns, bomb_cords):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i, j) in bomb_cords:
                row.append("X")
            else:
                row.append(number_of_neighboring_mines((i, j), bomb_cords))
        board.append(row)
    return board


def create_hidden_board(rows, cols):
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i == 0 and j == 0:
                row.append(chr(9556))
            elif i == 0 and j == cols-1:
                row.append(chr(9559))
            elif i == rows-1 and j == 0:
                row.append(chr(9562))
            elif i == rows-1 and j == cols-1:
                row.append(chr(9565))
            elif i == 0:
                row.append(chr(9574))
            elif i == rows-1:
                row.append(chr(9577))
            elif j == 0:
                row.append(chr(9568))
            elif j == cols - 1:
                row.append(chr(9571))
            else:
                row.append(chr(9580))
        board.append(row)
    return board


def reveal_fields(field, board, hidden_board):
    current_field = board[field[0]][field[1]]
    if hidden_board[field[0]][field[1]] not in symbols:
        return
    if current_field != "X" and current_field > 0:
        hidden_board[field[0]][field[1]] = current_field
    elif current_field != "X" and current_field == 0:
        hidden_board[field[0]][field[1]] = current_field
        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= field[0]+x < len(board) and 0 <= field[1]+y < len(board[0]) and (x, y) != (0, 0):
                    reveal_fields((field[0]+x, field[1]+y), board, hidden_board)
    elif current_field == "X":
        hidden_board[field[0]][field[1]] = "X"


def print_board(board):
    for row in board:
        for element in row:
            print(element, end='')
        print()

