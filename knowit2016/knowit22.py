import json
data = json.load(open('input/knowit22'))
from sys import stdout


def valid(t):
    ma = None
    mi = None
    seen_any_rect = False

    for row in t:
        ma_l = None
        mi_l = None
        seen_rect = False
        in_rect = False
        x = 0

        for c in row:
            if c:
                if seen_rect and not in_rect:
                    return False

                seen_rect = True
                seen_any_rect = True
                in_rect = True

                ma_l = x

                if mi_l is None:
                    mi_l = x
            else:
                in_rect = False

            x += 1

        if ma_l is not None:
            if ma is None:
                ma = ma_l
            elif ma_l != ma:
                return False

        if mi_l is not None:
            if mi is None:
                mi = mi_l
            elif mi_l != mi:
                return False

    if ma is None or mi is None:
        return False

    if not seen_any_rect:
        return False

    return True


def print_table(t):
    for row in t:
        for c in row:
            stdout.write(str(c) if c else '.')

        stdout.write("\n")

    stdout.write("\n")


results = []

for task in data:
    table = []

    for i in range(0, 7):
        row = []

        for j in range(0, 10):
            row.append(False)

        table.append(row)

    overlap = False
    iidx = 1

    for instr in task:
        x1, y1, x2, y2 = instr

        for y in range(y1, y2):
            for x in range(x1, x2):
                if table[7-y-1][x+1]:
                    overlap = True

                table[7-y-1][x+1] = hex(iidx)[2:]

        iidx += 1

    print_table(table)
    _valid = valid(table)
    print(_valid)
    results.append(_valid)

print(', '.join(['true' if r else 'false' for r in results]))
