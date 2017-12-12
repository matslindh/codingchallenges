from copy import copy


def move_on_board(n, xs, ys):
    board = [[False]*xs for i in range(0, ys)]
    x = y = 0
    moves = 0

    valid_moves = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))

    while moves < n:
        possible_moves = []

        for m in valid_moves:
            if 0 <= (x + m[0]) < xs and 0 <= (y + m[1]) < ys:
                possible_moves.append({
                    'score': (x + m[0]) * 10 + (y + m[1]),
                    'x': x + m[0],
                    'y': y + m[1],
                })
                pass

        best = None
        print(possible_moves)

        for m in possible_moves:
            if board[m['y']][m['x']] == board[y][x] and (best is None or m['score'] < best['score']):
                best = m

        if best is None:
            for m in possible_moves:
                if best is None or best['score'] < m['score']:
                    best = m

        board[y][x] = not board[y][x]
        y = best['y']
        x = best['x']
        moves += 1

        #print_board(board, x, y)

    c = 0
    for row in board:
        c += sum(row)

    return c


def print_board(board, x, y):
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            sym = '#' if board[row][col] else '.'

            if row == y and col == x:
                sym = 'k'

            print(sym, end='')

        print('')

    print('')


def test_move_on_board():
    assert 2 == move_on_board(2, 10, 10)


print(move_on_board(200, 10, 10))