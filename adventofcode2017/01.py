for line in open("input/dec01").readlines():
    l = len(line.strip())
    s = 0
    src = 0

    while src < l:
        dst = src + 1 if src < (l - 1) else 0

        if line[src] == line[dst]:
            s += int(line[src])

        src += 1

    print(s)

# b
for line in open("input/dec01").readlines():
    l = len(line.strip())
    s = 0
    src = 0

    while src < l:
        dst = (src + int(l / 2)) % l

        if line[src] == line[dst]:
            s += int(line[src])

        src += 1

    print(s)