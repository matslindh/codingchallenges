from collections import Counter


def is_valid_passcode(pc):
    c = Counter(pc.split())

    for k in c:
        if c[k] > 1:
            return False

    return True


def is_valid_passcode_and_anagram(pc):
    if not is_valid_passcode(pc):
        return False

    versions = {}

    for w in pc.split():
        c = Counter(w)
        kv = ''

        for k in sorted(c.keys()):
            kv += k + str(c[k])

        if kv in versions:
            return False

        versions[kv] = True

    return True


def count_valid_in_file(f, func=is_valid_passcode):
    lines = open(f).readlines()
    count = 0

    for line in lines:
        count += func(line.strip())

    return count


def test_is_valid_passcode():
    assert is_valid_passcode('aa bb cc dd ee') is True
    assert is_valid_passcode('aa bb cc dd aa') is False
    assert is_valid_passcode('aa bb cc dd aaa') is True


def test_count_valid_in_file():
    assert count_valid_in_file('input/dec04_test') == 2


def test_is_valid_passcode_and_anagram():
    assert is_valid_passcode_and_anagram('abcde fghij') is True
    assert is_valid_passcode_and_anagram('abcde xyz ecdab') is False
    assert is_valid_passcode_and_anagram('a ab abc abd abf abj') is True
    assert is_valid_passcode_and_anagram('iiii oiii ooii oooi oooo') is True
    assert is_valid_passcode_and_anagram('oiii ioii iioi iiio') is False


if __name__ == "__main__":
    print(count_valid_in_file('input/dec04'))
    print(count_valid_in_file('input/dec04', func=is_valid_passcode_and_anagram))
