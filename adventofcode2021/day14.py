from collections import defaultdict
from math import floor, ceil


def polymer_builder(lines, iterations=10):
    polymer = lines[0]
    rules = {}

    for line in lines[2:]:
        source, dest = line.split(' -> ')
        rules[source] = dest

    pairs = {}

    for idx in range(len(polymer) - 1):
        p = ''.join(polymer[idx:idx+2])

        if p not in pairs:
            pairs[p] = 0

        pairs[p] += 1

    for i in range(iterations):
        new_pairs = defaultdict(lambda: 0)

        for pair, count in pairs.items():
            if pair in rules:
                new_pairs[pair[0] + rules[pair]] += count
                new_pairs[rules[pair] + pair[1]] += count
            else:
                new_pairs[pair] = count

        pairs = new_pairs

    counter = defaultdict(lambda: 0)

    for pair, count in pairs.items():
        for char in pair:
            counter[char] += count

    occurs = list(sorted(counter.items(), key=lambda c: c[1], reverse=True))
    return ceil(occurs[0][1]/2.0) - ceil(occurs[-1][1]/2.0)


def test_polymer_builder():
    assert polymer_builder(open('input/14.test').read().splitlines(), iterations=10) == 1588


if __name__ == '__main__':
    print(polymer_builder(open('input/14').read().splitlines()))
    print(polymer_builder(open('input/14').read().splitlines(), iterations=40))
