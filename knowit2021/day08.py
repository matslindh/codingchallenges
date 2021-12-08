from functools import reduce


def package_throwinator_3000(lines):
    cities = []
    travel = []

    for line in lines:
        if line.startswith('('):
            cities.append(tuple(map(int, line[1:-1].split(','))))
        else:
            travel.append(int(line))

    ground = [[0]*1000 for _ in range(1000)]
    current = travel[0]

    for destination in travel[1:]:
        draw(ground, cities[current], cities[destination])
        current = destination

    highest = max(reduce(lambda x, y: x + y, ground))
    x1 = None
    y1 = None
    x2 = None
    y2 = None

    for y, row in enumerate(ground):
        if highest in row:
            if x1 is None:
                x1 = row.index(highest)
                row.reverse()
                x2 = len(row) - row.index(highest) - 1
                y1 = y
            else:
                y2 = y

    return (x1, y1), (x2, y2)


def draw(ground, from_, to):
    for y in range(from_[1], to[1], -1 if to[1] < from_[1] else 1):
        for x in range(from_[0], to[0], -1 if to[0] < from_[0] else 1):
            ground[y][x] += 1


def test_package_throwinator_3000():
    assert package_throwinator_3000(open('input/08.test').read().splitlines()) == ((4, 3), (5, 5))


if __name__ == '__main__':
    print(package_throwinator_3000(open('input/08').read().splitlines()))
