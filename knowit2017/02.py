
def generate(s_x, s_y):
    map = []

    for y in range(1, s_y + 1):
        m = []

        for x in range(1, s_x + 1):
            calc = x ** 3 + 12 * x * y + 5 * x * y ** 2
            v = count_bits(calc) % 2
            m.append(v)

        map.append(m)

    return map


def count_bits(n):
    c = 0

    while n:
        c += n&1
        n >>= 1

    return c


def explore(map, x=0, y=0):
    s_y = len(map)
    s_x = len(map[0])
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        map[y][x] = 2

        if x + 1 < s_x and not map[y][x+1]:
            queue.append((x+1, y))

        if x - 1 >= 0 and not map[y][x-1]:
            queue.append((x-1, y))

        if y + 1 < s_y and not map[y+1][x]:
            queue.append((x, y+1))

        if y - 1 >= 0 and not map[y-1][x]:
            queue.append((x, y-1))

    not_visited = 0

    for y in range(0, s_y):
        for x in range(0, s_x):
            if not map[y][x]:
                not_visited += 1

    return not_visited


def test_explore():
    map = generate(10, 10)
    assert explore(map) == 11


def test_generate():
    assert generate(2, 2) == [[0, 1], [0, 0]]
    assert generate(3, 3) == [[0, 1, 0], [0, 0, 0], [1, 0, 0]]


def test_count_bits():
    assert count_bits(1) == 1
    assert count_bits(2) == 1
    assert count_bits(3) == 2
    assert count_bits(4) == 1


if __name__ == '__main__':
    map = generate(1000, 1000)
    print(explore(map))