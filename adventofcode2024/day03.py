import re
from functools import reduce
from operator import add


def multiplier(path):
    inp = open(path).read().strip()

    return reduce(add, [
        int(a) * int(b)
        for a, b in re.findall(r'mul\((\d+),(\d+)\)', inp)
    ])


def multiplier_do_dont(path):
    inp = open(path).read().strip()
    targets = ['do()', 'don\'t()']
    idx = 0
    enabled = True
    res = 0

    while idx < len(inp):
        positions = [
            (inp.find(target, idx), target)
            for target in targets
            if inp.find(target, idx) > -1
        ]

        if not positions:
            next_interval = inp[idx:]
            next_token = None
        else:
            next_token = min(positions)
            next_interval = inp[idx:next_token[0]]

        if enabled:
            for a, b in re.findall(r'mul\((\d+),(\d+)\)', next_interval):
                res += int(a) * int(b)

        if not next_token:
            return res

        if next_token[1] == 'do()':
            enabled = True
        elif next_token[1] == 'don\'t()':
            enabled = False

        idx = next_token[0] + 1

    return res


def test_multiplier():
    assert multiplier("input/03.test") == 161


def test_multiplier_do_dont():
    assert multiplier_do_dont("input/03.test2") == 48


if __name__ == '__main__':
    print(multiplier("input/03"))
    print(multiplier_do_dont("input/03"))