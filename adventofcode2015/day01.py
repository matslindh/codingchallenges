instr = open("input/01").read()
count = 0
has_printed = False

for idx, c in enumerate(instr):
    if c == '(':
        count += 1
    if c == ')':
        count -= 1

        if count < 0 and not has_printed:
            has_printed = True
            print(f"idx: {idx+1}")

print(f"total {count}")