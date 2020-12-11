import copy


def print_seats(seats):
    for line in seats:
        for char in line:
            if char is None:
                print('.', end='')
            elif not char:
                print('L', end='')
            else:
                print('#', end='')

        print()

    print("\n\n")


def seatplanner_flippityflipper(f):
    seats = [[False if char == 'L' else None for char in line.strip()] for line in open(f)]

    def flip_it():
        output = copy.deepcopy(seats)
        flipped = False

        for y, row in enumerate(seats):
            for x, spot in enumerate(row):
                if spot is not None:
                    occ = count_occupied(x, y)

                    if spot and occ >= 4:
                        flipped = True
                        output[y][x] = False
                    elif not spot and occ == 0:
                        flipped = True
                        output[y][x] = True

        return output, flipped

    def count_occupied(x, y):
        occupied = 0

        for y_i in range(max(0, y - 1), min(y + 2, len(seats))):
            for x_i in range(max(0, x - 1), min(x + 2, len(seats[y]))):
                if y_i == y and x_i == x:
                    continue

                occupied += seats[y_i][x_i] is True

        return occupied

    while True:
        seats, flipped = flip_it()

        if not flipped:
            occupied = 0

            for row in seats:
                for spot in row:
                    if spot:
                        occupied += 1

            return occupied


def seatplanner_flippityflipper_raytracer(f):
    seats = [[False if char == 'L' else None for char in line.strip()] for line in open(f)]

    def flip_it():
        output = copy.deepcopy(seats)
        occupied_table = occupied_seen_table(seats)
        flipped = False

        for y in range(0, len(seats)):
            row = []

            for x in range(0, len(seats[y])):
                row.append([])

        for y, row in enumerate(seats):
            for x, spot in enumerate(row):
                if spot is not None:
                    occ = occupied_table[y][x]

                    if spot and len(occ) >= 5:
                        flipped = True
                        output[y][x] = False
                    elif not spot and len(occ) == 0:
                        flipped = True
                        output[y][x] = True

        return output, flipped

    while True:
        seats, flipped = flip_it()

        if not flipped:
            occupied = 0

            for row in seats:
                for spot in row:
                    if spot:
                        occupied += 1

            return occupied


def occupied_seen_table(seats):
    occupied_table = []
    seen_table = []

    for y in range(0, len(seats)):
        row = []
        row_seen = []

        for x in range(0, len(seats[y])):
            row.append([])
            row_seen.append([])

        occupied_table.append(row)
        seen_table.append(row_seen)

    def populate_table(x, y, x_d, y_d):
        occ = False
        seen_from = (0, 0)

        while x >= 0 and y >= 0 and y < len(seats) and x < len(seats[0]):
            if seats[y][x] is not None:
                if occ and (x_d, y_d) not in occupied_table[y][x]:
                    occupied_table[y][x].append((x_d, y_d))

                seen_table[y][x].append((seen_from, occ))
                occ = seats[y][x]
                seen_from = (x, y)

            x += x_d
            y += y_d

    for y in range(0, len(seats)):
        populate_table(0, y, 1, 0)
        populate_table(0, y, 1, 1)
        populate_table(0, y, -1, 1)
        populate_table(0, y, 1, -1)
        populate_table(len(seats[0]) - 1, y, -1, 0)
        populate_table(len(seats[0]) - 1, y, -1, -1)
        populate_table(len(seats[0]) - 1, y, -1, 1)
        populate_table(len(seats[0]) - 1, y, 1, -1)

    for x in range(0, len(seats[0])):
        populate_table(x, 0, 0, 1)
        populate_table(x, 0, 1, 1)
        populate_table(x, 0, -1, 1)
        populate_table(x, 0, 1, -1)
        populate_table(x, len(seats) - 1, 0, -1)
        populate_table(x, len(seats) - 1, -1, -1)
        populate_table(x, len(seats) - 1, 1, -1)
        populate_table(x, len(seats) - 1, -1, 1)

    return occupied_table


def test_seatplanner_flippityflipper():
    assert 37 == seatplanner_flippityflipper('input/11.test')
    assert 26 == seatplanner_flippityflipper_raytracer('input/11.test')



if __name__ == '__main__':
    print(seatplanner_flippityflipper('input/11'))
    print(seatplanner_flippityflipper_raytracer('input/11'))
