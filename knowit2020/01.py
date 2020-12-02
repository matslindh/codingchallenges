vals = sorted([int(x) for x in open("input/01").read().split(',')])

for idx, val in enumerate(vals):
    if val != (idx+1):
        print(idx+1)
        break
