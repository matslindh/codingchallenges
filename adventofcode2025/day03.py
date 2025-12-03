from common import lines_with_individual_digits
from functools import lru_cache


def joltage(path):
    s = 0

    for vals in lines_with_individual_digits(path):
        best = [0, 0]

        for idx, d_1 in enumerate(vals[:-1]):
            if d_1 < best[0]:
                continue

            if d_1 > best[0]:
                best[1] = 0

            best[0] = d_1

            for d_2 in vals[idx+1:]:
                if d_2 > best[1]:
                    best[1] = d_2

        s += best[0] * 10 + best[1]

    return s


def joltage_12bits(path):
    file_sum = 0

    @lru_cache  # dynamic programming baby
    def find_best_value(vals, s_idx, left):
        if left > 1:
            my_vals = vals[s_idx:-left+1]
        else:
            my_vals = vals[s_idx:]

        best = max(my_vals)

        if left <= 1:
            return (best, )

        best_nexts = []

        for curr_idx, val in enumerate(my_vals):
            if val != best:
                continue

            best_below = find_best_value(vals, s_idx + curr_idx + 1, left - 1)
            best_nexts.append(best_below)

        return (best, ) + max(best_nexts)

    for vals_line in lines_with_individual_digits(path):
        best_value = find_best_value(vals_line, 0, 12)

        s = sum(
            val * 10**(11 - idx)
            for idx, val in enumerate(best_value)
        )

        file_sum += s

    return file_sum


def test_joltage():
    assert joltage('input/03.test') == 357


def test_joltage_12bits():
    assert joltage_12bits('input/03.test') == 3121910778619


if __name__ == '__main__':
    print(joltage('input/03'))
    print(joltage_12bits('input/03'))
