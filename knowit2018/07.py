def kind_reversesort(f):
    intervals = []
    interval = []
    prev = None

    for line in f.readlines():
        i = int(line.strip())

        if prev is None or i < prev:
            if interval:
                intervals.append(interval)

            interval = [i]
        else:
            interval.append(i)

        prev = i

    if interval:
        intervals.append(interval)

    for x in range(1, len(intervals)):
        pass
    
    print(intervals)


def test_kind_removesort():
    assert kind_reversesort(open('input/07.test')) == 10