valid = {
    'up': set('|7F'),
    'down': set('|LJ'),
    'right': set('-J7'),
    'left': set('-LF'),
}

changes_direction = {'F', '7', 'J', 'L'}


def navigate_map(lines):
    x, y = starting_coordinate(lines)
    start_x, start_y = x, y
    moved = None

    if y > 0 and lines[y-1][x] in valid['up']:
        moved = 'up'
        y -= 1
    elif x > 0 and lines[y][x-1] in valid['left']:
        moved = 'left'
        x -= 1
    elif y < len(lines) and lines[y+1][x] in valid['down']:
        moved = 'down'
        y += 1
    elif x < len(lines[y]) and lines[y][x+1] in valid['right']:
        moved = 'right'
        x += 1

    sequence = {
        (start_x, start_y): moved,
    }

    while (start_x, start_y) != (x, y):
        current = lines[y][x]
        sequence[(x, y)] = moved

        if current == 'F':
            if moved == 'up':
                x += 1
                moved = 'right'
            elif moved == 'left':
                y += 1
                moved = 'down'

        if current == '7':
            if moved == 'up':
                x -= 1
                moved = 'left'
            elif moved == 'right':
                y += 1
                moved = 'down'

        if current == 'L':
            if moved == 'down':
                x += 1
                moved = 'right'
            elif moved == 'left':
                y -= 1
                moved = 'up'

        if current == 'J':
            if moved == 'down':
                x -= 1
                moved = 'left'
            elif moved == 'right':
                y -= 1
                moved = 'up'

        if current == '|':
            if moved == 'up':
                y -= 1
            elif moved == 'down':
                y += 1

        if current == '-':
            if moved == 'left':
                x -= 1
            elif moved == 'right':
                x += 1

    return sequence


def circumference_of_path(lines):
    return len(navigate_map(lines)) // 2


def size_of_contained_area(lines):
    start_x, start_y = starting_coordinate(lines)
    sequence = navigate_map(lines)
    line_starting_character = list(lines[start_y])
    line_starting_character[start_x] = starting_character(lines)
    lines[start_y] = ''.join(line_starting_character)
    contained = 0

    for y in range(len(lines)):
        inside = False
        started_with = None

        for x in range(len(lines[y])):
            current = lines[y][x]

            if (x, y) in sequence:
                if current == '|':
                    inside = not inside
                elif current == 'J' and started_with == 'F':
                    inside = not inside
                elif current == '7' and started_with == 'L':
                    inside = not inside
                elif current == 'J' and started_with == 'L':
                    started_with = None
                elif current == '7' and started_with == 'F':
                    started_with = None
                elif current == 'L':
                    started_with = 'L'
                elif current == 'F':
                    started_with = 'F'
            else:
                contained += inside

    return contained


def starting_coordinate(lines):
    for y, line in enumerate(lines):
        if 'S' in line:
            return line.index('S'), y


def starting_character(lines):
    x, y = starting_coordinate(lines)

    valids = set()

    if y > 0 and lines[y-1][x] in valid['up']:
        valids.add('up')

    if x > 0 and lines[y][x-1] in valid['left']:
        valids.add('left')

    if y < len(lines) and lines[y+1][x] in valid['down']:
        valids.add('down')

    if x < len(lines[y]) and lines[y][x+1] in valid['right']:
        valids.add('right')

    if {'up', 'down'} == valids:
        return '|'

    if {'left', 'right'} == valid:
        return '-'

    if {'up', 'right'} == valids:
        return 'L'

    if {'down', 'right'} == valids:
        return 'F'

    if {'up', 'left'} == valids:
        return 'J'

    if {'down', 'left'} == valids:
        return '7'

    raise Exception('invalid start character?')


def test_size_of_contained_area():
    assert size_of_contained_area(open("input/10.test").read().splitlines()) == 1
    assert size_of_contained_area(open("input/10.test2").read().splitlines()) == 1
    assert size_of_contained_area(open("input/10.test3").read().splitlines()) == 4
    assert size_of_contained_area(open("input/10.test4").read().splitlines()) == 8
    assert size_of_contained_area(open("input/10.test5").read().splitlines()) == 10


def test_circumference_of_path():
    assert circumference_of_path(open("input/10.test").read().splitlines()) == 4
    assert circumference_of_path(open("input/10.test2").read().splitlines()) == 8


def test_starting_coordinate():
    assert starting_coordinate(open("input/10.test").read().splitlines()) == (1, 1)
    assert starting_coordinate(open("input/10.test2").read().splitlines()) == (0, 2)


if __name__ == '__main__':
    print(navigate_map(open("input/10").read().splitlines()))
    print(size_of_contained_area(open("input/10").read().splitlines()))