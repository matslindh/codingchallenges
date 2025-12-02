from common import rs
from itertools import batched


def is_id_valid_part2(id_):
    digits = str(id_)
    digits_l = len(digits)

    for s_idx in range(digits_l - 1):
        for length in range(1, (digits_l // 2) + 1):
            if digits_l % length != 0:  # does not divide exactly - we could find divisors of the len, but this is faster to write and less complex
                continue

            if len(set(batched(digits, length))) == 1:  # all slices are identical
                return False

    return True


def is_id_valid_part1(id_):
    digits = str(id_)
    digits_l = len(digits)

    if digits_l % 2 == 1:
        return True

    left = digits[0:digits_l//2]
    right = digits[digits_l//2:]

    return left != right


def sum_invalid_ids(path):
    s_p1 = 0
    s_p2 = 0

    for line in rs(path):
        for interval in line.split(','):
            start, end = map(int, interval.split('-'))

            for id_ in range(start, end + 1):
                if not is_id_valid_part1(id_):
                    s_p1 += id_

                if not is_id_valid_part2(id_):
                    s_p2 += id_

    return s_p1, s_p2


def test_is_id_valid_part1():
    assert is_id_valid_part1(123123) is False
    assert is_id_valid_part1(123124)
    assert is_id_valid_part1(111)


def test_is_id_valid_part2():
    assert is_id_valid_part2(123123) is False
    assert is_id_valid_part2(123124)
    assert is_id_valid_part2(111) is False


def test_sum_invalid_ids():
    assert sum_invalid_ids('input/02.test') == (1227775554, 4174379265)


if __name__ == '__main__':
    print(sum_invalid_ids('input/02'))
