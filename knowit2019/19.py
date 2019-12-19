def hidden_palindrome(n):
    n_s = str(n)

    if n_s == n_s[::-1]:
        return False

    s = str(n + int(n_s[::-1]))

    return s == s[::-1]


def test_hidden_palindrome():
    assert hidden_palindrome(38)
    assert not hidden_palindrome(49)


if __name__ == '__main__':
    s = 0

    for x in range(1, 123454321+1):
        if x % 1000000 == 0:
            print(x)

        s += x if hidden_palindrome(x) else 0

    print(s)