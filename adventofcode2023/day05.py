import bisect
from itertools import pairwise


def intstr_to_list(intstr: str):
    return tuple(
        int(n)
        for n in intstr.split(' ')
    )

def generate_structure(lines):
    _, seeds_part = lines[0].split(': ')
    seeds = intstr_to_list(seeds_part)
    seeds_intervals = []

    for idx in range(0, len(seeds), 2):
        seeds_intervals.append((seeds[idx], seeds[idx] + seeds[idx+1] - 1))

    from_ = None
    mapping = {}

    for line in lines[2:]:
        if not line:
            continue

        if not line[0].isdigit():
            mapping_part, _ = line.split(' ')
            from_, _, next_ = mapping_part.split('-')
            mapping[from_] = {
                'next': next_,
                'mapping': [],
            }
            continue

        dest, source, length = intstr_to_list(line)
        mapping[from_]['mapping'].append((source, dest, length))

    for key in mapping:
        mapping[key]['mapping'] = list(sorted(mapping[key]['mapping']))

    return seeds, seeds_intervals, mapping


def next_index(current, mapping_list):
    lowest = bisect.bisect_right(mapping_list, (current, 99999999999999, 99999999999999))

    if lowest == 0:
        return current

    source_idx, dest_idx, length = mapping_list[lowest - 1]
    covers = source_idx + length

    if current < covers:
        return dest_idx + current - source_idx

    return current


def navigate_mapping(seeds, mapping):
    location_for_seed = {}

    for seed in seeds:
        current = 'seed'
        current_source = seed

        while True:
            current_mapping = mapping[current]
            dest = next_index(current_source, mapping[current]['mapping'])

            if current_mapping['next'] == 'location':
                location_for_seed[seed] = dest
                break

            current = current_mapping['next']
            current_source = dest

    return location_for_seed


def next_ranges(current_range, mapping_list):
    ranges = []
    current_index = current_start = current_range[0]
    current_end = current_range[1]

    lowest = bisect.bisect_right(mapping_list, (current_start, 99999999999999, 99999999999999))

    if lowest == 0:
        start_next = min(mapping_list[lowest][0] - 1, current_end)
        ranges.append((current_start, start_next))
        current_index = start_next + 1

    while True:
        lowest = bisect.bisect_right(mapping_list, (current_index, 99999999999999, 99999999999999))

        if lowest == len(mapping_list):
            source, dest, length = mapping_list[-1]
            source_end = source + length
            diff = dest - source

            if source_end <= current_index:
                ranges.append((current_index, current_end))
            elif source_end > current_end:
                ranges.append((current_index + diff, current_end + diff))
            else:
                ranges.append((current_index + diff, source_end + diff - 1))
                ranges.append((source_end, current_end))

            break

        next_mapping_range = mapping_list[lowest]
        source, dest, length = mapping_list[lowest - 1]
        source_end = source + length - 1
        diff = dest - source

        if source_end < current_index:
            end_at = min(current_end, next_mapping_range[0] - 1)
            ranges.append((current_index, end_at))
            current_index = end_at + 1
        elif source <= current_index < source_end:
            end_at = min(
                source_end,
                current_end,
            )
            ranges.append((current_index + diff, end_at + diff))
            current_index = end_at + 1

        if current_index > current_end:
            break

    return list(sorted(ranges))


def recurse(current, interval, mapping):
    current_mapping = mapping[current]
    next_ = current_mapping['next']
    mapping_list = current_mapping['mapping']
    next_intervals = next_ranges(interval, mapping_list)
    resulting_intervals = []

    if next_ == 'location':
        return next_intervals

    for next_interval in next_intervals:
        resulting_intervals.extend(recurse(next_, next_interval, mapping))

    return resulting_intervals

def navigate_mapping_ranges(seeds_intervals, mapping):
    resulting_intervals = []

    for seed_interval in seeds_intervals:
        intervals = recurse('seed', seed_interval, mapping)
        resulting_intervals.extend(intervals)

    return min(resulting_intervals)

def test_navigate_mapping_ranges():
    seeds, seeds_intervals, mapping = generate_structure(open("input/05.test").read().splitlines())

    assert navigate_mapping_ranges(seeds_intervals, mapping)[0] == 46


def test_seed_intervals():
    _, seeds_intervals, _ = generate_structure(open("input/05.test").read().splitlines())

    assert seeds_intervals == [
        (79, 92),
        (55, 67),
    ]



def test_next_ranges_before_first_range():
    mapping_list = [
        (10, 20, 5),
        (20, 30, 5)
    ]

    assert next_ranges((5, 7), mapping_list) == [
        (5, 7)
    ]


def test_next_ranges_intersects_first_range():
    mapping_list = [
        (10, 20, 5),
        (20, 30, 5)
    ]

    assert next_ranges((5, 13), mapping_list) == [
        (5, 9),
        (20, 23)
    ]


def test_next_ranges_after_last_range_on_boundary():
    mapping_list = [
        (50, 52, 48),  # 50, 97
        (98, 50, 2),   # 98, 99
    ]

    assert next_ranges((100, 100), mapping_list) == [
        (100, 100)
    ]


def test_next_ranges_intersects_first_range_not_second():
    mapping_list = [
        (10, 20, 5),
        (20, 30, 5)
    ]

    assert next_ranges((13, 19), mapping_list) == [
        (15, 19),
        (23, 24),
    ]


def test_next_ranges():
    mapping_list = [
        (50, 52, 48),  # 50, 97
        (98, 50, 2),   # 98, 99
    ]


    assert next_ranges((40, 100), mapping_list) == [
        (40, 49),
        (50, 51),

        (52, 99),
        (100, 100)
    ]


def test_next_ranges_start_within_range():
    mapping_list = [
        (50, 52, 48),  # 50, 97
        (98, 50, 2),   # 98, 99
    ]

    assert next_ranges((55, 100), mapping_list) == [
        (50, 51),
        (57, 99),
        (100, 100)
    ]


def test_next_ranges_after_last_range():
    mapping_list = [
        (50, 52, 48),  # 50, 97
        (98, 50, 2),   # 98, 99
    ]

    assert next_ranges((102, 105), mapping_list) == [
        (102, 105)
    ]

def test_next_ranges_intersects_between_middle_range():
    mapping_list = [
        (10, 20, 5),
        (20, 30, 5)
    ]

    assert next_ranges((15, 19), mapping_list) == [
        (15, 19),
    ]


def test_next_ranges_intersects_last_range_contained():
    mapping_list = [
        (50, 52, 48),  # 50, 97
        (98, 50, 2),   # 98, 99
    ]

    assert next_ranges((99, 99), mapping_list) == [
        (51, 51),
    ]


def test_next_ranges_intersects_last_range():
    mapping_list = [
        (50, 52, 48),  # 50, 97
        (98, 50, 2),   # 98, 99
    ]

    assert next_ranges((99, 105), mapping_list) == [
        (51, 51),
        (100, 105)
    ]


def test_next_ranges_single():
    mapping_list = [
        (50, 52, 48),
        (98, 50, 2),
    ]

    assert next_ranges((10, 20), mapping_list) == [
        (10, 20),
    ]


def test_navigate_mapping():
    seeds, seeds_intervals, mapping = generate_structure(open("input/05.test").read().splitlines())

    assert navigate_mapping(seeds, mapping) == {
        79: 82,
        14: 43,
        55: 86,
        13: 35,
    }

def test_generate_structure():
    seeds, seeds_intervals, mapping = generate_structure(open("input/05.test").read().splitlines())

    assert mapping['seed'] == {
        'next': 'soil',
        'mapping': [
            (50, 52, 48),
            (98, 50, 2),
        ],
    }


def test_next_index():
    mapping_list = [
        (50, 52, 48),
        (98, 50, 2),
    ]

    assert next_index(53, mapping_list) == 55
    assert next_index(79, mapping_list) == 81
    assert next_index(14, mapping_list) == 14


if __name__ == '__main__':
    seeds, seeds_intervals, mapping = generate_structure(open("input/05").read().splitlines())

    print(min(navigate_mapping(seeds, mapping).values()))
    print(min(navigate_mapping_ranges(seeds_intervals, mapping)))
