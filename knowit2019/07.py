def zee_special_divison_operator(exp_r, x):
    for y_d in range(2, 27644437):
        b = y_d * x
        r = b % 27644437

        if exp_r == r:
            break

    return y_d


def test_special():
    assert 13825167 == zee_special_divison_operator(5897, 2)
    assert 9216778 == zee_special_divison_operator(5897, 3)
    assert 20734802 == zee_special_divison_operator(5897, 4)


if __name__ == '__main__':
    print(zee_special_divison_operator(5897, 7))