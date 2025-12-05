from common import rs
import bisect


def count_fresh_ingredients(path):
    intervals = []
    ingredients = []
    parsing_intervals = True

    for line in rs(path):
        if not line:
            parsing_intervals = False
            continue

        if parsing_intervals:
            start, end = map(int, line.split('-'))
            intervals.append((start, end))
            continue

        ingredients.append(int(line))

    intervals = sorted(intervals)

    start_indexes = tuple(
        (interval[0], idx)
        for idx, interval in enumerate(intervals)
    )

    end_indexes = tuple(sorted(
        (interval[1], idx)
        for idx, interval in enumerate(intervals)
    ))

    fresh_count = 0

    for ingredient in ingredients:
        # build two lists of interval indexes that can fit based on start and end -
        # valid ingredients will be those that find the same indexes on both sides
        possible_intervals_from_start = set(
            interval
            for pos, interval in start_indexes[:bisect.bisect_left(start_indexes, (ingredient, 0))]
        )

        possible_intervals_from_end = set(
            interval
            for pos, interval in end_indexes[bisect.bisect_left(end_indexes, (ingredient, 0)):]
        )

        if possible_intervals_from_start & possible_intervals_from_end:
            fresh_count += 1

    merged_intervals = merge_intervals(intervals)

    merged_sizes = sum(
        end - start + 1
        for start, end in merged_intervals
    )

    return fresh_count, merged_sizes


def merge_intervals(intervals):
    merged = []

    current = list(intervals[0])
    dangling = False

    for interval in intervals[1:]:
        # the start point is within our current interval
        if interval[0] <= current[1]:
            current[1] = max(current[1], interval[1])
            dangling = True
            continue

        merged.append(current)
        current = list(interval)
        dangling = False

    if dangling:
        merged.append(current)

    return merged


def test_count_fresh_ingredients():
    assert count_fresh_ingredients('input/05.test') == (3, 14)


if __name__ == '__main__':
    print(count_fresh_ingredients('input/05'))
