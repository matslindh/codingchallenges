

def snail_away(steps):
    orig = steps
    y = 0
    x = 0

    while steps > 0:
        y += 1
        steps -= 1
        print('y', x, y, steps, orig - steps)

        while (y % 3 != 0 or y % 5 == 0) and steps > 0:
            y += 1
            steps -= 1
            print('y', x, y, steps, orig - steps)

        if steps <= 0:
            break

        print(" turn east")

        x += 1
        steps -= 1
        print('x', x, y, steps, orig - steps)

        while (x % 5 != 0 or x % 3 == 0) and steps > 0:
            x += 1
            steps -= 1
            print('x', x, y, steps, orig - steps)

        print(" turn north")

    return x, y


def test_snail_away():
    assert snail_away(11) == (5, 6)


print(snail_away(11))
print("this is just the experiment to visualize the period and confirm assumptions.")
print("answer: y = 3 + 15 * c, x = 5 + 30 * c -> 45 in period, take answer / 45 (+1 on answer makes it work, subtract nine (8 in offset at the start + 1 added from x, and you've got it).")
