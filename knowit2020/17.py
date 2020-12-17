from bitarray import bitarray


def map_reader(f):
    lines = ['x' + line.strip("\n") + 'x' for line in open(f).readlines()]
    lines.insert(0, 'x' * len(lines[0]))
    lines.append('x' * len(lines[0]))
    map_data = []
    w = 0
    printable_map = []
    cleaned_map = []

    for line in lines:
        w = max(w, len(line))
        map_data.append(bitarray(line.replace('x', '1').replace(' ', '0')))
        cleaned_map.append(bitarray(len(line)))
        printable_map.append(list(line))

    return {
        'height': len(lines),
        'width': w,
        'map': map_data,
        'cleaned_map': cleaned_map,
        'printable_map': printable_map
    }


def place_robot(map_data):
    robot = [
        bitarray('0011100'),
        bitarray('0111110'),
        bitarray('1111111'),
        bitarray('1111111'),
        bitarray('1111111'),
        bitarray('0111110'),
        bitarray('0011100'),
    ]

    cleaner = [
        bitarray('111000111'),
        bitarray('111111111'),
        bitarray('111111111'),
        bitarray('011111110'),
        bitarray('011111110'),
        bitarray('011111110'),
        bitarray('111111111'),
        bitarray('111111111'),
        bitarray('111000111'),
    ]

    for y in range(3, map_data['height'] - 3):
        for x in range(3, map_data['width'] - 3):
            intersects = False

            for ridx, r in enumerate(robot):
                # robot intersects
                if (map_data['map'][y-3+ridx][x-3:x+4] & r).any():
                    intersects = True
                    break

            if not intersects:
                for cidx, c in enumerate(cleaner):
                    y_idx = y - 4 + cidx

                    if y_idx < 0:
                        continue

                    if y_idx >= len(map_data['map']):
                        continue

                    map_data['cleaned_map'][y-4+cidx][x-4:x+5] = c & ~map_data['map'][y-4+cidx][x-4:x+5]

                    for bidx, b in enumerate(c):
                        if (x - 4 + bidx) < 0:
                            continue

                        if (x - 4 + bidx) > len(map_data['printable_map'][y]):
                            continue

                        if b & map_data['cleaned_map'][y-4+cidx][x-4+bidx] and map_data['printable_map'][y-4+cidx][x-4+bidx] != 's':
                            map_data['printable_map'][y-4+cidx][x-4+bidx] = '.'

                for ridx, r in enumerate(robot):
                    for bidx, b in enumerate(r):
                        if b:
                            map_data['printable_map'][y-3+ridx][x-3+bidx] = 's'

        print(y)

    count = 0

    for row in map_data['printable_map']:
        count += row.count(' ')

    return count


def print_map(map_data):
    for row in map_data['printable_map']:
        print(''.join(row))


def test_robotizer():
    map_data = map_reader('input/17.test')
    assert place_robot(map_data) == 96


if __name__ == '__main__':
    map_data = map_reader('input/17')
    print(place_robot(map_data))

