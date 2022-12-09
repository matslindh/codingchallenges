def head_or_tails(path: str, knot_count: int) -> int:
    instructions = open(path).read().splitlines()
    tail_positions = set()

    knots = []

    for knot in range(knot_count):
        knots.append([0, 0])

    for instr in instructions:
        d, moves = instr.split(' ')

        for _ in range(int(moves)):
            if d == 'R':
                knots[0][0] += 1
            elif d == 'L':
                knots[0][0] -= 1
            elif d == 'U':
                knots[0][1] -= 1
            elif d == 'D':
                knots[0][1] += 1

            for idx in range(knot_count - 1):
                x_diff = knots[idx][0] - knots[idx + 1][0]
                y_diff = knots[idx][1] - knots[idx + 1][1]

                if abs(x_diff) > 1 and abs(y_diff) > 1:
                    knots[idx + 1][0] += x_diff // 2
                    knots[idx + 1][1] += y_diff // 2
                elif abs(x_diff) > 1:
                    knots[idx + 1][0] += x_diff // 2
                    knots[idx + 1][1] = knots[idx][1]
                elif abs(y_diff) > 1:
                    knots[idx + 1][1] += y_diff // 2
                    knots[idx + 1][0] = knots[idx][0]

            tail_positions.add(tuple(knots[-1]))

            #if instr == 'U 8':
            #    print_knots(knots, min_x=-15, max_x=15, min_y=-16, max_y=5)

    return len(tail_positions)


def print_knots(knots, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            val = '.'

            for idx, knot in enumerate(knots[::-1]):
                if knot[0] == x and knot[1] == y:
                    val = str(len(knots) - idx - 1)

            print(val, end='')

        print("")

    print("")


def test_head_or_tails():
    #assert head_or_tails('input/09.test', 2) == 13
    #assert head_or_tails('input/09.test', 10) == 1
    assert head_or_tails('input/09.test2', 10) == 36


if __name__ == '__main__':
    print(head_or_tails('input/09', 2))
    print(head_or_tails('input/09', 10))
