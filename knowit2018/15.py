def golden(f):
    c = 0

    for line in f.readlines():
        year = int(line.split('.')[-1])
        bday = 0
        has_squared = False

        while True:
            year += 1
            bday += 1
            squared = bday**2

            if squared > year:
                break

            if squared == year:
                has_squared = True
                break

        if has_squared:
            c += 1

    return c


def test_golden():
    assert golden(open('input/15.test')) == 1


if __name__ == '__main__':
    print(golden(open('input/15')))