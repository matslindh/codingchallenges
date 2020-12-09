from cachetools import cached

def addifier(numbers, window=25):
    idx = window

    for number in numbers[idx:]:
        i2 = idx - window
        found = False

        for inner_offset, n1 in enumerate(numbers[i2:idx-1]):
            for n2 in numbers[i2+inner_offset+1:idx]:
                if n1 + n2 == number:
                    found = True

                if found:
                    break

            if found:
                break

        if not found:
            return number

        idx += 1


def sumifier(numbers, goal):
    for sidx in range(0, len(numbers) - 1):
        if numbers[sidx] > goal:
            continue

        for eidx in range(sidx+1, len(numbers)):
            seq = numbers[sidx:eidx+1]
            s = sum(seq)

            if s > goal:
                break

            if s == goal:
                return min(seq) + max(seq)

    return None


def test_addifier():
    assert 127 == addifier([int(x) for x in open('input/09.test').readlines()], window=5)


def test_sumifier():
    assert 62 == sumifier([int(x) for x in open('input/09.test').readlines()], goal=127)


if __name__ == '__main__':
    print(addifier([int(x) for x in open('input/09').readlines()], window=25))
    print(sumifier([int(x) for x in open('input/09').readlines()], goal=1504371145))
