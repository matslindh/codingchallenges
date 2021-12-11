def octopus_flasher(inp):
    octopi = [list(map(int, row)) for row in inp]
    s = 0

    for _ in range(100):
        s += evolve(octopi)

    return s


def octopus_synchronized_detection_algorithm(inp):
    octopi = [list(map(int, row)) for row in inp]
    flash_count = 0
    step_count = 0

    while True:
        step_count += 1
        flash_count = evolve(octopi)

        if flash_count == 100:
            return step_count


def evolve(octopi):
    flashed = set()

    def flash(x_v, y_v):
        flashed.add((x_v, y_v))
        octopi[y_v][x_v] = 0
        rows = [y_v]
        columns = [x_v]

        if y_v > 0:
            rows.append(y_v - 1)

        if x_v > 0:
            columns.append(x_v - 1)

        if y_v < (len(octopi) - 1):
            rows.append(y_v + 1)

        if x_v < (len(octopi[0]) - 1):
            columns.append(x_v + 1)

        for row_idx in rows:
            for col_idx in columns:
                if (col_idx, row_idx) in flashed:
                    continue

                octopi[row_idx][col_idx] += 1

                if octopi[row_idx][col_idx] > 9:
                    flash(col_idx, row_idx)

    for y, row in enumerate(octopi):
        for x, value in enumerate(row):
            if (x, y) in flashed:
                continue

            octopi[y][x] += 1

            if octopi[y][x] > 9:
                flash(x, y)

    return len(flashed)


def test_octopus_flasher():
    assert octopus_flasher(open('input/11.test').read().splitlines()) == 1656


def test_octopus_synchronized_detection_algorithm():
    assert octopus_synchronized_detection_algorithm(open('input/11.test').read().splitlines()) == 195


if __name__ == '__main__':
    print(octopus_flasher(open('input/11').read().splitlines()))
    print(octopus_synchronized_detection_algorithm(open('input/11').read().splitlines()))
