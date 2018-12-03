
def count_overlaps(f):
    map = {}
    overlaps = {}

    for y in range(0, 1000):
        map[y] = {}

        for x in range(0, 1000):
            map[y][x] = []

    for line_no, line in enumerate(f.readlines()):
        idx, _, coords, size = line.strip().split(' ')
        x, y = coords[:-1].split(',')
        xs, ys = size.split('x')
        overlaps[idx] = False

        x = int(x)
        y = int(y)
        xs = int(xs)
        ys = int(ys)

        for y_i in range(y, y+ys):
            for x_i in range(x, x + xs):
                map[y_i][x_i].append(idx)

    count = 0

    for y in map:
        for x in map[y]:
            if len(map[y][x]) > 1:
                for claim in map[y][x]:
                    if claim in overlaps:
                        del overlaps[claim]

                count += 1

    return count, list(overlaps.keys())[0]


def test_overlap():
    assert count_overlaps(open('input/03.test')) == (4, '#3')


if __name__ == '__main__':
    print(count_overlaps(open('input/03')))
