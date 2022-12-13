def parse_map(file_path):
    height_map = {
        'start': None,
        'end': None,
        'possible_starts': [],
        'map': []
    }

    for y, line in enumerate(open(file_path).read().splitlines()):
        row = []

        for x, char in enumerate(line):
            if char == 'S':
                height_map['start'] = (x, y)
                char = 'a'
            elif char == 'E':
                height_map['end'] = (x, y)
                char = 'z'

            if char == 'a':
                height_map['possible_starts'].append((x, y))

            row.append(ord(char))

        height_map['map'].append(row)

    return height_map


def is_valid_next(visited, height_map, x, y, x_d, y_d):
    if (x_d, y_d) in visited:
        return False

    return height_map['map'][y_d][x_d] - height_map['map'][y][x] < 2


def shortest_path(file_path):
    height_map = parse_map(file_path)

    initial = explore_map(height_map, height_map['start'][0], height_map['start'][1])

    minimum = min(explore_map(height_map, x, y) for x, y in height_map['possible_starts'])
    return initial, minimum


def explore_map(height_map, x_s, y_s):
    visited = set()
    queue = [(x_s, y_s, 0)]

    while queue:
        x, y, dist = queue.pop(0)

        if (x, y) == height_map['end']:
            return dist

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x > 0:
            if is_valid_next(visited, height_map, x, y, x - 1, y):
                queue.append((x - 1, y, dist+1))

        if x < len(height_map['map'][y]) - 1:
            if is_valid_next(visited, height_map, x, y, x + 1, y):
                queue.append((x + 1, y, dist+1))

        if y > 0:
            if is_valid_next(visited, height_map, x, y, x, y - 1):
                queue.append((x, y - 1, dist+1))

        if y < len(height_map['map']) - 1:
            if is_valid_next(visited, height_map, x, y, x, y + 1):
                queue.append((x, y + 1, dist+1))

    return 99999999


def test_shortest_path():
    assert shortest_path('input/12.test') == (31, 29)


if __name__ == '__main__':
    print(shortest_path('input/12'))
