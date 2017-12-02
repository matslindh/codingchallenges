def diff(row):
    return max(row) - min(row)


def dividable(row):
    for i in range(0, len(row) - 1):
        for j in range(i + 1, len(row)):
            if row[i] % row[j] == 0:
                return int(row[i] / row[j])

            if row[j] % row[i] == 0:
                return int(row[j] / row[i])

    return 0


def checksum_file(path):
    checksum = 0

    with open(path) as f:
        for line in f:
            line = [int(l) for l in line.split()]

            if line:
                checksum += diff(line)

    return checksum


def checksum_dividable_file(path):
    checksum = 0

    with open(path) as f:
        for line in f:
            line = [int(l) for l in line.split()]

            if line:
                checksum += dividable(line)

    return checksum


def test_diff():
    assert 8 == diff([5, 1, 9, 5])
    assert 4 == diff([7, 5, 3])
    assert 6 == diff([2, 4, 6, 8])


def test_dividable():
    assert 4 == dividable([5, 9, 2, 8])
    assert 3 == dividable([9, 4, 7, 3])
    assert 2 == dividable([3, 8, 6, 5])


def test_checksum():
    assert 18 == checksum_file('input/dec02_test')


def test_dividable_checksum():
    assert 9 == checksum_dividable_file('input/dec02_test_b')


if __name__ == '__main__':
    print('Task 1: ' + str(checksum_file('input/dec02')))
    print('Task 2: ' + str(checksum_dividable_file('input/dec02')))
