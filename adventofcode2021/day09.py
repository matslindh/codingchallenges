from functools import reduce
from operator import mul


def risk_from_heightmap(heightmap):
    heightmap = [list(map(int, row)) for row in heightmap]
    s = 0

    for idx, row in enumerate(heightmap):
        for c_idx, column in enumerate(row):
            valid = True

            if idx > 0 and heightmap[idx-1][c_idx] <= column:
                valid = False

            if idx < (len(heightmap) - 1) and heightmap[idx+1][c_idx] <= column:
                valid = False

            if c_idx > 0 and heightmap[idx][c_idx-1] <= column:
                valid = False

            if c_idx < (len(row) - 1) and heightmap[idx][c_idx+1] <= column:
                valid = False

            if valid:
                s += 1 + column

    return s


def three_largest_basins_from_heightmap(heightmap):
    heightmap = [list(map(int, row)) for row in heightmap]
    basins = []

    for idx, row in enumerate(heightmap):
        for c_idx, column in enumerate(row):
            if column is None or column == 9:
                continue

            basins.append(bfs(heightmap, c_idx, idx))

    for row in heightmap:
        print(''.join([' ' if column is None else 'X' for column in row]))

    return reduce(mul, sorted(basins, reverse=True)[:3])


def bfs(heightmap, x, y):
    def valid(x_v, y_v):
        return heightmap[y_v][x_v] is not None and heightmap[y_v][x_v] != 9

    queue = [(x, y)]
    size = 0

    while queue:
        x, y = queue.pop(0)

        if not valid(x, y):
            continue

        heightmap[y][x] = None
        size += 1

        if y > 0 and valid(x, y - 1):
            queue.append((x, y - 1))

        if y < (len(heightmap) - 1) and valid(x, y + 1):
            queue.append((x, y + 1))

        if x > 0 and valid(x - 1, y):
            queue.append((x - 1, y))

        if x < (len(heightmap[y]) - 1) and valid(x + 1, y):
            queue.append((x + 1, y))

    return size


def test_risk_from_heightmap():
    assert risk_from_heightmap(open('input/09.test').read().splitlines()) == 15


def test_three_largest_basins_from_heightmap():
    assert three_largest_basins_from_heightmap(open('input/09.test').read().splitlines()) == 1134


if __name__ == '__main__':
    print(risk_from_heightmap(open('input/09').read().splitlines()))
    print(three_largest_basins_from_heightmap(open('input/09').read().splitlines()))