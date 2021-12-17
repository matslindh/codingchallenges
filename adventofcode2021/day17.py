def mission_control(x, y):
    x_low, x_high = x
    y_low, y_high = y

    highest = []

    for x_init in range(1, 500):
        for y_init in range(-200, 200):
            x_v = x_init
            y_v = y_init
            x_pos, y_pos = 0, 0
            current_best = 0

            while x_pos <= x_high:
                x_pos += x_v
                y_pos += y_v

                y_v -= 1

                if x_v > 0:
                    x_v -= 1

                if x_low <= x_pos <= x_high and y_low <= y_pos <= y_high:
                    highest.append((current_best, x_init, y_init))
                    break

                if y_pos < y_low:
                    break

                if x_pos > x_high:
                    break

                if y_pos > current_best:
                    current_best = y_pos

    return max(highest), len(highest)


def test_mission_control():
    assert mission_control(x=(20, 30), y=(-10, -5)) == ((45, 7, 9), 112)


if __name__ == '__main__':
    print(mission_control(x=(150, 171), y=(-129, -70)))