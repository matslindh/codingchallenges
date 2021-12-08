def decode_line(line):
    wires, display_numbers = line.split('|')
    digits = display_numbers.strip().split(' ')
    wires = wires.strip().split(' ')

    return wires, digits


def count_unique_digits(display_lines):
    unique = 0

    for line in display_lines:
        _, digits = decode_line(line)

        for digit in digits:
            unique += len(digit) in (2, 3, 4, 7)

    return unique


def decode_display_value(wires, digits):
    possible = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set(),
        9: set(),
    }

    resolved = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    }

    for code in wires:
        length = len(code)

        if length == 2:
            possible[1].add(code)
            resolved[1] = code
        elif length == 3:
            possible[7].add(code)
            resolved[7] = code
        elif length == 4:
            possible[4].add(code)
            resolved[4] = code
        elif length == 5:
            possible[2].add(code)
            possible[3].add(code)
            possible[5].add(code)
        elif length == 6:
            possible[0].add(code)
            possible[6].add(code)
            possible[9].add(code)
        elif length == 7:
            possible[8].add(code)
            resolved[8] = code

    for option in possible[3]:
        if set(resolved[1]).issubset(set(option)):
            resolved[3] = option
            possible[2].remove(option)
            possible[5].remove(option)
            break

    for option in possible[5]:
        if len(set(resolved[4]).intersection(set(option))) == 3:
            resolved[5] = option
            possible[2].remove(option)
            resolved[2] = possible[2].pop()

    for option in possible[9]:
        if set(resolved[4]).issubset(set(option)):
            resolved[9] = option
            possible[0].remove(option)
            possible[6].remove(option)

    for option in possible[0]:
        if set(resolved[1]).issubset(set(option)):
            resolved[0] = option
            possible[6].remove(option)
            resolved[6] = possible[6].pop()

    output = ''

    for digit in digits:
        for resolved_digit, key in resolved.items():
            if set(digit) == set(key):
                output += str(resolved_digit)
                break

    return output


def sum_up_input_values(display_lines):
    s = 0

    for line in display_lines:
        wires, digits = decode_line(line)

        s += int(decode_display_value(wires, digits))

    return s


def test_count_unique_digits():
    assert count_unique_digits(open('input/08.test').read().splitlines()) == 26


def test_decode_display_value():
    assert decode_display_value('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb'.split(' '),
                                'fdgacbe cefdb cefbgd gcbe'.split(' ')) == '8394'


def test_sum_up_input_values():
    assert sum_up_input_values(open('input/08.test').read().splitlines()) == 61229


if __name__ == '__main__':
    print(count_unique_digits(open('input/08').read().splitlines()))
    print(sum_up_input_values(open('input/08').read().splitlines()))
