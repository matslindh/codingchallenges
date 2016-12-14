import sys

values = {}


def get_value(x, y):
    if y in values and x in values[y]:
        return values[y][x]

    return x + y


def set_value(x, y, val):
    if y not in values:
        values[y] = {}

    values[y][x] = val


def get_next(x, y):
    current = get_value(x, y)

    possible = [
        (x - 2, y - 1), (x + 2, y - 1), (x - 1, y - 2), (x + 1, y - 2),
        (x - 2, y + 1), (x + 2, y + 1), (x - 1, y + 2), (x - 1, y + 2),
    ]

    best = None

    for x_, y_ in possible:
        val = get_value(x_, y_)
        new = {'x': x_, 'y': y_, 'dist': abs(current - val), 'value': val}

        if best and new['dist'] > best['dist']:
            continue

        if best and new['dist'] == best['dist']:
            if new['x'] > best['x']:
                continue

            if new['x'] == best['x'] and new['y'] > best['y']:
                continue

        best = new

    if current == 1000:
        set_value(x, y, 0)
    else:
        set_value(x, y, 1000)

    return best


def print_values(mi, ma, x_c, y_c, x_n, y_n):
    for y in range(ma, mi, -1):
        v = str(y)
        sys.stdout.write(v + ' ' * (3 - len(v)) + ': ')

        for x in range(mi, ma):
            v = str(get_value(x, y))

            if x == x_c and y == y_c:
                v += ' --'

            if x == x_n and y == y_n:
                v += ' ++'

            sys.stdout.write(v + ' ' * (10 - len(v)))

        sys.stdout.write("\n")

x, y = 0, 0

for _ in range(0, 10):
    next = get_next(x, y)

    print_values(-5, 5, x, y, next['x'], next['y'])
    print(next)
    #print("----------")

    x = next['x']
    y = next['y']

print(abs(x) + abs(y))

print((1000000000000000 * 3) - 3)


