
def generate_table(n):
    table = {}
    h = int(n/2) + 1

    for x in range(1, h + 1):
        s = x

        for y in range(x + 1, h + 1):
            s += y

            if s > n:
                break

            if s not in table:
                table[s] = 0

            table[s] += 1

    return table


def child_gifts(n):
    t = generate_table(n)
    return t[n] if n in t else 0


def test_child_gifts():
    assert child_gifts(8) == 0
    assert child_gifts(9) == 2


if __name__ == "__main__":
    s = 0

    print("Generating table..")

    table = generate_table(130000)

    print("Summing")

    for t in table:
        s += table[t]

    print(s)