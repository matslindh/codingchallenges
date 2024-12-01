def lists_from_path(path):
    left = []
    right = []

    for row in open(path).read().splitlines():
        if not row.strip():
            continue

        inp = tuple(map(int, row.split('   ')))
        left.append(inp[0])
        right.append(inp[1])

    return left, right


def calculate_distance(path):
    distance = 0
    left, right = lists_from_path(path)

    for pair in zip(sorted(left), sorted(right)):
        distance += abs(pair[1] - pair[0])

    return distance


def similarity_score(path):
    similarity = 0
    left, right = lists_from_path(path)

    for val in left:
        # O(n^2) is good enough for anyone, baby
        similarity += val * right.count(val)

    return similarity


def test_distance():
    assert calculate_distance('input/01.test') == 11


def test_similarity():
    assert similarity_score('input/01.test') == 31


if __name__ == '__main__':
    print(calculate_distance('input/01'))
    print(similarity_score('input/01'))
