from builtins import range
from collections import Counter


def largest_confined(f, abs_limit):
    points = []

    for coords in f.readlines():
        x, y = map(int, coords.split(','))

        points.append({
            'x': x,
            'y': y,
        })

    w, h = get_sizes(points)
    m = []
    abs_m = []

    # calculate closeness map
    for y in range(0, h + 1):
        line = []
        abs_line = []

        for x in range(0, w + 1):
            closest = get_closest(points, {'x': x, 'y': y})
            absolute = get_absolute_distance(points, {'x': x, 'y': y})
            line.append(closest)
            abs_line.append(absolute)

        m.append(line)
        abs_m.append(abs_line)

    # exclude any points that has a border point
    exclusions = {}

    for y in range(0, h + 1):
        if len(m[y][0]) == 1:
            exclusions[m[y][0][0]] = True

        if len(m[y][w]) == 1:
            exclusions[m[y][w][0]] = True

    for x in range(0, w + 1):
        if len(m[0][x]) == 1:
            exclusions[m[0][x][0]] = True

        if len(m[h][x]) == 1:
            exclusions[m[h][x][0]] = True

    c = Counter()
    a = 0

    for r_idx, row in enumerate(m):
        for c_idx, cell in enumerate(row):
            if len(cell) == 1:
                c.update(cell)

            if abs_m[r_idx][c_idx] < abs_limit:
                a += 1

    for id_ in exclusions:
        del c[id_]

    return c.most_common(1)[0][1], a


def get_closest(input_points, coords):
    best_d = 99999999999
    points = []

    for idx, p in enumerate(input_points):
        d = abs(p['x'] - coords['x']) + abs(p['y'] - coords['y'])

        if d < best_d:
            points = [idx]
            best_d = d
        elif d == best_d:
            points.append(idx)

    return points


def get_absolute_distance(input_points, coords):
    d = 0

    for idx, p in enumerate(input_points):
        d += abs(p['x'] - coords['x']) + abs(p['y'] - coords['y'])

    return d


def get_sizes(points):
    w = 0
    h = 0

    for p in points:
        w = max(w, p['x'])
        h = max(h, p['y'])

    return w, h


def test_largest_confined():
    assert largest_confined(open('input/06.test'), 32) == (17, 16)


if __name__ == '__main__':
    print(largest_confined(open('input/06'), 10000))
