from collections import defaultdict


def draw_line_in_map(caves, p1: tuple, p2: tuple):
    if p1[0] == p2[0]:
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            caves[y][p1[0]] = '#'
    else:
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            caves[p1[1]][x] = '#'


def load_map(path):
    lines = set(open(path).read().splitlines())
    caves = defaultdict(dict)

    for line in lines:
        parts = line.split(' -> ')

        for idx in range(1, len(parts)):
            p1 = tuple(map(int, parts[idx - 1].split(',')))
            p2 = tuple(map(int, parts[idx].split(',')))
            draw_line_in_map(caves, p1, p2)

    return caves


def drop_snow(caves):
    max_y = max(caves.keys())

    while True:
        x, y = 500, 0

        while True:
            while caves.get(y + 1, {}).get(x) is None:
                y += 1

                if y > max_y:
                    return

            if caves.get(y + 1, {}).get(x - 1) is None:
                x -= 1
                y += 1
                continue

            if caves.get(y + 1, {}).get(x + 1) is None:
                x += 1
                y += 1
                continue

            caves[y][x] = 'o'

            if y == 0 and x == 500:
                return

            break


def count_snow(caves):
    snowdrops = 0

    for row in caves.values():
        snowdrops += list(row.values()).count('o')

    return snowdrops


def print_caves(caves, width, height):
    print('')
    for y in range(height + 1):
        for x in range(500 - width//2, 500 + width//2):
            sym = caves.get(y, {}).get(x)

            if sym is None:
                sym = '.'

            print(sym, end='')

        print('')


def units_before_infinity(path):
    caves = load_map(path)
    drop_snow(caves)
    first = count_snow(caves)

    floor_at = max(caves.keys()) + 2
    draw_line_in_map(caves, (300, floor_at), (700, floor_at))

    drop_snow(caves)
    second = count_snow(caves)
    return first, second


def test_units_before_infinity():
    assert units_before_infinity('input/14.test') == (24, 93)


if __name__ == '__main__':
    print(units_before_infinity('input/14'))