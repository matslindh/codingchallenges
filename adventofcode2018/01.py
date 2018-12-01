def freq_parser(f):
    freq = 0
    freq_result = 0
    history = {}
    first_duplicate = None
    first_iteration = True
    lines = [int(l.strip()) for l in f.readlines()]

    while not first_duplicate:
        for n in lines:
            freq += n

            if not first_duplicate and freq in history:
                first_duplicate = freq

            history[freq] = n

        if first_iteration:
            freq_result = freq
            first_iteration = False

    return first_duplicate, freq_result


def test_freqparser():
    assert freq_parser(open('input/01.test')) == 2, 3


if __name__ == '__main__':
    print(freq_parser(open('input/01')))
