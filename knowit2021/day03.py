from collections import defaultdict


def find_largest_balance_neighbourhood(childs):
    counts = defaultdict(list)
    count = 0

    for idx, c in enumerate(childs):
        count += 1 if c == 'J' else -1
        counts[count].append(idx)

    best = 0
    best_idx = 0

    for count, indices in counts.items():
        longest = max(indices) - min(indices)

        if longest > best or (longest == best and min(indices) < best_idx):
            best = longest
            best_idx = min(indices)

    return best, best_idx + 1


def test_largest_neighbourhood():
    assert find_largest_balance_neighbourhood('JJJJJNNJJNNJJJJJ') == (8, 3)


if __name__ == '__main__':
    print(find_largest_balance_neighbourhood(open('input/03').read()))
