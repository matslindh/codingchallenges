def navigator(s):
    num = ''
    dirs = ['H', 'V', 'F', 'B']
    x = 0
    y = 0

    for c in s:
        if c not in dirs:
            num += c
            continue

        moves = int(num)
        num = ''

        if c == 'H':
            x += moves
        elif c == 'V':
            x -= moves
        elif c == 'F':
            y += moves
        elif c == 'B':
            y -= moves
        else:
            print("invalid c ", c)

    return x, y


def test_navigator():
    assert navigator('2H2F2H3B') == (4, -1)


if __name__ == '__main__':
    print(navigator(open('input/11').read()))