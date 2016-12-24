instr = [x.strip().split(' ') for x in open("input/dec23").readlines()]
pc = 0
reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
skip = {}
modified = {}

instr[6] = ['add', 'a', 'c']  # adds c to d, sets c to 0
skip[7] = True
skip[8] = True
modified[6] = modified[7] = modified[8] = True

instr[9] = ['mul', 'a', 'd']  # multiplies a with d
skip[10] = True

modified[9] = modified[10] = True

"""instr[10] = ['add', 'a', 'b']  # adds b to a, sets b to 0
skip[11] = True
skip[12] = True"""

#instr[14] = ['mul', 'a', 'd']  # multiplies a with d
#skip[15] = True


def print_program(inss):
    i = 0

    for inst in inss:
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
        if inst[2] in reg:
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
            if inst[2] in reg:
                pc += reg[inst[2]]
            else:
                pc += int(inst[2])
        else:
            pc += 1
    elif inst[0] == 'tgl':
        if inst[1] in reg:
            d = pc + reg[inst[1]]

            # valid
            if d < len(instr) and d >= 0:
                if d in modified:
                    print("modified instruction tggled")
                if len(instr[d]) == 2:
                    if instr[d][0] == 'inc':
                        instr[d][0] = 'dec'
                    else:
                        instr[d][0] = 'inc'
                elif len(instr[d]) == 3:
                    if instr[d][0] == 'jnz':
                        instr[d][0] = 'cpy'
                    else:
                        instr[d][0] = 'jnz'
        else:
            print(" invalid register", inst[1])

        pc += 1


print(reg['a'])