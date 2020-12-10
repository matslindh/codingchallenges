def differ_calculator_beep_booper(values):
    prev = 0
    diffs = {3: 1}

    for x in sorted(values):
        diff = x - prev

        if diff not in diffs:
            diffs[diff] = 0

        diffs[diff] += 1
        prev = x

    return diffs[1] * diffs[3]


def arrangement_calculator_beep_booper(values):
    values.append(0)
    values = sorted(values)

    possibilities = {
        values[0]: 1,
    }

    for idx, val in enumerate(values):
        d_idx = idx + 1

        while d_idx < len(values) and values[d_idx] <= val + 3:
            dst = values[d_idx]

            if dst not in possibilities:
                possibilities[dst] = 0

            possibilities[dst] += possibilities[val]
            d_idx += 1

    return possibilities[values[-1]]


def test_differ():
    assert differ_calculator_beep_booper([int(x) for x in open('input/10.test').readlines()]) == 35
    assert differ_calculator_beep_booper([int(x) for x in open('input/10-2.test').readlines()]) == 220


def test_arrangement():
    assert 19208 == arrangement_calculator_beep_booper([int(x) for x in open('input/10-2.test').readlines()])
    assert 4 == arrangement_calculator_beep_booper([1, 4, 5, 6, 7])
    assert 8 == arrangement_calculator_beep_booper([int(x) for x in open('input/10.test').readlines()])


if __name__ == '__main__':
    print(differ_calculator_beep_booper([int(x) for x in open('input/10').readlines()]))
    print(arrangement_calculator_beep_booper([int(x) for x in open('input/10').readlines()]))
