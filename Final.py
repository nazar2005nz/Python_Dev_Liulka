from random import randrange

def display_board(board):
    """
    Функція для виведення ігрової дошки.
    """
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")


def enter_move(board):
    """
    Функція для отримання ходу користувача.
    """
    while True:
        move = input("Введіть номер поля (1-9): ")
        if not move.isdigit():
            print("Невірний формат. Спробуйте ще раз.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Номер має бути від 1 до 9.")
            continue
        for i in range(3):
            for j in range(3):
                if board[i][j] == str(move):
                    board[i][j] = 'O'
                    return
        print("Поле вже зайнято. Спробуйте ще раз.")


def make_list_of_free_fields(board):
    """
    Функція для визначення вільних полів на дошці.
    """
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ('X', 'O'):
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    """
    Функція для перевірки, чи є переможець.
    """
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    """
    Функція для ходу комп'ютера.
    """
    free_fields = make_list_of_free_fields(board)
    move = free_fields[randrange(len(free_fields))]
    board[move[0]][move[1]] = 'X'


# Ігровий цикл
board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
board[1][1] = 'X'  # Перший хід комп'ютера

while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("Комп'ютер виграв!")
        break
    if not make_list_of_free_fields(board):
        print("Нічия!")
        break

    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("Ви виграли!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Нічия!")
        break

    draw_move(board)
