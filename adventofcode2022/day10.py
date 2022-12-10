def create_x_reg_values(path):
    instructions = open(path).read().splitlines()
    cycle = 0
    current_x = 1
    x_reg_values = [current_x]

    for inst in instructions:
        match inst.split():
            case["noop"]:
                cycle += 1
                x_reg_values.append(current_x)
            case["addx", v]:
                v = int(v)
                cycle += 2
                x_reg_values.append(current_x)
                x_reg_values.append(current_x + v)

        current_x = x_reg_values[-1]

    return x_reg_values


def signal_strength(path):
    x_reg_values = create_x_reg_values(path)
    s = 0

    for idx in range(20, len(x_reg_values), 40):
        s += x_reg_values[idx - 1] * idx

    return s


def draw_display(x_reg_values):
    lines = []
    row = ''

    for x in range(0, 240):
        if x > 0 and x % 40 == 0:
            lines.append(row)
            row = ''

        row += '#' if abs(x_reg_values[x] - x % 40) < 2 else '.'

    lines.append(row)

    return "\n".join(lines)


def test_signal_strength_simple():
    assert signal_strength('input/10.test2') == 0


def test_signal_strength():
    assert signal_strength('input/10.test') == 13140


def test_draw_display():
    x_reg_values = create_x_reg_values('input/10.test')
    assert draw_display(x_reg_values) == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""


if __name__ == '__main__':
    print(signal_strength('input/10'))
    x_reg_values = create_x_reg_values('input/10')
    print(draw_display(x_reg_values))
