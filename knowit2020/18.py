from math import ceil

words = [x.strip() for x in open('input/18.wordlist', encoding='utf-8')]


def is_palmostidrome(w):
    # palindromes are not
    rev = w[::-1]

    if w == rev:
        return False

    if len(w) == 2:
        return False




def get_parts(w):
    e = (len(w) // 2 - 1) if len(w) % 2 == 0 else len(w) // 2
    b = e + 2 - (len(w) % 2)

    return w[:e], w[b:], w[e:b]


def test_get_parts():
    assert get_parts('kauka') == ('ka', 'ka', 'u')
    assert get_parts('baluba') == ('ba', 'ba', 'lu')
    assert get_parts('tarotkorta') == ('taro', 'orta', 'tk')


def test_is_palmostidrome():
    assert not is_palmostidrome('regninger')
    assert not is_palmostidrome('ab')
    assert is_palmostidrome('kauka')
    assert is_palmostidrome('tarotkorta')
    assert is_palmostidrome('baluba')
    assert is_palmostidrome('ebcce')
    assert not is_palmostidrome('skolebolle')


if __name__ == '__main__':
    c = 0

    for w in words:
        if is_palmostidrome(w):
            c += 1
            print(w, c)

    print(c)