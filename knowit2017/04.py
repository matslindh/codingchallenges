from collections import Counter


def can_be_permutated_palindrome(w):
    has_odd = False
    c = Counter(w)

    for k in c:
        if c[k] % 2:
            if has_odd:
                return False

            has_odd = True

    return True


def is_palindrome(w):
    return w == w[::-1]


def count_permutated_palindromes(f):
    count = 0

    for line in open(f).readlines():
        line = line.strip()

        if not is_palindrome(line) and can_be_permutated_palindrome(line):
            count += 1

    return count


def test_is_palindrome():
    assert is_palindrome('regninger') is True
    assert is_palindrome('regningar') is False
    assert is_palindrome('abba') is True


def test_can_be_permutated_palindrome():
    assert can_be_permutated_palindrome('tartar') is True
    assert can_be_permutated_palindrome('tartarba') is False


def test_count_permutated_palindromes():
    assert count_permutated_palindromes('input/dec04_test') == 1


if __name__ == '__main__':
    print(count_permutated_palindromes('input/dec04'))
