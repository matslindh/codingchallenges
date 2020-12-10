import copy


def print_field(field):
    for line in field:
        for char in line:
            print('S' if char else 'F', end='')

        print('')


def evaluator(f):
    field = [[y == 'S' for y in line.strip()] for line in open(f).readlines()]

    def becomes_sick(x, y):
        hits = 0

        if x > 0:
            hits += field[y][x-1]

        if x < (len(field[0]) - 1):
            hits += field[y][x+1]

        if y > 0:
            hits += field[y-1][x]

        if y < len(field) - 1:
            hits += field[y+1][x]

        if hits > 1:
            return True

        return False

    iteration = 1

    while True:
        next_field = copy.deepcopy(field)
        changed = False

        for y in range(0, len(next_field)):
            for x in range(0, len(next_field[y])):
                if not field[y][x]:
                    if becomes_sick(x, y):
                        changed = True
                        next_field[y][x] = True

        if not changed:
            return iteration

        iteration += 1
        field = next_field


def test_evaluator():
    assert 6 == evaluator('input/09.test')


if __name__ == '__main__':
    print(evaluator('input/09'))