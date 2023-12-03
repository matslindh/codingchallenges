import re

from collections import defaultdict
from typing import Dict, List


def numbers_start_end_on_line(y: int, line: str):
    matches = list(re.finditer(r"(\d+)", line))

    return [
        {
            'part_no': int(match.group(1)),
            'line_no': y,
            'start': match.start(),
            'end': match.end(),
        }
        for match in matches
    ]


def sum_numbers_in_chart(chart: List[str]):
    all_numbers = []

    for line_no, line in enumerate(chart):
        all_numbers.extend(numbers_start_end_on_line(line_no, line))

    summed_part_nos = 0
    parts_by_symbol = defaultdict(list)

    for part_number in all_numbers:
        close_to_symbols = has_part_close_to_part_number(part_number, chart)

        if close_to_symbols:
            summed_part_nos += part_number['part_no']

        for symbol in close_to_symbols:
            parts_by_symbol[symbol].append(part_number)

    total_gear_ratio = 0

    for symbol, parts in parts_by_symbol.items():
        if symbol[0] == '*' and len(parts) == 2:
            gear_ratio = parts[0]['part_no'] * parts[1]['part_no']
            total_gear_ratio += gear_ratio

    return summed_part_nos, total_gear_ratio


def has_part_close_to_part_number(part_number: Dict[str, int], chart: List[str]):
    close_to_symbols = []

    for y in range(
            max(0, part_number['line_no'] - 1),
            min(len(chart), part_number['line_no'] + 2),
    ):
        for x in range(
            max(0, part_number['start'] - 1),
            min(len(chart[0]), part_number['end'] + 1)
        ):
            if chart[y][x] == '.':
                continue

            if chart[y][x].isdigit():
                continue

            close_to_symbols.append((chart[y][x], x, y))

    return close_to_symbols


def test_sum_numbers_in_chart():
    assert sum_numbers_in_chart(
        open("input/03.test").read().splitlines()
    ) == (4361, 467835)


def test_has_part_close_to_part_number():
    assert has_part_close_to_part_number(
        {'part_no': 467, 'line_no': 0, 'start': 0, 'end': 3},
        open("input/03.test").read().splitlines(),
    )

    assert not has_part_close_to_part_number(
        {'part_no': 114, 'line_no': 0, 'start': 5, 'end': 8},
        open("input/03.test").read().splitlines(),
    )


def test_numbers_start_end_on_line():
    assert numbers_start_end_on_line(0, "467..114..") == [
        {'part_no': 467, 'line_no': 0, 'start': 0, 'end': 3},
        {'part_no': 114, 'line_no': 0, 'start': 5, 'end': 8},
    ]


if __name__ == '__main__':
    print(sum_numbers_in_chart(open("input/03").read().splitlines()))