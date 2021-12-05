def line_intersection_count(line_list, count_diagonals=False):
    count_map = {}

    # 3,4 -> 2,5
    for line in line_list:
        xy, _, xy2 = line.split(' ')
        x1, y1 = map(int, xy.split(','))
        x2, y2 = map(int, xy2.split(','))

        if x1 == x2:
            y_start,  y_end = (y1, y2) if y1 < y2 else (y2, y1)

            for y in range(y_start, y_end + 1):
                increment_map_count(count_map, x1, y)

        elif y1 == y2:
            x_start,  x_end = (x1, x2) if x1 < x2 else (x2, x1)

            for x in range(x_start, x_end + 1):
                increment_map_count(count_map, x, y1)

        elif count_diagonals:
            x_delta = 1 if x1 < x2 else -1
            y_delta = 1 if y1 < y2 else -1

            while x1 != x2:
                increment_map_count(count_map, x1, y1)

                x1 += x_delta
                y1 += y_delta

            increment_map_count(count_map, x1, y1)

    c = 0

    for row, columns in count_map.items():
        for column, count in columns.items():
            if count > 1:
                c += 1

    return c


def increment_map_count(count_map, x, y):
    if y not in count_map:
        count_map[y] = {}

    if x not in count_map[y]:
        count_map[y][x] = 0

    count_map[y][x] += 1


def test_line_intersection_count():
    assert line_intersection_count(open('input/05.test').read().split("\n")) == 5


def test_line_intersection_count_with_diagonals():
    assert line_intersection_count(open('input/05.test').read().split("\n"), count_diagonals=True) == 12


if __name__ == '__main__':
    print(line_intersection_count(open('input/05').read().split("\n")))
    print(line_intersection_count(open('input/05').read().split("\n"), count_diagonals=True))