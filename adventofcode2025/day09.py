from common import rs
from itertools import combinations


def make_largest_rectangle(path):
    coords = []

    for line in rs(path):
        x, y = line.split(',')

        coords.append(
            (int(x), int(y))
        )

    b = 0

    for p1, p2 in combinations(coords, r=2):
        a = abs(p1[0] - p2[0] + 1) * \
            abs(p1[1] - p2[1] + 1)

        if a > b:
            b = a

    return b
            


def test_make_largest_rectangle():
    assert make_largest_rectangle('input/09.test') == 50


if __name__ == '__main__':
    print(make_largest_rectangle('input/09'))
