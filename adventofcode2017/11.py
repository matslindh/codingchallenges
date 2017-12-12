def navigate_grid(instructions):
    x = y = z = 0
    away = 0

    for inst in instructions:
        if inst == 'ne':
            y -= 1
            x += 1
        elif inst == 'se':
            y -= 1
            z += 1
        elif inst == 's':
            x -= 1
            z += 1
        elif inst == 'sw':
            x -= 1
            y += 1
        elif inst == 'nw':
            y += 1
            z -= 1
        elif inst == 'n':
            x += 1
            z -= 1

        if max(abs(x), abs(y), abs(z)) > away:
            away = max(abs(x), abs(y), abs(z))

    return max(abs(x), abs(y), abs(z)), away


def test_navigate_grid():
    assert (3, 3) == navigate_grid('ne,ne,ne'.split(','))
    assert (0, 2) == navigate_grid('ne,ne,sw,sw'.split(','))
    assert (2, 2) == navigate_grid('ne,ne,s,s'.split(','))
    assert (3, 3) == navigate_grid('se,sw,se,sw,sw'.split(','))


if __name__ == "__main__":
    print(navigate_grid(open('input/dec11').read().strip().split(',')))