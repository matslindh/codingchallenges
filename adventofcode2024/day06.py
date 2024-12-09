def read_map(path):
    mapdata = open(path).read().splitlines()
    start = None

    for idx, row in enumerate(mapdata):
        if '^' in row:
            start = row.index('^'), idx
            break

    mapdata = [
        list(row)
        for row in mapdata
    ]

    return mapdata, start


def explore_map(mapdata, start):
    current = 'U'

    movement = {
        'U': 'R',
        'R': 'D',
        'D': 'L',
        'L': 'U'
    }

    pos = start
    visited = { start }
    visited_dir = { (start, 'U') }
    looped = False
    invalid = False
    changed_direction_previous = False

    while True:
        # print_map(mapdata=mapdata, current=pos, visited=visited)

        if current == 'U':
            n = pos[0], pos[1] - 1
        elif current == 'R':
            n = pos[0] + 1, pos[1]
        elif current == 'D':
            n = pos[0], pos[1] + 1
        elif current == 'L':
            n = pos[0] - 1, pos[1]
        else:
            raise Exception('invalid direction')

        if (n, current) in visited_dir:
            looped = True
            break

        if n[0] < 0 or n[0] >= len(mapdata[0]) or n[1] < 0 or n[1] >= len(mapdata):
            break

        if mapdata[n[1]][n[0]] == '#':
            current = movement[current]

            if changed_direction_previous:
                invalid = True

            changed_direction_previous = True
            continue

        visited.add(n)
        visited_dir.add((n, current))
        pos = n
        changed_direction_previous = False

    return visited, looped, invalid


def print_map(mapdata, current, visited):
    print("")
    for y, row in enumerate(mapdata):
        for x, c in enumerate(row):
            if (x, y) == current:
                c = 'p'
            elif (x, y) in visited:
                c = '-'

            print(c, end='')

        print('')


def try_locations(mapdata, start, visited):
    loop_count = 0

    for pos in sorted(visited):
        if pos == start:
            continue

        x, y = pos
        mapdata[y][x] = '#'
        visited, looped, invalid = explore_map(mapdata, start)
        mapdata[y][x] = '.'

        if invalid:
            continue

        loop_count += looped

    return loop_count


def test_explore_map():
    mapdata, start = read_map('input/06.test')
    visited, looped, invalid = explore_map(mapdata=mapdata, start=start)

    assert len(visited) == 41
    assert not looped


def test_try_locations():
    mapdata, start = read_map('input/06.test')
    visited, _, invalid = explore_map(mapdata=mapdata, start=start)
    assert try_locations(mapdata=mapdata, start=start, visited=visited) == 6



if __name__ == '__main__':
    mapdata, start = read_map('input/06')
    visited, *_ = explore_map(mapdata=mapdata, start=start)
    print(len(visited))
    # 1129 => too low
    print(try_locations(mapdata=mapdata, start=start, visited=visited))