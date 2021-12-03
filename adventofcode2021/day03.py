from typing import List
from collections import defaultdict

test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def bit_counter(rows, column):
    counter = defaultdict(lambda: 0)

    for row in rows:
        counter[row[column]] += 1

    return counter


def power_consumption(bits: List):
    gamma = ''
    epsilon = ''

    for column in range(len(bits[0])):
        counter = bit_counter(column=column, rows=bits)

        if counter['1'] > counter['0']:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def get_life_rating(bits: List, want_least=False):
    current_bits = bits

    for column in range(len(bits[0])):
        counter = bit_counter(rows=current_bits, column=column)

        if not want_least:
            most = '1' if counter['1'] >= counter['0'] else '0'
        else:
            most = '0' if counter['1'] >= counter['0'] else '1'

        kept_bits = [row for row in current_bits if row[column] == most]

        if len(kept_bits) == 1:
            return int(kept_bits[0], 2)

        current_bits = kept_bits


def oxygen_rating(bits: List):
    return get_life_rating(bits, want_least=False)


def co2_rating(bits: List):
    return get_life_rating(bits, want_least=True)


def life_support_rating(bits: List):
    return oxygen_rating(bits) * co2_rating(bits)


def test_power_consumption():
    assert power_consumption(test_data.split("\n")) == 198


def test_oxygen_rating():
    assert get_life_rating(test_data.split("\n")) == 23


def test_co2_rating():
    assert get_life_rating(test_data.split("\n"), want_least=True) == 10


def test_life_support_rating():
    assert life_support_rating(test_data.split("\n")) == 230


if __name__ == '__main__':
    print(power_consumption(open('input/03').read().split("\n")))
    print(life_support_rating(open('input/03').read().split("\n")))
