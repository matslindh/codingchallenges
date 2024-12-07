def count_xmas(path):
    field = open(path).read().splitlines()

    find = {'XMAS', 'SAMX'}
    count = 0

    x_limit = len(field[0]) - 4
    y_limit = len(field) - 4

    for y in range(len(field)):
        for x in range(len(field)):
            words = []

            if x <= x_limit:
                words.append(field[y][x:x + 4])

            if y <= y_limit:
                words.append(field[y][x] + field[y + 1][x] + field[y + 2][x] + field[y + 3][x])

                if x <= x_limit:
                    # down right / up left
                    words.append(field[y][x] + field[y+1][x+1] + field[y+2][x+2] + field[y+3][x+3])

                if x >= 3:
                    # down left / up right
                    words.append(field[y][x] + field[y+1][x-1] + field[y+2][x-2] + field[y+3][x-3])

            for word in words:
                if word in find:
                    count += 1

    return count


def count_xmas_x(path):
    field = open(path).read().splitlines()
    count = 0

    for y in range(1, len(field) - 1):
        for x in range(1, len(field) - 1):
            if not field[y][x] == 'A':
                continue

            count += (
                (
                    (field[y - 1][x - 1] == 'S' and field[y + 1][x + 1] == 'M') or
                    (field[y - 1][x - 1] == 'M' and field[y + 1][x + 1] == 'S')
                ) and (
                    (field[y + 1][x - 1] == 'S' and field[y - 1][x + 1] == 'M') or
                    (field[y + 1][x - 1] == 'M' and field[y - 1][x + 1] == 'S')
                )
            )

    return count



def test_count_xmas():
    assert count_xmas("input/04.test") == 18


def test_count_xmas_x():
    assert count_xmas_x("input/04.test") == 9


if __name__ == '__main__':
    print(count_xmas("input/04"))
    print(count_xmas_x("input/04"))
