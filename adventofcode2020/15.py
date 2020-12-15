def sayer_counter(sequence, limit):
    last_spoken = {}

    for idx, s in enumerate(sequence):
        last_spoken[s] = idx

    spoken_state = None

    for i in range(len(sequence), limit):
        if spoken_state is not None:
            current = i - spoken_state - 1
        else:
            current = 0

        spoken_state = last_spoken.get(current)
        last_spoken[current] = i

    return current


def test_sayer_counter():
    assert sayer_counter([0, 3, 6], 2020) == 436
    assert sayer_counter([1, 3, 2], 2020) == 1
    assert sayer_counter([2, 1, 3], 2020) == 10
    assert sayer_counter([1, 2, 3], 2020) == 27


if __name__ == '__main__':
    print(sayer_counter([8, 0, 17, 4, 1, 12], 2020))
    print(sayer_counter([8, 0, 17, 4, 1, 12], 30000000))
