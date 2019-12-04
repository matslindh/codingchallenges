def snail_it(coords):
    grid = {
        0: {
            0: 1
        }
    }
    time = 0
    x = 0
    y = 0

    for x_d, y_d in coords:
        x_step = -1 if x_d < x else 1
        y_step = -1 if y_d < y else 1

        while x != x_d:
            x += x_step
            slime(grid, x, y)
            time += grid[y][x]

        while y != y_d:
            y += y_step
            slime(grid, x, y)
            time += grid[y][x]

    return time


def slime(grid, x, y):
    if y not in grid:
        grid[y] = {}

    if x not in grid[y]:
        grid[y][x] = 0

    grid[y][x] += 1


def snail_it_file(fname, header=True):
    lines = open(fname).readlines()

    if header:
        lines.pop(0)

    coords = [tuple(map(int, line.strip().split(','))) for line in lines]
    return snail_it(coords)


def test_snail_it():
    assert 14 == snail_it_file('input/04.test', header=False)


if __name__ == '__main__':
    print(snail_it_file('input/coords.csv', header=True))