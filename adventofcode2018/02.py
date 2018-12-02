from collections import Counter


def checksum(f):
    two_c = 0
    three_c = 0

    for line in f.readlines():
        has_two = False
        has_three = False

        for c, count in Counter(line.strip()).items():
            if count == 2:
                has_two = True
            elif count == 3:
                has_three = True

        two_c += 1 if has_two else 0
        three_c += 1 if has_three else 0

    return two_c * three_c


def find_ids(f):
    ids = [line.strip() for line in f.readlines()]

    for i in range(0, len(ids) - 1):
        for j in range(i, len(ids)):
            diffs = 0
            diff_at = None

            for idx in range(0, len(ids[i])):
                if ids[i][idx] != ids[j][idx]:
                    diffs += 1
                    diff_at = idx

                if diffs > 2:
                    break

            if diffs == 1:
                return ids[i][0:diff_at] + ids[i][diff_at + 1:]


def test_checksum():
    assert checksum(open('input/02.test')) == 12


def test_find_ids():
    assert find_ids(open('input/02b.test')) == 'fgij'


if  __name__ == '__main__':
    print(checksum(open('input/02')))
    print(find_ids(open('input/02')))
