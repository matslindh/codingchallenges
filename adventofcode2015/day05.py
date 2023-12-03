from collections import Counter


def is_nice(s):
    c = Counter(s)
    vowels = ('a', 'e', 'i', 'o', 'u')
    naughty = ('ab', 'cd', 'pq', 'xy')

    vowel_count = sum(c.get(vowel, 0) for vowel in vowels)

    if vowel_count < 3:
        return False

    for n in naughty:
        if n in s:
            return False

    for idx, current in enumerate(s[:-1]):
        if s[idx + 1] == current:
            return True

    return False


def test_is_nice():
    assert is_nice("ugknbfddgicrmopn")
    assert is_nice("aaa")
    assert not is_nice("jchzalrnumimnmhp")
    assert not is_nice("haegwjzuvuyypxyu")
    assert not is_nice("dvszwmarrgswjxmb")


def is_nice_two(s):
    has_twice = False

    for x in range(0, len(s) - 3, 1):
        if s[x:x+2] in s[x+2:]:
            has_twice = True
            break

    if not has_twice:
        return False

    for x in range(0, len(s) - 2, 1):
        if s[x] == s[x+2]:
            return True

    return False



def test_is_nice_two():
    assert is_nice_two("qjhvhtzxzqqjkmpb")
    assert is_nice_two("xxyxx")
    assert not is_nice_two("uurcxstgmygtbstg")
    assert not is_nice_two("ieodomkazucvgmuy")


if __name__ == '__main__':
    count = 0

    for line in open("input/05").read().splitlines():
        count += is_nice(line)

    print(count)

    count = 0

    for line in open("input/05").read().splitlines():
        count += is_nice_two(line)

    print(count)