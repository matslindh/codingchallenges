from common import rs
from operator import add, mul
from functools import reduce
from itertools import pairwise

def solve_workbook(path):
    columns = []

    for line in rs(path):
        columns.append(line.split())

    operators = columns[-1]
    callbacks = {
        '+': add,
        '*': mul,
    }

    sums = []

    for col_idx in range(len(columns[0])):
        sums.append(
            reduce(callbacks[operators[col_idx]], (
                int(row[col_idx]) for row in columns[:-1]
            ))
        )

    p1 = sum(sums)

    lines = rs(path)

    start_idxes = [
        idx
        for idx, c in enumerate(lines[-1]) if c != ' '
    ] + [len(lines[0]) + 1]  # append the end so that pairwise works

    sums_p2 = []

    for start, end in pairwise(start_idxes):
        end -= 1
        operator = callbacks[lines[-1][start]]
        numbers = []

        for col in range(start, end):
            digits = ''

            for row in lines[:-1]:
                digits += row[col]

            n = int(digits.strip())
            numbers.append(n)

        sums_p2.append(reduce(operator, numbers))

    p2 = sum(sums_p2)

    return p1, p2

def test_solve_workbook():
    assert solve_workbook('input/06.test') == (4277556, 3263827)


if __name__ == '__main__':
    print(solve_workbook('input/06'))
