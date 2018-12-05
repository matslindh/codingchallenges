from operator import (
    add,
    sub,
)

import copy

from itertools import product

def concat(a, b):
    return int(str(a) + str(b))


def print_ops(ops, l):
    for idx, op in enumerate(ops):
        print(l[idx], end='')

        if op is add:
            print(' + ', end='')

        if op is sub:
            print(' - ', end='')

        if not op:
            print('', end='')

    print(l[len(l) - 1], end='')
    print("")


def apply_operators_on_list(l):
    magic = 42
    magic_count = 0

    for op_list in product([add, sub, None], repeat=len(l) - 1):
        new_list = copy.copy(l)
        work_idx = 0

        #print("\n\n-----")

        #print_ops(op_list, new_list)

        #print("\nTRANSFORMED")
        end_ops = []

        for op in op_list:
            if not op:
                new_list[work_idx] = concat(new_list[work_idx], new_list[work_idx+1])
                del new_list[work_idx+1]
            else:
                end_ops.append(op)
                work_idx += 1

        #print_ops(end_ops, new_list)
        stack = new_list[0]
        #print("")

        for i in range(0, len(end_ops)):
            #print("in: ", stack, end_ops[i], new_list[i+1])
            stack = end_ops[i](stack, new_list[i+1])
            #print("out: ", stack)

        if stack == magic:
            magic_count += 1

    return magic_count


def test_apply_operators_on_list():
    assert apply_operators_on_list([1, 2, 3, 4, 5, 6, 7]) == 2


if __name__ == '__main__':
    print(apply_operators_on_list([1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]))