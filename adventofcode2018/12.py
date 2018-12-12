def landscaper(f, generations):
    header = f.readline()
    f.readline()

    for rule in f.readlines():
        print(rule)


def test_landscaper():
    assert landscaper(open('input/12.test'), 20) == 325


if __name__ == '__main__':
    test_landscaper()