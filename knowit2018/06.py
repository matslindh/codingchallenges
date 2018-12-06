def is_zero_heavy(n):
    s = str(n)
    le = len(s)

    return s.count('0') > le / 2.0


def test_is_zero_heavy():
    assert is_zero_heavy(1050006) is True
    assert is_zero_heavy(105006) is False
    assert is_zero_heavy(1) is False


if __name__ == '__main__':
    c = 0

    # for x in range(1, 101):
    for x in range(1, 18163107):
        if is_zero_heavy(x):
            c += x

    print(c)
