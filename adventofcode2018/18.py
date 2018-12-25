from collections import Counter


def simulate(f, iterations):
    forest = []
    seen = {}
    period = []
    printed = False

    for line in f.readlines():
        forest.append(line.strip())

    for i in range(0, iterations):
        if i % 100 == 0:
            print(i)

        new = []

        for y, row in enumerate(forest):
            line = ''

            for x, c in enumerate(row):
                counts = count_close(forest, y, x)

                if c == '.':
                    if counts['trees'] > 2:
                        line += '|'
                    else:
                        line += '.'

                if c == '|':
                    if counts['lumberyards'] > 2:
                        line += '#'
                    else:
                        line += '|'

                if c == '#':
                    if counts['lumberyards'] and counts['trees']:
                        line += '#'
                    else:
                        line += '.'

            new.append(line)

        checksum = '-'.join(new)

        if checksum in seen and not printed:
            printed = True
            state = (iterations - seen[checksum]) % (i - seen[checksum])
            idx = seen[checksum] + state

            # 208750 -- too high
            # 194959 -- too low
            print(state)
            print('period', i, 'from', seen[checksum])
            print('idx', )
            c = Counter(period[idx - 1])
            return c['#'] * c['|']

        seen[checksum] = i
        period.append(checksum)
        forest = new

    c = Counter()

    for row in forest:
        c.update(row)

    return c['#'] * c['|']


def count_close(forest, y, x):
    counts = {
        'trees': 0,
        'lumberyards': 0,
    }

    if y > 0 and x > 0:
        add_count(counts, forest[y-1][x-1])

    if y > 0:
        add_count(counts, forest[y-1][x])

    if x > 0:
        add_count(counts, forest[y][x-1])

    if y < (len(forest) - 1):
        add_count(counts, forest[y + 1][x])

    if x < (len(forest[y]) - 1):
        add_count(counts, forest[y][x + 1])

    if y < (len(forest) - 1) and x < (len(forest[y]) - 1):
        add_count(counts, forest[y + 1][x + 1])

    if y < (len(forest) - 1) and x > 0:
        add_count(counts, forest[y + 1][x - 1])

    if x < (len(forest[y]) - 1) and y > 0:
        add_count(counts, forest[y - 1][x + 1])

    return counts


def add_count(counts, letter):
    if letter == '|':
        counts['trees'] += 1
    elif letter == '#':
        counts['lumberyards'] += 1


def test_simulate():
    assert simulate(open('input/18.test'), iterations=10) == 1147


if __name__ == '__main__':
    print(simulate(open('input/18'), iterations=1_000_000_000))