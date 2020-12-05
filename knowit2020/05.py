def area_calculator(instructions):
    area = {}
    x, y = 0, 0

    for instr in instructions:
        if instr == 'H':
            x += 1
        elif instr == 'V':
            x -= 1
        elif instr == 'O':
            y += 1
        elif instr == 'N':
            y -= 1

        if instr in ('O', 'N'):
            y_log = y if instr == 'O' else y + 1

            if y_log not in area:
                area[y_log] = []

            area[y_log].append(x)

    a_s = sorted(area.items())
    area_summed = 0

    for y, line in a_s:
        idxes = sorted(line)

        for i in range(0, len(idxes), 2):
            area_summed += idxes[i+1] - idxes[i]

    return area_summed


def test_area_calculator():
    assert 4 == area_calculator('HHOOVVNN')
    assert 14 == area_calculator('HHHHHHOOOOVVNNNVVOVVNN')


if __name__ == '__main__':
    print(area_calculator(open('input/05').read()))