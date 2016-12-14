xs, ys = 50, 6
display = []

for y in range(0, ys):
    display.append(['.'] * xs)


def print_display():
    for row in display:
        print(''.join(row))

    print("")


def pixelcount():
    cnt = 0

    for row in display:
        for c in row:
            if c == '#':
                cnt += 1

    return cnt


def rect(w, h):
    for y in range(0, int(h)):
        for x in range(0, int(w)):
            display[y][x] = '#'


def rotate_row(row, steps):
    for _ in range(0, steps):
        display[row].insert(0, display[row].pop())


def rotate_column(col, steps):
    for _ in range(0, steps):
        t = display[-1][col]

        for y in range(len(display) - 1, 0, -1):
            display[y][col] = display[y-1][col]

        display[0][col] = t

for line in open("input/dec08").readlines():
    instr = line.split(" ")

    if instr[0] == 'rect':
        w, h = instr[1].split('x')
        rect(w, h)
    elif instr[0] == 'rotate':
        if instr[1] == 'column':
            rotate_column(int(instr[2][2:]), int(instr[4]))
        elif instr[1] == 'row':
            rotate_row(int(instr[2][2:]), int(instr[4]))
        else:
            print("invalid rotate spec: " + instr[1])
    else:
        print("invalid instruction: " + instr[0])

    print_display()

print(pixelcount())