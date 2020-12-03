from functools import reduce
from operator import mul


def toboggan_raceway(map_file, x_delta=3, y_delta=1):
    forest = [x.strip() for x in open(map_file).readlines()]
    height = len(forest)
    width = len(forest[0])
    trees = 0
    y = 0
    x = 0

    while y < height:
        trees += int(forest[y][x % width] == '#')
        x += x_delta
        y += y_delta

    return trees


def test_toboggan_raceway():
    assert 7 == toboggan_raceway('input/03.test')


if __name__ == '__main__':
    print(toboggan_raceway('input/03'))

    print(reduce(mul, [
        toboggan_raceway('input/03', x_delta=1, y_delta=1),
        toboggan_raceway('input/03', x_delta=3, y_delta=1),
        toboggan_raceway('input/03', x_delta=5, y_delta=1),
        toboggan_raceway('input/03', x_delta=7, y_delta=1),
        toboggan_raceway('input/03', x_delta=1, y_delta=2),
    ]))