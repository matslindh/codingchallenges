def most_possible_gifts(packets, elves):
    s = sum(packets)

    for x in packets[::-1]:
        if s % elves == 0:
            return s / elves

        s -= x

    return None


def test_most_possible_gifts():
    assert 13 == most_possible_gifts([int(x) for x in '10,14,14,13,13,13,15,14,11,15,11'.split(',')], 9)


if __name__ == '__main__':
    print(most_possible_gifts([int(x) for x in open('input/06').read().split(',')], 127))