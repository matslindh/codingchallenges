
def winning_sum_for_board_and_drawings(lines, last_wins=False):
    drawings = map(int, lines[0].split(','))  # '7', '4', '9' => 7, 4, 9, ...

    boards = []
    board = []

    for line in lines[2:]:
        if not line:
            boards.append(board)
            board = []
            continue

        elements = line.strip().replace('  ', ' ').split(' ')
        board_line = list(map(int, elements))
        board.append(board_line)

    boards.append(board)

    for number in drawings:
        to_remove = []

        for idx, board in enumerate(boards):
            mark_drawn_numbers_in_board(board, number)

            if check_if_board_is_winner(board):
                if not last_wins:
                    return calculate_board_value(board) * number

                to_remove.append(idx)

        if len(boards) == 1 and check_if_board_is_winner(boards[0]):
            return calculate_board_value(boards[0]) * number

        for idx in sorted(to_remove, reverse=True):
            del boards[idx]


def calculate_board_value(board):
    s = 0

    for row in board:
        s += sum(filter(lambda x: x is not None, row))

    return s


def mark_drawn_numbers_in_board(board, number):
    for row in board:
        try:
            number_idx = row.index(number)
            row[number_idx] = None
        except ValueError:
            pass


def check_if_board_is_winner(board):
    for row in board:
        found_value = False

        for value in row:
            if value is not None:
                found_value = True
                break

        if not found_value:
            return True

    for column in range(len(board[0])):
        found_value = False

        for row in board:
            if row[column] is not None:
                found_value = True
                break

        if not found_value:
            return True

    return False


def test_winning_sum_for_board_and_drawings():
    assert winning_sum_for_board_and_drawings(open('input/04.test').read().split("\n")) == 4512


def test_winning_sum_for_board_and_drawings_last_wins():
    assert winning_sum_for_board_and_drawings(open('input/04.test').read().split("\n"), last_wins=True) == 1924


def test_mark_draw_numbers_in_board():
    board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

    mark_drawn_numbers_in_board(board, 4)

    assert board[0][3] is None
    assert board[0][2] is not None


def test_board_is_a_winner():
    board_winner_row = [[None, None], [1, 2]]
    board_winner_column = [[None, 1], [None, 2]]
    board_loser = [[None, 1], [3, 2]]

    assert not check_if_board_is_winner(board_loser)
    assert check_if_board_is_winner(board_winner_row)
    assert check_if_board_is_winner(board_winner_column)


def test_calculate_board_value():
    assert calculate_board_value([[None, None], [1, 2]]) == 3
    assert calculate_board_value([[None, 1], [None, 2]]) == 3
    assert calculate_board_value([[None, 1], [3, 2]]) == 6


if __name__ == '__main__':
    print(winning_sum_for_board_and_drawings(open("input/04").read().split("\n")))
    print(winning_sum_for_board_and_drawings(open("input/04").read().split("\n"), last_wins=True))