from functools import lru_cache


@lru_cache()
def generate_map(serial):
    map = []

    for y in range(0, 300):
        row = []

        for x in range(0, 300):
            row.append(powerlevel(serial, x+1, y+1))

        map.append(tuple(row))

    return tuple(map)


@lru_cache(maxsize=1280000)
def sum_square(serial, x, y, kernel_size):
    map = generate_map(serial)

    if kernel_size == 1:
        return map[y][x]

    s = sum_square(serial, x, y, kernel_size - 1)

    for y_v in range(y, y + kernel_size):
        s += map[y_v][x + kernel_size - 1]

    # -1 since we've already counted this previously
    for x_v in range(x, x + kernel_size - 1):
        s += map[y + kernel_size - 1][x_v]

    return s


def fuel_cell(serial, kernel_size=3):
    max_data = ()
    max_v = None

    for y in range(0, 300 - kernel_size):
        for x in range(0, 300 - kernel_size):
            avg = sum_square(serial, x, y, kernel_size)

            if max_v is None or avg > max_v:
                max_data = (x + 1, y + 1, avg)
                max_v = avg

    return max_data


def fuel_cell_varying_kernel(serial):
    best = None
    best_kernel_size = None

    for size in range(1, 301):
        result = fuel_cell(serial, kernel_size=size)

        if not result:
            continue

        if not best or best[2] < result[2]:
            best = result
            best_kernel_size = size

    return best[0], best[1], best_kernel_size, best[2]


def powerlevel(serial, x, y):
    pl = (x + 10) * y + serial
    pl *= (x + 10)

    if pl < 100:
        pl = 0
    else:
        pl = int(str(pl)[-3])

    pl -= 5

    return pl


def test_powerlevel():
    assert powerlevel(57, 122, 79) == -5
    assert powerlevel(39, 217, 196) == 0
    assert powerlevel(71, 101, 153) == 4


def test_sum_square():
    assert sum_square(18, 0, 0, 3) == -3


def test_fuel_cell():
    assert fuel_cell(18) == (33, 45, 29)
    assert fuel_cell(42) == (21, 61, 30)


def test_fuel_cell_varying_kernel():
    assert fuel_cell_varying_kernel(18) == (90, 269, 16, 113)
    assert fuel_cell_varying_kernel(42) == (232, 251, 12, 119)


if __name__ == '__main__':
    print(fuel_cell_varying_kernel(5034))
    print(fuel_cell(5034))
