from collections import deque


def solve(p1, p2):
    p1 = deque(p1)
    p2 = deque(p2)

    while len(p1) and len(p2):
        c1 = p1.popleft()
        c2 = p2.popleft()

        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    s = 0
    best = list(enumerate(p1 or p2))

    for bidx, val in best:
        s += (len(best) - bidx) * val

    return s


#@profile
def solve_v2(p1, p2):
    v2_cache = {}
    print(p1, p2)
    print("+", end='')

    """s = sorted(p1 + p2)

    if s[0] > len(s) or s[1] > len(s):
        if max(p1) > max(p2):
            return True, []

        return False, []"""

    while p1 and p2:
        cache_key = ','.join(str(x) for x in p1) + '|' + ','.join(str(x) for x in p2)
        #cache_key = (tuple(p1), tuple(p2))

        if cache_key in v2_cache:
            print("/", end='')
            return True, []

        v2_cache[cache_key] = True

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if c1 <= len(p1) and c2 <= len(p2):
            p1_winner, stack = solve_v2(p1[0:c1], p2[0:c2])
        else:
            p1_winner = c1 > c2

        if p1_winner:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    print("-", end='')
    if not p1:
        return False, p2
    else:
        return True, p1


def read_and_solve(f, game=solve):
    p1 = []
    p2 = []
    actual = p1

    for line in [x.strip() for x in open(f)][1:]:
        if line.startswith('Player'):
            actual = p2
            continue

        if not line:
            continue

        actual.append(int(line))

    return game(p1, p2)


def result_to_int(l):
    best = list(enumerate(l))
    s = 0

    for bidx, val in best:
        s += (len(best) - bidx) * val

    return s



def test_solve():
    assert read_and_solve('input/22.test') == 306


def test_solve_v2():
    winner, result = read_and_solve('input/22.test', game=solve_v2)
    assert result_to_int(result) == 291


def test_solve_loop_v2():
    winner, result = read_and_solve('input/22-2.test', game=solve_v2)
    assert result_to_int(result) == 0


if __name__ == '__main__':
    print(read_and_solve('input/22'))
    winner, result = read_and_solve('input/22', game=solve_v2)
    print(result)
    print(result_to_int(result))

