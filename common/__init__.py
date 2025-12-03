def as_2d_ints(path):
    return [
        list(map(int, row))
        for row in rs(path)
    ]


def as_1d_ints(path):
    return list(map(int, rs(path)[0].split(' ')))


def rs(path):
    return open(path, encoding='utf-8').read().splitlines()


def lines_with_individual_digits(path):
    return tuple(
        map(
            lambda line: tuple(map(int, line)),
            rs(path)
        )
    )