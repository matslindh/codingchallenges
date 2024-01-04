import re
from itertools import product


def pattern_matches_groups(pattern, groups):
    return groups == tuple(len(group) for group in re.findall("#+", pattern))


def test_pattern_matches_groups():
    assert pattern_matches_groups("#.#.###", (1, 1, 3))


def get_possible_placements(pattern):
    possible_placements_per_position = [0] * len(pattern)
    required_placements_per_position = [0] * len(pattern)

    idx = len(pattern)
    possible_count = 0
    required_count = 0

    while True:
        idx -= 1

        if idx < 0:
            break

        if pattern[idx] == '?':
            possible_count += 1
            required_count = 0
        elif pattern[idx] == '#':
            possible_count += 1
            required_count += 1
        else:
            required_count = 0
            possible_count = 0

        required_placements_per_position[idx] = required_count
        possible_placements_per_position[idx] = possible_count

    return possible_placements_per_position, required_placements_per_position


def debug_current(current):
    s = ''

    for c, idx in current:
        if len(s) < idx:
            s += '.' * (idx - len(s))

        s += str(c) * c

    return s

def can_place(cache, possible_placements, required_placements, idx, groups_left, current=None):
    cache_key = (idx, groups_left)

    if cache_key in cache:
        return cache[cache_key]

    if not current:
        current = []

    matching_positions = 0
    new_idx = idx
    placements_len = len(possible_placements)

    while new_idx < placements_len:
        if possible_placements[new_idx] < groups_left[0]:
            new_idx += possible_placements[new_idx] + 1
            continue

        if groups_left[0] < required_placements[new_idx]:
            break

        previous_index = 0
        previous_length = 0

        if current:
            previous_length, previous_index = current[-1]

        if any(required_placements[previous_index+previous_length:new_idx]):
            break

        if len(groups_left) == 1:
            is_valid = True
            current.append((groups_left[0], new_idx))
            s = debug_current(current)
            current.pop()

            for offset, future_required_placement in enumerate(required_placements[new_idx:]):
                if future_required_placement == 0:
                    continue

                if groups_left[0] - offset < future_required_placement:
                    is_valid = False
                    break

            new_idx += 1

            if not is_valid:
                continue

            matching_positions += 1
            continue

        next_idx = new_idx + groups_left[0]

        if next_idx >= len(required_placements):
            break

        if required_placements[next_idx] > 0:
            new_idx += 1
            continue

        current.append((groups_left[0], new_idx))

        matching_positions += can_place(cache,
                                        possible_placements,
                                        required_placements,
                                        next_idx + 1,
                                        groups_left[1:],
                                        current=current,
                                        )

        current.pop()

        if required_placements[new_idx] == groups_left[0]:
            break

        new_idx += required_placements[new_idx] or 1

    cache[cache_key] = matching_positions
    return matching_positions

def arrangements(pattern, groups):
    possible_placements, required_placements = get_possible_placements(pattern)

    return can_place({}, possible_placements, required_placements, 0, groups_left=groups)


def triple_arrangements(pattern, groups):
    pattern += '?'
    pattern *= 5
    pattern = pattern[:-1]
    groups *= 5
    possible_placements, required_placements = get_possible_placements(pattern)

    return can_place({}, possible_placements, required_placements, 0, groups_left=groups)


def test_possible_placements():
    assert get_possible_placements("???.###") == ([3, 2, 1, 0, 3, 2, 1], [0, 0, 0, 0, 3, 2, 1])


def test_arrangements():
    assert arrangements("###.###", (1, 1, 3)) == 0
    assert arrangements("???.###", (1, 1, 3)) == 1
    assert arrangements(".??..??...?##.", (1, 1, 3)) == 4
    assert arrangements("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
    assert arrangements("????.#...#...", (4, 1, 1)) == 1
    assert arrangements("????.######..#####.", (1, 6, 5)) == 4
    assert arrangements("?#####???????#..", (5,1,1,1)) == 6
    assert arrangements("#?#???##??#.?#?#?#?", (3,3,1,7)) == 2
    assert arrangements("?###????????", (3, 2, 1)) == 10
    assert arrangements("??.??#.???", (1,1,2)) == 6


def test_triple_arrangements():
    assert triple_arrangements("???.###", (1,1,3)) == 1
    assert triple_arrangements(".??..??...?##.", (1,1,3)) == 16384
    assert triple_arrangements("?#?#?#?#?#?#?#?", (1,3,1,6)) == 1
    assert triple_arrangements("????.#...#...", (4,1,1)) == 16
    assert triple_arrangements("????.######..#####.", (1,6,5)) == 2500
    assert triple_arrangements("?###????????", (3,2,1)) == 506250


if __name__ == '__main__':
    lines = open("input/12").read().splitlines()
    s = 0
    s_triple = 0

    for line_no, line in enumerate(lines):
        pattern, group = line.split(' ')
        groups = tuple(int(g) for g in group.split(','))
        arrangement_count = arrangements(pattern, groups)
        triple_count = triple_arrangements(pattern, groups)

        print(line_no, line, arrangement_count, triple_count)
        s += arrangement_count
        s_triple += triple_count

    print(s)
    print(s_triple)

# 20778962 too low