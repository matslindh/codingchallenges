memoized = {}


def christmas_number(n):
    in_sequence = {1: True}

    while True:
        if n > 10000000:
            for k in in_sequence:
                memoized[k] = False

            return False

        in_sequence[n] = True

        if n in memoized:
            return memoized[n]

        n = sum([int(d)**2 for d in str(n)])

        if n == 1:
            for k in in_sequence:
                memoized[k] = True

            return True

        if n in in_sequence:
            for k in in_sequence:
                memoized[k] = False

            return False


def test_christmas_number():
    assert christmas_number(13) is True


if __name__ == "__main__":
    s = 0

    for n in range(1, 10000001):
        if n % 100000 == 0:
            print(n)

        if christmas_number(n):
            s += n

    print(s)