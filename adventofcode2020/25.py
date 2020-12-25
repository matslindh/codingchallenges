
def loop_size_finder(inp, subject_number=7):
    i = 1
    c = 0

    while i != inp:
        i *= subject_number
        i %= 20201227
        c += 1

    return c


def transformer(iterations, subject_number=7):
    i = 1

    for _ in range(0, iterations):
        i *= subject_number
        i %= 20201227

    return i


def test_loop_size_finder():
    assert loop_size_finder(5764801) == 8
    assert loop_size_finder(17807724) == 11

    assert transformer(11, subject_number=5764801) == transformer(8, subject_number=17807724)


if __name__ == '__main__':
    card_loops = loop_size_finder(10212254)
    door_loops = loop_size_finder(12577395)

    print(transformer(card_loops, 12577395))
