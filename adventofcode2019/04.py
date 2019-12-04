from collections import Counter


def validator(n):
    s = str(n)
    has_double = False
    is_incrementing = True

    for i, c in enumerate(s[1:]):
        if s[i] == c:
            has_double = True

        if int(s[i]) > int(c):
            is_incrementing = False

    return has_double and is_incrementing


def validator2(n):
    s = str(n)
    has_double = False
    is_incrementing = True
    seq = 0

    for i, c in enumerate(s[1:]):
        if s[i] == c:
            seq += 1
        else:
            if seq == 1:
                has_double = True

            seq = 0

        if int(s[i]) > int(c):
            is_incrementing = False

    if seq == 1:
        has_double = True

    return has_double and is_incrementing


def test_validator():
    assert validator(111111)
    assert not validator(223450)
    assert not validator(123789)
    assert not validator(158585)


def test_validator_2():
    assert validator2(112233)
    assert not validator2(123444)
    assert validator2(111122)


if __name__ == '__main__':
    count = 0

    for n in range(158126, 624575):
        if validator(n):
            count += 1

    print(count)
    count = 0

    for n in range(158126, 624575):
        if validator2(n):
            count += 1

    print(count)
