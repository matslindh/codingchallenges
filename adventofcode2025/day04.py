from common import as_board


def count_available_positions(path):
    board = as_board(path)

    rows = len(board)
    cols = len(board[0])
    p1 = 0
    p2 = 0
    iteration = 0

    while True:
        to_remove = []

        for row in range(rows):
            for col in range(cols):
                if board[row][col] != '@':
                    continue

                coords = {
                    (max(0, col - 1), max(0, row - 1)),  # -1, -1
                    (col, max(0, row - 1)),  # 0, -1
                    (min(cols - 1, col + 1), max(0, row - 1), ),  # 1, -1

                    (max(0, col - 1), row),  # -1, 0
                    (min(cols - 1, col + 1), row),  # 1, 0

                    (max(0, col - 1), min(rows - 1, row + 1)),  # -1, 1
                    (col, min(rows - 1, row + 1)),  # 0, 1
                    (min(cols - 1, col + 1), min(rows - 1, row + 1)),  # 1, 1
                }

                coords.discard((col, row))

                taken = sum(
                    1 if board[y][x] == '@' else 0
                    for x, y in coords
                )

                if taken < 4:
                    if iteration == 0:
                        p1 += 1

                    p2 += 1
                    to_remove.append((col, row))

        if not to_remove:
            return p1, p2

        for col, row in to_remove:
            board[row][col] = '.'

        iteration += 1


def test_count_available_positions():
    assert count_available_positions('input/04.test') == (13, 43)


if __name__ == '__main__':
    print(count_available_positions('input/04'))
