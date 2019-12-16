
def fjordify(f):
    lines = [line.strip() for line in open(f).readlines()]
    width = len(lines[0])
    fjord = {
        'map': [],
        'boat': None,
    }

    for y, line in enumerate(lines):
        row = [' '] * width

        for x in range(0, len(line)):
            if line[x] == '#':
                row[x] = '#'
            elif line[x] == 'B':
                row[x] = 'B'
                fjord['boat'] = (x, y)

        fjord['map'].append(row)

    return fjord


def navigate(fjord):
    x, y = fjord['boat']
    d = 'ne'
    changed = 0

    while True:
        x += 1

        if x == len(fjord['map'][0]):
            break

        if d == 'ne':
            y -= 1
        elif d == 'se':
            y += 1

        fjord['map'][y][x] = '/' if d == 'ne' else '\\'

        if (d == 'ne' and fjord['map'][y-3][x] == '#') or \
           (d == 'se' and fjord['map'][y+3][x] == '#'):
            changed += 1

            if d == 'ne':
                y -= 1
                d = 'se'
            else:
                d = 'ne'
                y += 1

    return changed + 1


def print_map(fjord):
    print("\n")
    for row in fjord['map']:
        print(''.join(row))


def test_fjordify():
    fjord = fjordify('input/fjord.test.txt')

    assert len(fjord['map']) == 11
    assert len(fjord['map'][0]) == 20
    assert fjord['boat'] == (1, 8)

    result = navigate(fjord)
    assert 5 == result


if __name__ == '__main__':
    fjord = fjordify('input/fjord.txt')
    print(navigate(fjord))
