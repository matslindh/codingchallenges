import math


def count_tris_and_squares(n):
    c = 0

    for i in range(n + 1):
        t = int(i * (i + 1) / 2)

        for v in rollin_rollin_rollin(t):
            sqr = math.sqrt(v)

            # works for small enough numbers
            if int(sqr)**2 == v:
                c += 1
                break

    return c


def rollin_rollin_rollin(n):
    s = list(str(n))

    for i in range(len(s)):
        s.append(s.pop(0))
        yield int(''.join(s))


def test_rollin_rollin_rollin():
    assert [2301, 3012, 123, 1230 ] == list(rollin_rollin_rollin(1230))


def test_count_tris_and_squares():
    assert 3 == count_tris_and_squares(5)


if __name__ == '__main__':
    print(count_tris_and_squares(1000000))