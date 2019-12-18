from functools import reduce
import math
from collections import Counter

def build_structure(f):
    d = {
        'male': [],
        'female': [],
        'lastname_1': [],
        'lastname_2': [],
    }

    keys = list(d.keys())
    k = keys.pop(0)

    for line in open(f).readlines():
        line = line.strip()

        if line == '---':
            k = keys.pop(0)
            continue

        d[k].append(line)

    return d


def starwarsify(struct, fname, lname, sex):
    k = 'male' if sex == 'M' else 'female'
    first = struct[k][sum([ord(c) for c in fname]) % len(struct[k])]
    half = math.ceil(len(lname) / 2.0)
    p1 = lname[:half]
    p2 = lname[half:]

    last = struct['lastname_1'][sum([ord(c.lower()) - 96 for c in p1]) % len(struct['lastname_1'])]

    factor = reduce(lambda x, y: x * y, [ord(c) for c in p2]) * (len(fname) if sex == 'M' else len(fname) + len(lname))
    last += struct['lastname_2'][int(''.join(sorted(str(factor), reverse=True))) % len(struct['lastname_2'])]

    return first + ' ' + last


def test_starwarsify():
    struct = build_structure('input/names.txt')
    assert 'Poe Lightverse' == starwarsify(struct, 'Jan', 'Johannsen', 'M')


if __name__ == '__main__':
    struct = build_structure('input/names.txt')

    names = []

    for line in open('input/employees.csv'):
        fname, lname, sex = line.strip().split(',')
        names.append(starwarsify(struct, fname, lname, sex))

    print(Counter(names).most_common(10))
