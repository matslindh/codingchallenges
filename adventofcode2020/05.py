def bitlify(s, true_char):
    r = 0
    l = len(s) - 1

    for idx, c in enumerate(s):
        r |= (c == true_char) << (l - idx)

    return r


def seat_indexer(s):
    return bitlify(s[0:7], 'B') * 8 + bitlify(s[7:], 'R')


def test_bitlify():
    assert 44 == bitlify('FBFBBFF', 'B')
    assert 5 == bitlify('RLR', 'R')


def test_seat_indexer():
    assert 357 == seat_indexer('FBFBBFFRLR')
    assert 567 == seat_indexer('BFFFBBFRRR')
    assert 119 == seat_indexer('FFFBBBFRRR')
    assert 820 == seat_indexer('BBFFBBFRLL')


if __name__ == '__main__':
    all_ids = list(map(seat_indexer, [x.strip() for x in open('input/05').readlines()]))
    print(max(all_ids))
    print(set(range(0, 974)).symmetric_difference(set(all_ids)))
