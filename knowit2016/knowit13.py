leds = {}


def turn_on(x, y):
    if y not in leds:
        leds[y] = {}

    leds[y][x] = True


def turn_off(x, y):
    if y not in leds or not x in leds[y]:
        return

    del leds[y][x]


def toggle(x, y):
    if y not in leds or x not in leds[y]:
        turn_on(x, y)
    else:
        turn_off(x, y)


def apply(f, x, y, x2, y2):
    for i_y in range(y, y2+1):
        for i_x in range(x, x2+1):
            f(i_x, i_y)


def apply_dimensions(f, dimensions):
    x, y = dimensions[0].split(',')
    x2, y2 = dimensions[2].split(',')

    apply(f, int(x), int(y), int(x2), int(y2))


def cnt():
    c = 0

    for y in leds:
        c += len(leds[y])

    return c

i_c = 0

for line in open("input/knowit13").readlines():
    instr = line.strip().split()

    if instr[0] == 'toggle':
        apply_dimensions(toggle, instr[1:])
    elif instr[0] == 'turn' and instr[1] == 'on':
        apply_dimensions(turn_on, instr[2:])
    elif instr[0] == 'turn' and instr[1] == 'off':
        apply_dimensions(turn_off, instr[2:])
    else:
        print("Invalid instruction: " + instr[0])

    i_c += 1
    print(i_c)

print(cnt())
