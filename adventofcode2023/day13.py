from utils import rs
from itertools import pairwise, islice


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def find_reflection_indexes(lines):
    possible_reflections = set()

    for (idx_1, line), (idx_2, line2) in pairwise(enumerate(lines)):
        if line == line2:
            possible_reflections.add(idx_1)

    return possible_reflections

def valid_reflection_index(lines):
    return set(filter(lambda x: has_reflection_from_index(lines, x), find_reflection_indexes(lines)))


def has_reflection_from_index(lines, idx):
    for low, high in zip(range(idx, -1, -1), range(idx+1, len(lines))):
        if lines[low] != lines[high]:
            return False

    return True


def score_modified_mirrorfields(lines):
    row_length = len(lines[0])
    source = "".join(lines)

    original_valid_reflection_index_x = valid_reflection_index(lines)
    original_valid_reflection_index_y = valid_reflection_index(list(zip(*lines)))

    for idx in range(len(source)):
        new_source = source[:idx] + ('.' if source[idx] == '#' else '#') + source[idx+1:]
        new_lines = list(batched(new_source, row_length))

        new_valid_reflection_indexes_x = valid_reflection_index(new_lines)
        new_valid_reflection_indexes_y = valid_reflection_index(list(zip(*new_lines)))

        diff_x = new_valid_reflection_indexes_x.difference(original_valid_reflection_index_x)
        diff_y = new_valid_reflection_indexes_y.difference(original_valid_reflection_index_y)

        if diff_x or diff_y:
            if diff_x:
                return (diff_x.pop() + 1) * 100

            return diff_y.pop() + 1

    pass

def score_reflection(lines):
    reflection_idx = valid_reflection_index(lines)

    if reflection_idx:
        return (reflection_idx.pop() + 1) * 100

    lines = list(zip(*lines))

    reflection_idx = valid_reflection_index(lines)

    if reflection_idx:
        return reflection_idx.pop() + 1

    pass

def score_combined(lines):
    batch = []
    score = 0

    for line in lines:
        if not line:
            score += score_reflection(batch)
            batch = []
        else:
            batch.append(line)

    if batch:
        score += score_reflection(batch)

    return score


def score_combined_modified(lines):
    batch = []
    score = 0

    for line in lines:
        if not line:
            score += score_modified_mirrorfields(batch)
            batch = []
        else:
            batch.append(line)

    if batch:
        score += score_modified_mirrorfields(batch)

    return score

def test_score_reflection():
    assert score_reflection(rs("13.test")) == 5
    assert score_reflection(rs("13.test2")) == 400

    assert score_combined(rs("13.test_combined")) == 405


def test_modified_score_reflection():
    assert score_combined_modified(rs("13.test_combined")) == 400


if __name__ == "__main__":
    print(score_combined(rs("13")))
    print(score_combined_modified(rs("13")))