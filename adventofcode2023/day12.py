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



def can_place(possible_placements, required_placements, idx, groups_left, current=None):
    if not current:
        current = []

    remaining_positions = sum(groups_left) + len(groups_left) - 1
    matching_positions = 0
    new_idx = idx
    placements_len = len(possible_placements)

    while new_idx < placements_len:
        if possible_placements[new_idx] < groups_left[0]:
            new_idx += possible_placements[new_idx] + 1
            continue

        if groups_left[0] < required_placements[new_idx]:
            break

        if len(groups_left) == 1:
            current.append((groups_left[0], new_idx))
            s = debug_current(current)
            current.pop()
            matching_positions += 1
            new_idx += 1
            continue

        next_idx = new_idx + groups_left[0]

        if next_idx >= len(required_placements):
            break

        if required_placements[next_idx] > 0:
            new_idx += 1
            continue

        current.append((groups_left[0], new_idx))

        matching_positions += can_place(possible_placements,
                                        required_placements,
                                        next_idx + 1,
                                        groups_left[1:],
                                        current=current,
                                        )

        current.pop()

        if required_placements[new_idx] == groups_left[0]:
            break

        new_idx += required_placements[new_idx] or 1

    return matching_positions

def arrangements(pattern, groups):
    possible_placements, required_placements = get_possible_placements(pattern)

    return can_place(possible_placements, required_placements, 0, groups_left=groups)


def test_possible_placements():
    assert get_possible_placements("???.###") == ([3, 2, 1, 0, 3, 2, 1], [0, 0, 0, 0, 3, 2, 1])


def test_arrangements():
    assert arrangements("###.###", (1, 1, 3)) == 0
    assert arrangements("???.###", (1, 1, 3)) == 1
    assert arrangements(".??..??...?##.", (1, 1, 3)) == 4
    assert arrangements("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
    assert arrangements("????.#...#...", (4, 1, 1)) == 1
    assert arrangements("????.######..#####.", (1, 6, 5)) == 4
    assert arrangements("?###????????", (3, 2, 1)) == 10


if __name__ == '__main__':
    lines = open("input/12").read().splitlines()
    summed = 0
    for line in lines:
        pattern, group = line.split(' ')

        summed += arrangements(pattern, tuple(int(g) for g in group.split(',')))

    print(summed)