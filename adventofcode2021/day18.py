from math import ceil, floor
from functools import reduce
from itertools import permutations


def is_tuple(n):
    return isinstance(n, tuple)


def magnitude_calculatur(number):
    left, right = number

    if is_tuple(left):
        left = magnitude_calculatur(left)

    if is_tuple(right):
        right = magnitude_calculatur(right)

    return 3 * left + 2 * right


def add_numbers(n1, n2):
    return n1, n2


def explode_number(n):
    state = {
        'left': None,
        'right': None,
        'value_index': -1,
        'can_explode': True,
    }

    def do_explode(number, depth=0):
        left, right = number

        if is_tuple(left):
            if depth > 2 and state['can_explode']:
                state['left'] = (state['value_index'], left[0])
                state['right'] = (state['value_index'] + 2, left[1])
                state['can_explode'] = False
                left = 0
            else:
                left = do_explode(left, depth=depth+1)
        else:
            state['value_index'] += 1

        if is_tuple(right):
            if depth > 2 and state['can_explode']:
                state['left'] = (state['value_index'], right[0])
                state['right'] = (state['value_index'] + 2, right[1])
                state['can_explode'] = False
                right = 0
            else:
                right = do_explode(right, depth=depth+1)
        else:
            state['value_index'] += 1

        return left, right

    def modify_value_index(number):
        left, right = number

        if is_tuple(left):
            left = modify_value_index(left)
        else:
            state['value_index'] += 1

            if state['value_index'] == state['left'][0]:
                left += state['left'][1]

            if state['value_index'] == state['right'][0]:
                left += state['right'][1]

        if is_tuple(right):
            right = modify_value_index(right)
        else:
            state['value_index'] += 1

            if state['value_index'] == state['right'][0]:
                right += state['right'][1]

            if state['value_index'] == state['left'][0]:
                right += state['left'][1]

        return left, right

    explode_result = do_explode(n)
    state['value_index'] = -1

    if state['left'] is not None:
        return modify_value_index(explode_result)

    return explode_result


def split_number(n):
    def do_split(number):
        left, right = number
        can_split = True

        if is_tuple(left):
            left, can_split = do_split(left)
        elif left >= 10:
            left = (floor(left / 2), ceil(left / 2))
            can_split = False

        if can_split:
            if is_tuple(right):
                right, can_split = do_split(right)
            elif right >= 10:
                right = (floor(right / 2), ceil(right / 2))
                can_split = False

        return (left, right), can_split

    return do_split(n)[0]


def reduce_number(n):
    while True:
        old_n = n

        n = explode_number(n)

        if n != old_n:
            continue

        n = split_number(n)

        if n == old_n:
            break

    return n


def summer_homework_i_wanna_go_to_camp_instead(lines):
    result = reduce(evaluate, lines)
    return magnitude_calculatur(result)


def evaluate(a, b):
    res = add_numbers(a, b)
    reduced = reduce_number(res)
    return reduced


def best_two(lines):
    return max(
        magnitude_calculatur(evaluate(a, b)) for a, b in permutations(lines, r=2)
    )


def test_summer_homework_i_wanna_go_to_camp_instead():
    assert summer_homework_i_wanna_go_to_camp_instead(testdata_small()) == 3488
    assert summer_homework_i_wanna_go_to_camp_instead(testdata()) == 4140


def test_best_two():
    assert best_two(testdata()) == 3993


def test_split_number():
    assert split_number((15, 1)) == ((7, 8), 1)
    assert split_number(((((0, 7), 4), (15, (0, 13))), (1, 1))) == ((((0, 7), 4), ((7, 8), (0, 13))), (1, 1))


def test_explode_number():
    assert explode_number((((((9, 8), 1), 2), 3), 4)) == ((((0, 9), 2), 3), 4)
    assert explode_number((7, (6, (5, (4, (3, 2)))))) == (7, (6, (5, (7, 0))))
    assert explode_number(((6, (5, (4, (3, 2)))), 1)) == ((6, (5, (7, 0))), 3)
    assert explode_number(((3, (2, (1, (7, 3)))), (6, (5, (4, (3, 2)))))) == ((3, (2, (8, 0))), (9, (5, (4, (3, 2)))))
    assert explode_number(((3, (2, (8, 0))), (9, (5, (4, (3, 2)))))) == ((3, (2, (8, 0))), (9, (5, (7, 0))))
    assert explode_number(((4, (5, 4)), ((((5, 3), 1), 2), 4))) == ((4, (5, 9)), (((0, 4), 2), 4))


def test_add_numbers():
    assert add_numbers((1, 2), ((3, 4), 5)) == ((1, 2), ((3, 4), 5))


def test_magnitude_calculatur():
    assert magnitude_calculatur(((1, 2), ((3, 4), 5))) == 143
    assert magnitude_calculatur(((((0, 7), 4), ((7, 8), (6, 0))), (8, 1))) == 1384
    assert magnitude_calculatur(((((1, 1), (2, 2)), (3, 3)), (4, 4))) == 445
    assert magnitude_calculatur(((((3, 0), (5, 3)), (4, 4)), (5, 5))) == 791
    assert magnitude_calculatur(((((5, 0), (7, 4)), (5, 5)), (6, 6))) == 1137
    assert magnitude_calculatur(((((8, 7), (7, 7)), ((8, 6), (7, 7))), (((0, 7), (6, 6)), (8, 7)))) == 3488
    assert magnitude_calculatur(((((6, 6), (7, 6)), ((7, 7), (7, 0))), (((7, 7), (7, 7)), ((7, 8), (9, 9))))) == 4140


def testdata_reduce():
    return (
        ((((4, 3), 4), 4), (7, ((8, 4), 9))),
        (1, 1)
    )


def testdata_small():
    return (
        (((0, (4, 5)), (0, 0)), (((4, 5), (2, 6)), (9, 5))),
        (7, (((3, 7), (4, 3)), ((6, 3), (8, 8)))),
        ((2, ((0, 8), (3, 4))), (((6, 7), 1), (7, (1, 6)))),
        ((((2, 4), 7), (6, (0, 5))), (((6, 8), (2, 8)), ((2, 1), (4, 5)))),
        (7, (5, ((3, 8), (1, 4)))),
        ((2, (2, 2)), (8, (8, 1))),
        (2, 9),
        (1, (((9, 3), 9), ((9, 0), (0, 7)))),
        (((5, (7, 4)), 7), 1),
        ((((4, 2), 2), 6), (8, 7)),
    )


def testdata_micro():
    return (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )


def testdata():
    return (
        (((0, (5, 8)), ((1, 7), (9, 6))), ((4, (1, 2)), ((1, 4), 2))),
        (((5, (2, 8)), 4), (5, ((9, 9), 0))),
        (6, (((6, 2), (5, 6)), ((7, 6), (4, 7)))),
        (((6, (0, 7)), (0, 9)), (4, (9, (9, 0)))),
        (((7, (6, 4)), (3, (1, 3))), (((5, 5), 1), 9)),
        ((6, ((7, 3), (3, 2))), (((3, 8), (5, 7)), 4)),
        ((((5, 4), (7, 7)), 8), ((8, 3), 8)),
        ((9, 3), ((9, 9), (6, (4, 9)))),
        ((2, ((7, 7), 7)), ((5, 8), ((9, 3), (0, 2)))),
        ((((5, 2), 5), (8, (3, 7))), ((5, (7, 5)), (4, 4))),
    )


def proddata():
    return (
        ((((4, 9), (1, 7)), (9, 8)), ((7, 9), (7, 9))),
        (((1, (1, 5)), 9), (((8, 0), (8, 8)), ((7, 2), (4, 6)))),
        ((3, 7), ((7, (4, 6)), ((8, 0), (7, 8)))),
        ((((0, 1), 2), 4), ((9, (2, 8)), 7)),
        ((((9, 0), 9), 7), ((1, 0), 8)),
        ((4, ((1, 2), 1)), 1),
        ((((6, 1), (0, 2)), ((2, 3), 4)), ((9, 1), 8)),
        (((5, 9), (1, 0)), ((7, 0), 3)),
        ((9, 1), ((4, 7), (5, (8, 6)))),
        ((5, ((3, 2), (1, 9))), (((3, 8), 9), 3)),
        ((0, ((5, 6), 2)), 9),
        (6, (2, ((4, 2), 6))),
        ((((8, 2), (9, 1)), (9, 1)), 7),
        (9, 1),
        ((((9, 8), (5, 3)), 5), ((6, 9), (9, (6, 8)))),
        (0, ((2, (2, 5)), 2)),
        ((2, 6), (((2, 8), 1), ((0, 2), (0, 7)))),
        ((((7, 8), (8, 5)), ((3, 2), (4, 0))), (2, ((1, 0), (2, 6)))),
        (((7, (7, 0)), ((1, 9), 9)), 7),
        ((((5, 1), (0, 9)), 4), ((0, (9, 7)), (8, (6, 8)))),
        ((8, 2), (2, (6, 0))),
        ((2, 6), (((4, 0), 6), 2)),
        ((9, (7, (0, 1))), 8),
        ((((3, 8), (4, 3)), (7, (0, 6))), (((5, 5), (0, 4)), ((8, 2), 0))),
        ((((9, 1), (9, 3)), (1, (0, 1))), (((9, 6), 8), (9, 6))),
        ((((2, 3), (7, 1)), ((6, 8), 6)), (((6, 0), 0), 0)),
        ((7, ((5, 0), 4)), (((8, 8), (6, 2)), (8, 2))),
        (((0, (3, 8)), ((0, 0), (6, 1))), ((4, 5), ((3, 9), (5, 8)))),
        (4, ((1, (9, 6)), (8, 2))),
        ((9, ((9, 2), 3)), (((5, 6), 2), (1, (0, 9)))),
        ((9, 9), ((0, (9, 6)), ((8, 6), 3))),
        ((4, ((8, 3), 2)), (((9, 9), 9), (2, (2, 0)))),
        ((((7, 3), (4, 2)), 7), (4, 6)),
        (((2, 6), ((4, 0), (0, 8))), ((5, 0), (3, 5))),
        ((((9, 3), (0, 3)), ((0, 0), (1, 1))), (3, ((8, 4), (8, 6)))),
        ((((3, 6), 8), 1), ((4, (4, 1)), ((5, 1), (3, 0)))),
        ((((8, 1), (2, 0)), (5, (2, 1))), ((9, (0, 0)), ((7, 2), (1, 0)))),
        (((6, 6), (2, 3)), ((7, 6), ((9, 8), 2))),
        (((0, 9), 3), (((9, 5), 5), ((6, 8), (0, 4)))),
        (((0, 3), 9), (5, (5, (0, 5)))),
        ((0, ((9, 1), 4)), (2, 4)),
        (((9, 7), (0, (7, 8))), (((3, 3), 5), ((0, 9), (1, 5)))),
        ((0, ((8, 0), (5, 2))), (((1, 8), (1, 2)), (3, 8))),
        (5, (0, ((9, 8), 9))),
        ((6, ((9, 2), (3, 5))), (((2, 3), 9), 3)),
        (1, (1, 1)),
        ((6, ((0, 0), 1)), ((7, (4, 9)), 7)),
        ((3, ((3, 5), 3)), (((9, 9), 6), ((5, 0), 8))),
        (1, 5),
        ((0, 4), (8, 7)),
        ((7, ((9, 2), 1)), 5),
        ((((6, 8), (6, 5)), 0), 4),
        (((4, 1), (9, 0)), (((4, 3), 6), (5, 9))),
        ((8, ((1, 9), (5, 4))), (((9, 0), 4), (5, 5))),
        ((0, 9), (((5, 5), (7, 7)), 6)),
        ((8, (8, 5)), (8, (2, 6))),
        ((((8, 4), 4), 0), ((3, (2, 6)), (6, 6))),
        ((5, ((5, 2), 6)), (((2, 3), (5, 0)), ((2, 9), 0))),
        ((((5, 9), 6), ((8, 9), (5, 7))), (0, (8, (2, 5)))),
        ((((9, 0), 7), 1), 2),
        (((9, 3), 6), (((6, 6), (9, 6)), 1)),
        (((2, 0), (0, (4, 6))), (((5, 7), 6), (9, 5))),
        (((3, (4, 3)), 8), (((6, 3), (0, 5)), 2)),
        ((((2, 8), 8), (5, (2, 4))), ((3, 7), (2, 1))),
        ((1, ((2, 7), 4)), 7),
        ((2, (4, (5, 9))), (((7, 0), 6), (4, (9, 1)))),
        (((9, (3, 5)), ((9, 5), (5, 2))), ((2, (4, 3)), ((0, 5), (1, 9)))),
        ((1, (9, 0)), (((0, 9), (9, 3)), 0)),
        ((((7, 8), (3, 6)), 3), (((2, 6), (2, 9)), ((1, 3), (1, 3)))),
        (((7, (1, 4)), (4, 7)), (((0, 7), (0, 6)), 5)),
        (((6, 0), (3, (2, 3))), 6),
        ((0, (3, (1, 3))), ((2, 3), 9)),
        (((8, 6), (0, 2)), (((8, 9), (7, 0)), 9)),
        ((((4, 9), 6), 2), (((8, 9), (1, 5)), (9, 3))),
        (((1, 5), (6, (2, 7))), (7, (1, 7))),
        (5, (3, (9, 1))),
        (((7, 5), (1, 5)), 1),
        (2, (((5, 0), (4, 0)), ((3, 7), 5))),
        (((5, 9), 1), (((3, 9), 4), 6)),
        ((3, ((5, 2), (9, 2))), (4, ((3, 6), (8, 9)))),
        (((5, 4), (8, 8)), 1),
        ((((8, 9), (5, 8)), 0), ((9, 5), (6, (7, 1)))),
        (((4, (8, 8)), ((9, 5), 4)), 3),
        ((6, (6, (4, 3))), ((7, (3, 9)), (4, 8))),
        ((5, ((4, 2), (7, 3))), (((9, 0), (0, 1)), ((5, 8), 0))),
        ((((6, 1), 6), (9, (0, 8))), (9, 9)),
        ((4, 0), (((1, 4), 4), (4, 4))),
        ((7, ((0, 0), (1, 6))), 7),
        ((6, 3), (5, ((2, 7), 5))),
        ((1, (7, 5)), (0, (4, 1))),
        (((3, 7), 3), ((3, (0, 2)), 2)),
        (((0, 8), ((7, 0), (9, 8))), (((0, 3), 4), ((6, 0), 6))),
        ((((4, 6), (1, 7)), ((6, 4), (1, 5))), (3, (9, 9))),
        (((2, (1, 7)), (9, 9)), ((0, (7, 8)), (0, (9, 6)))),
        ((9, 8), (5, (6, (1, 8)))),
        (((7, 2), ((0, 6), (2, 6))), ((9, (0, 4)), (9, (5, 8)))),
        (((8, (6, 8)), ((5, 5), (9, 9))), (((2, 0), 6), (8, 1))),
        ((((0, 8), 4), (3, 4)), ((0, (0, 8)), ((7, 5), 2))),
        (7, (((3, 4), (5, 4)), 8)),
        (((2, 8), (0, 2)), 6),
    )


if __name__ == '__main__':
    print(summer_homework_i_wanna_go_to_camp_instead(proddata()))
    print(best_two(proddata()))


