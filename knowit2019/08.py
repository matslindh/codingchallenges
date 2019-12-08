def reversersiffer(n):
    nn = int(str(abs(n))[::-1])

    if n < 0:
        nn *= -1

    return nn


def opp7(n):
    while str(n)[-1] != '7':
        n += 1

    return n


def gangemsd(n):
    return n * int(str(abs(n))[0])


def delemsd(n):
    return n // int(str(abs(n))[0])


def pluss1tilpar(n):
    ns = str(abs(n))
    nn = ''

    for i in range(len(ns)):
        if int(ns[i]) % 2 == 0:
            nn += str(int(ns[i]) + 1)
        else:
            nn += ns[i]

    return int(nn) * (-1 if n < 0 else 1)


def trekk1fraodde(n):
    ns = str(abs(n))
    nn = ''

    for i in range(len(ns)):
        if int(ns[i]) % 2 == 1:
            nn += str(int(ns[i]) - 1)
        else:
            nn += ns[i]

    return int(nn) * (-1 if n < 0 else 1)


def wheelspinner(n):
    operations = [[op.strip() for op in line.strip()[8:].split(',')] for line in open('input/08').readlines()]
    pos = [0]*10

    while True:
        idx = n % 10
        op_code = operations[idx][pos[idx]]

        # print(n, idx, op_code)
        func = None

        if op_code.lower() in globals():
            func = globals()[op_code.lower()]

        if func:
            n = func(n)
        elif op_code == 'STOPP':
            return n
        elif op_code == 'PLUSS4':
            n += 4
        elif op_code == 'PLUSS101':
            n += 101
        elif op_code == 'MINUS9':
            n -= 9
        elif op_code == 'MINUS1':
            n -= 1
        elif op_code == 'ROTERPAR':
            for i in range(0, len(pos), 2):
                pos[i] = (pos[i] + 1) % len(operations[i])
        elif op_code == 'ROTERODDE':
            for i in range(1, len(pos), 2):
                pos[i] = (pos[i] + 1) % len(operations[i])
        elif op_code == 'ROTERALLE':
            for i in range(0, len(pos)):
                pos[i] = (pos[i] + 1) % len(operations[i])
        else:
            print("UNKNOWN OPCODE: " + op_code)
            return

        pos[idx] = (pos[idx] + 1) % len(operations[idx])


def test_reversersiffer():
    assert 321 == reversersiffer(123)
    assert -321 == reversersiffer(-123)
    assert 21 == reversersiffer(12)


def test_opp7():
    assert 27 == opp7(21)
    assert -7 == opp7(-13)
    assert 17 == opp7(17)


def test_gangemsd():
    assert 46 == gangemsd(23)
    assert -93 == gangemsd(-31)


def test_delemsd():
    assert 11 == delemsd(23)
    assert -11 == delemsd(-31)


def test_pluss1tilpar():
    assert 131 == pluss1tilpar(120)
    assert -1335 == pluss1tilpar(-1234)


def test_trekk1fraodde():
    assert 224 == trekk1fraodde(1234)
    assert -224 == trekk1fraodde(-1234)


if __name__ == '__main__':
    best = 0

    for coins in range(1, 10):
        result = wheelspinner(coins)

        if result > best:
            best = result
            print('new best: ' + str(result) + ' - ' + str(coins) + ' coins')
