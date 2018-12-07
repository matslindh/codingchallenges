def kind_removesort(f):
    intervals = []
    interval = []
    prev = None

    for line in f.readlines():
        i = int(line.strip())

        if prev is None or i < prev:
            if len(interval) > 1:
                intervals.append(interval)

            interval = [i]
        else:
            interval.append(i)

        prev = i

    if len(interval) > 1:
        intervals.append(interval)

    for x in range(1, len(intervals)):
        pass

    print(intervals)
    print(len(intervals))


def test_kind_removesort():
    assert kind_removesort(open('input/07.test')) == 10


if __name__ == '__main__':
    print(kind_removesort(open('input/07')))
