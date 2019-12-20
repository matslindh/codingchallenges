import math

n = 1000741
prime_table = list(range(0, n + 1))
mm = int(math.sqrt(n))

for x in range(3, mm, 2):
    for y in range(x*2, n, x):
        prime_table[y] = 0


def is_prime(n):
    if n % 2 == 0 or n < 2:
        return False

    return bool(prime_table[n])


def rule_1(step, elves, elf, elf_d):
    if is_prime(step):
        m = min(elves)

        if elves.count(m) == 1:
            elf = elves.index(m)
            return elf, elf_d


def rule_2(step, elves, elf, elf_d):
    if step % 28 == 0:
        elf_d = 1 if elf_d == -1 else -1
        elf += elf_d
        return elf, elf_d


def rule_3(step, elves, elf, elf_d):
    if step % 2 == 0:
        m = max(elves)
        lookup_elf = elf + elf_d

        if elves.count(m) == 1 and elves.index(m) == lookup_elf % 5:
            elf += elf_d * 2
            return elf, elf_d


def rule_4(step, elves, elf, elf_d):
    if step % 7 == 0:
        elf = 4
        return elf, elf_d


def rule_5(step, elves, elf, elf_d):
    elf += elf_d
    return elf, elf_d


def workit(steps):
    elves = [0]*5
    step = 1
    elf = 0
    elf_d = 1
    elves[0] = 1
    rules = [rule_1, rule_2, rule_3, rule_4, rule_5]
    rule_seq = []
    seq = []

    while step < steps:
        step += 1

        for rule_idx, rule in enumerate(rules):
            returned = rule(step, elves, elf, elf_d)

            if returned is None:
                continue

            elf, elf_d = returned
            elf = elf % 5

            seq.append(elf + 1)
            rule_seq.append(rule_idx + 1)

            elves[elf] += 1
            break

    return elves


def test_prime():
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)
    assert not is_prime(9)
    assert not is_prime(15)
    assert not is_prime(21)
    assert not is_prime(22)
    assert not is_prime(24)
    assert not is_prime(26)
    assert not is_prime(28)


def test_rule_1():
    assert (0, 1) == rule_1(3, [0, 1, 1, 1, 1], 4, 1)
    assert rule_1(3, [2, 1, 1, 1, 1], 4, 1) is None


def test_rule_2():
    assert (-1, -1) == rule_2(28, [0, 0, 0, 0, 0], 0, 1)
    assert (1, 1) == rule_2(28, [0, 0, 0, 0, 0], 0, -1)
    assert rule_2(14, [0, 0, 0, 0, 0], 0, -1) is None


def test_rule_3():
    assert (2, 1) == rule_3(2, [0, 1, 0, 0, 0], 0, 1)
    assert rule_3(2, [0, 1, 1, 0, 0], 0, 1) is None


def test_rule_4():
    assert (4, 1) == rule_4(7, [0, 0, 0, 0, 0], 2, 1)
    assert rule_4(8, [0, 0, 0, 0, 0], 2, 1) is None


def test_rule_5():
    assert (3, 1) == rule_5(3, [0, 0, 0, 0, 0], 2, 1)
    assert (1, -1) == rule_5(3, [0, 0, 0, 0, 0], 2, -1)


if __name__ == '__main__':
    worked = workit(1000740)
    print(worked)
    print(max(worked) - min(worked))
    print(sum(worked))
