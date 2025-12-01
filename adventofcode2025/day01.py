from collections import defaultdict
from common import rs


def safe_rotater(f):
    current = 50
    size = 100
    times_at = defaultdict(int)
    times_over = defaultdict(int)  # we can just use // <size> to see the number of times we additionally pass over 0, but this is more "fun"

    for line in rs(f):
        way, dist = line[0], int(line[1:])
        factor = 1

        if way == 'L':
            factor = -1

        for x in range(0, dist):
            if x > 0:  # moving "over" shouldn't count initial position thank you
                times_over[current] += 1

            current += factor
            current %= size

        times_at[current] += 1

    return times_at, times_over


def test_safe_rotater():
    assert safe_rotater('input/01.test')[0][0] == 3
    print(safe_rotater('input/01.test'))
    assert (safe_rotater('input/01.test')[0][0] + safe_rotater('input/01.test')[1][0]) == 6


if __name__ == '__main__':
    print(safe_rotater('input/01')[0][0])
    print(safe_rotater('input/01')[0][0] + safe_rotater('input/01')[1][0])
