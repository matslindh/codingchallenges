from common import as_2d_ints
from functools import cache

def print_map(mapdata, current_y, current_x):
    for y, row in enumerate(mapdata):
        for x, v in enumerate(row):
            if y == current_y and x == current_x:
                v = '.'
            print(v, end='')

        print("")


def explore_trailheads(path):
    mapdata = as_2d_ints(path)

    @cache
    def explore_from(y, x):
        current = mapdata[y][x]

        if current == 9:
            return {(y, x)}, 1

        req = current + 1
        s = set()
        total_paths = 0

        if y > 0 and mapdata[y - 1][x] == req:
            ends, paths = explore_from(y - 1, x)
            s.update(ends)
            total_paths += paths

        if y < len(mapdata) - 1 and mapdata[y + 1][x] == req:
            ends, paths = explore_from(y + 1, x)
            s.update(ends)
            total_paths += paths

        if x > 0 and mapdata[y][x - 1] == req:
            ends, paths = explore_from(y, x - 1)
            s.update(ends)
            total_paths += paths

        if x < len(mapdata[0]) - 1 and mapdata[y][x + 1] == req:
            ends, paths = explore_from(y, x + 1)

            s.update(ends)
            total_paths += paths

        return s, total_paths

    total = 0
    total_s = 0

    for y, row in enumerate(mapdata):
        for x, v in enumerate(row):
            if v == 0:
                tops, s = explore_from(y, x)
                total_s += s
                total += len(tops)

    return total, total_s


def test_explore_trailheads():
    assert explore_trailheads('input/10.test') == (36, 81)


if __name__ == '__main__':
    print(explore_trailheads('input/10'))