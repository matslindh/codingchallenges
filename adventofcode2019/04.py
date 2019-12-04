def validator(n):
    s = str(n)
    has_double = False
    is_incrementing = True

    for i, c in enumerate(s[1:]):
        if s[i-1] == c:
            has_double = True

        if int(s[i-1]) > int(c):
            is_incrementing = False

    return has_double and is_incrementing


def test_validator():
    assert validator('111111')
    assert not validator('223450')
    assert not validator('123789')


if __name__ == '__main__':
    count = 0

    for n in range(158126, 624575):
        if validator(n):
            count += 1

    print(count)