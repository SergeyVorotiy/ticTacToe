_player = 1
def field_output(field):
    output = "  0 1 2\n"
    k = 0
    for row in field:
        output = output + str(k)
        for column in row:
            output = output + " " + column
        output = output + "\n"
        k = k + 1
    return output
def rec_move_in_field(x, y, char):
    tic_tac_toe_field[x][y] = char


def is_game_over(field):
    if ((field[0][0] == 'x' and field[0][1] == 'x' and field[0][2] == 'x') or (
            field[0][0] == 'o' and field[0][1] == 'o' and field[0][2] == 'o')) or (
            (field[1][0] == 'x' and field[1][1] == 'x' and field[1][2] == 'x') or (
            field[1][0] == 'o' and field[1][1] == 'o' and field[1][2] == 'o')) or (
            (field[2][0] == 'x' and field[2][1] == 'x' and field[2][2] == 'x') or (
            field[2][0] == 'o' and field[2][1] == 'o' and field[2][2] == 'o')) or (
            (field[0][0] == 'x' and field[1][0] == 'x' and field[2][0] == 'x') or (
            field[0][0] == 'o' and field[1][0] == 'o' and field[2][0] == 'o')) or (
            (field[0][1] == 'x' and field[1][1] == 'x' and field[2][1] == 'x') or (
            field[0][1] == 'o' and field[1][1] == 'o' and field[2][1] == 'o')) or (
            (field[0][2] == 'x' and field[1][2] == 'x' and field[2][2] == 'x') or (
            field[0][2] == 'o' and field[1][2] == 'o' and field[2][2] == 'o')) or (
            (field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x') or (
            field[0][0] == 'o' and field[1][1] == 'o' and field[2][2] == 'o')) or (
            (field[2][0] == 'x' and field[1][1] == 'x' and field[0][2] == 'x') or (
            field[2][0] == 'o' and field[1][1] == 'o' and field[0][2] == 'o')):
        return False
    else:
        if "-" not in field[0] and "-" not in field[1] and "-"not in field[2]:
            return False
        return True
print("Поиграем в крестики нолики!")
play_again = "y"
player_1_name = input("Введите имя первого игрока - ")
player_2_name = input("Введите имя второго игрока - ")
while play_again == "y":
    print("Начнем же игру!")
    tic_tac_toe_field = [['-' for row in range(3)] for column in range(3)]
    print(field_output(tic_tac_toe_field))
    _player = 1
    while is_game_over(tic_tac_toe_field):
        if _player == 1:
            print(player_1_name)
            x = int(input("Введите номер строки вашего хода - ") or 5)
            y = int(input("Введите номер столбца вашего хода - ") or 5)
            if -1<x<3 and -1<y<3:
                if tic_tac_toe_field[x][y] == "-":
                    rec_move_in_field(x, y, "x")
                    _player = 2
                else:
                    print("Выберите другие координаты")
                    continue
            else:
                print("Выберите другие координаты")
                continue
            print(field_output(tic_tac_toe_field))

        elif _player == 2:
            print(player_2_name)
            x = int(input("Введите номер строки вашего хода - ") or 5)
            y = int(input("Введите номер столбца вашего хода - ") or 5)
            if -1 < x < 3 and -1 < y < 3:
                if tic_tac_toe_field[x][y] == "-":
                    rec_move_in_field(x, y, "o")
                    _player = 1
                else:
                    print("Выберите другие координаты")
                    continue
            else:
                print("Выберите другие координаты")
                continue
            rec_move_in_field(x, y, "o")

            print(field_output(tic_tac_toe_field))
        print("Игра окончена!\n")
    play_again = input("Сыграть ещё?(y/no)")