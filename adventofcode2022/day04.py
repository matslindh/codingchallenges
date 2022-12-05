def int_it(s):
    integers = tuple(map(int, s.split('-')))
    return {
        'start': integers[0],
        'end': integers[1],
    }


def overlap_count(path):
    lines = open(path).read().splitlines()
    contained = 0
    overlaps = 0

    for line in lines:
        interval_1_s, interval_2_s = line.split(',')
        interval_1 = int_it(interval_1_s)
        interval_2 = int_it(interval_2_s)

        if interval_1['start'] <= interval_2['start'] and interval_1['end'] >= interval_2['end']:
            contained += 1
        elif interval_2['start'] <= interval_1['start'] and interval_2['end'] >= interval_1['end']:
            contained += 1

        if interval_1['end'] >= interval_2['start'] and interval_1['start'] <= interval_2['end']:
            overlaps += 1

    return contained, overlaps


def test_overlap_count():
    assert overlap_count('input/04.test') == (2, 4)


if __name__ == '__main__':
    print(overlap_count('input/04'))
