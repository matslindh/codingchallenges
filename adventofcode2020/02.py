from collections import Counter


def is_valid_password(rule, password):
    counter, char = rule.split(' ')
    lower, upper = map(int, counter.split('-'))
    c = Counter(password)

    if char not in c and lower > 0:
        return False

    if c[char] < lower or c[char] > upper:
        return False

    return True


def is_valid_password_now(rule, password):
    counter, char = rule.split(' ')
    idx1, idx2 = map(lambda x: int(x)-1, counter.split('-'))
    return (password[idx1] == char or password[idx2] == char) and password[idx1] != password[idx2]


def test_valid_password():
    assert is_valid_password('1-3 a', 'abcde')
    assert not is_valid_password('1-3 b', 'cdefg')
    assert is_valid_password('2-9 c', 'ccccccccc')


def test_valid_password_oh_no_it_was_from_down_the_street():
    assert is_valid_password_now('1-3 a', 'abcde')
    assert not is_valid_password_now('1-3 b', 'cdefg')
    assert not is_valid_password_now('2-9 c', 'ccccccccc')


if __name__ == '__main__':
    count = 0
    count_now = 0

    for line in open('input/02').readlines():
        rule, password = [n.strip() for n in line.split(':')]
        count += int(is_valid_password(rule, password))
        count_now += int(is_valid_password_now(rule, password))

    print(count, count_now)
