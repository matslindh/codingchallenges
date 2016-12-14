instr = [x.strip().split(' ') for x in open("input/dec12").readlines()]
pc = 0
reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
skip = {}

instr[6] = ['add', 'd', 'c']  # adds c to d, sets c to 0
skip[7] = True
skip[8] = True

instr[10] = ['add', 'a', 'b']  # adds b to a, sets b to 0
skip[11] = True
skip[12] = True

#instr[14] = ['mul', 'a', 'd']  # multiplies a with d
#skip[15] = True

i = 0

for inst in instr:
    prefix = ' # ' if i in skip else '   '

    print(prefix, i, inst)

    i += 1

while pc < len(instr):
    if pc in skip:
        pc += 1
        continue

    inst = instr[pc]

    if inst[0] == 'add':
        reg[inst[1]] += reg[inst[2]]
        reg[inst[2]] = 0
        pc += 1
    elif inst[0] == 'mul':
        reg[inst[1]] *= reg[inst[2]]
        reg[inst[2]] = 0
        pc += 1
    elif inst[0] == 'cpy':
        if inst[1] in reg:
            reg[inst[2]] = reg[inst[1]]
        else:
            reg[inst[2]] = int(inst[1])

        pc += 1
    elif inst[0] == 'inc':
        reg[inst[1]] += 1
        pc += 1
    elif inst[0] == 'dec':
        reg[inst[1]] -= 1
        pc += 1
    elif inst[0] == 'jnz':
        if (inst[1] in reg and reg[inst[1]] != 0) or (inst[1] not in reg and int(inst[1]) != 0):
            pc += int(inst[2])
        else:
            pc += 1

print(reg['a'])