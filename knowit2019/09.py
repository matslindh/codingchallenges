def is_krampus(n):
    p = str(n**2)
    l_p = len(p)

    for i in range(1, l_p - 1):
        p_1 = int(p[:i])
        p_2 = int(p[i:])
        if p_1 and p_2 and p_1 + p_2 == n:
            return True

    return False


def test_is_krampus():
    assert is_krampus(45)
    assert not is_krampus(100)


if __name__ == '__main__':
    s = 0

    for n in open('input/09').readlines():
        n = int(n.strip())

        if is_krampus(n):
            s += n

    print(s)
