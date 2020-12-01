from itertools import combinations
from operator import mul
from functools import reduce


def summer_and_multiplier(rows, c):
    for combo in combinations(rows, c):
        if sum(combo) == 2020:
            return reduce(mul, combo)

    return None


def test_summer_and_multiplier():
    data = (1721, 979, 366, 299, 675, 1456)
    assert summer_and_multiplier(data, 2) == 514579


def test_summer_and_multiplier():
    data = (1721, 979, 366, 299, 675, 1456)
    assert summer_and_multiplier(data, 3) == 241861950


if __name__ == '__main__':
    print(summer_and_multiplier(map(lambda x: int(x.strip()), open("input/01").readlines()), 2))
    print(summer_and_multiplier(map(lambda x: int(x.strip()), open("input/01").readlines()), 3))