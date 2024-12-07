from operator import mul, add
from itertools import product


def concat(a: int, b: int):
    return int(str(a) + str(b))


def operator_applicator(path, ops):
    tasks = open(path).read().splitlines()
    valid_sum = 0

    def apply(cur, op_n):
        return op_n[0](op_n[1], cur)

    for task in tasks:
        answer, args = task.split(': ')
        answer = int(answer)
        values = list(map(int, args.split()))
        valid = False

        for opseq in product(ops, repeat=len(values) - 1):
            ans = values[0]

            for op, value in zip(opseq, values[1:]):
                ans = op(ans, value)

                if ans > answer:
                    break

            if ans == answer:
                valid = True
                break

        if valid:
            valid_sum += answer

    return valid_sum


def test_operator_applicator():
    assert operator_applicator('input/07.test', ops=(mul, add)) == 3749
    assert operator_applicator('input/07.test', ops=(mul, add, concat)) == 11387


if __name__ == '__main__':
    print(operator_applicator('input/07', ops=(mul, add)))
    print(operator_applicator('input/07', ops=(mul, add, concat)))