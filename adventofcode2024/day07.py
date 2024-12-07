from operator import mul, add
from itertools import product
from functools import reduce


def operator_applicator(path):
    tasks = open(path).read().splitlines()
    ops = (mul, add)
    valid_sum = 0

    def apply(cur, op_n):
        return op_n[0](op_n[1], cur)

    for task in tasks:
        answer, args = task.split(': ')
        answer = int(answer)
        values = list(map(int, args.split()))
        valid = False

        for opseq in product(ops, repeat=len(values) - 1):
            res = reduce(apply, zip(opseq, values[1:]), values[0])

            if res == answer:
                valid = True
                break

        if valid:
            valid_sum += answer

    return valid_sum


def test_operator_applicator():
    assert operator_applicator('input/07.test') == 3749


if __name__ == '__main__':
    print(operator_applicator('input/07'))