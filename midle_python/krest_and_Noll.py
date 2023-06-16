STATUS_CONTINUE = 'Игра продолжается'
EMTY = '-'
ROW1 = '1'
ROW2 = '2'
ROW3 = '3'
ColA = 'a'
ColB = 'b'
ColC = 'c'
date = {
    ROW1: {
            ColA: EMTY,
            ColB: EMTY,
            ColC: EMTY
        },
    ROW2: {
            ColA: EMTY,
            ColB: EMTY,
            ColC: EMTY
        },
    ROW3: {
            ColA: EMTY,
            ColB: EMTY,
            ColC: EMTY
    }
}
allowe_simbols = ['X', 'O']
allowe_rows = [ROW1, ROW2, ROW3]
allowe_columns = [ColA, ColB, ColC]


def check_if_fame_end():
    winner = STATUS_CONTINUE
    empty_symbols = 0
    for dat in date.values():
        for a in dat.values():
            if a == EMTY:
                empty_symbols += 1
        print()
    # по строкам
    if (date[ROW1][ColA] == date[ROW1][ColB]) and (date[ROW1][ColA] == date[ROW1][ColC]) and date[ROW1][ColA] != EMTY:
        winner = date[ROW1][ColA]
    elif (date[ROW2][ColA] == date[ROW2][ColB]) and (date[ROW2][ColA] == date[ROW2][ColC]) and date[ROW2][ColA] != EMTY:
        winner = date[ROW2][ColA]
    elif (date[ROW3][ColA] == date[ROW3][ColB]) and (date[ROW3][ColA] == date[ROW3][ColC]) and date[ROW3][ColA] != EMTY:
        winner = date[ROW1][ColA]
    # поколонкам
    elif (date[ROW1][ColA] == date[ROW2][ColA]) and (date[ROW1][ColA] == date[ROW3][ColA]) and date[ROW1][ColA] != EMTY:
        winner = date[ROW1][ColA]
    elif (date[ROW1][ColB] == date[ROW2][ColB]) and (date[ROW1][ColB] == date[ROW3][ColB]) and date[ROW1][ColB] != EMTY:
        winner = date[ROW1][ColB]
    elif (date[ROW1][ColC] == date[ROW2][ColC]) and (date[ROW1][ColC] == date[ROW3][ColC]) and date[ROW1][ColC] != EMTY:
        winner = date[ROW1][ColC]
    # по диогоналям
    elif (date[ROW1][ColA] == date[ROW2][ColB]) and (date[ROW1][ColA] == date[ROW3][ColC]) and date[ROW1][ColA] != EMTY:
        winner = date[ROW1][ColA]
    elif (date[ROW1][ColC] == date[ROW2][ColB]) and (date[ROW1][ColC] == date[ROW3][ColA]) and date[ROW1][ColC] != EMTY:
        winner = date[ROW1][ColC]
    # игра окончена закончилось поле
    elif empty_symbols == 0:
        winner = 'Ничья'
    return winner


def input_value(input_value, value):
    column = input_value[1].lower()
    if column not in allowe_columns:
        print(f"Вы ввели не привальную колонку:{column}, разрешённые колонки: {allowe_columns}")
        return
    row = input_value[0]
    if row not in allowe_rows:
        print(f"Вы ввели не привальную строчку:{row}, разрешённые строчки: {allowe_rows}")
        return
    if (value in allowe_simbols) and (date[row][column] == EMTY):
        date[row][column] = value
    else:
        print(f"Вы потеряли ход так как ввели не правильнный символ: {value}, разрешенные:{allowe_simbols}!!")


def print_game_field():
    print('Данные вводятся в формате: 1а')
    print(f"\t\ta\t\tb\t\tc\n")
    print(f"1.\t\t{date[ROW1][ColA]}\t\t{date[ROW1][ColB]}\t\t{date[ROW1][ColC]}\n")
    print(f"2.\t\t{date[ROW2][ColA]}\t\t{date[ROW2][ColB]}\t\t{date[ROW2][ColC]}\n")
    print(f"3.\t\t{date[ROW3][ColA]}\t\t{date[ROW3][ColB]}\t\t{date[ROW3][ColC]}\n")


def run_game():
    print('Игра Крестики_Нолики началась')
    print_game_field()
    current_player = 'X'
    while check_if_fame_end() == STATUS_CONTINUE:
        input_value(
            input(f"Ваш ход({current_player}): "),
            current_player
        )
        print_game_field()
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        check_if_fame_end()
    print(f'Игра завершена, победил: {check_if_fame_end()}')


run_game()