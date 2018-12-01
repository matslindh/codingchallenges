def vekkesort(f):
    current = 0
    s = 0

    for l in f.readlines():
        v = int(l.strip())

        if v >= current:
            s += v
            current = v

    return s


def test_vekkesort():
    assert vekkesort(open('input/01.test')) == 35


if __name__ == '__main__':
    print(vekkesort(open('input/01')))