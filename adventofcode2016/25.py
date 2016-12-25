instr = [x.strip().split(' ') for x in open("input/dec25").readlines()]
skip = {}
modified = {}

#instr[1] = ['add', 'a', '2572']
#skip[2] = skip[3] = skip[4] = skip[5] = skip[6] = skip[7] = skip[8] = skip[9] = True
#instr[6] = ['add', 'a', 'c']  # adds c to d, sets c to 0
#skip[7] = True
#skip[8] = True
#modified[6] = modified[7] = modified[8] = True

#instr[9] = ['mul', 'a', 'd']  # multiplies a with d
#skip[10] = True

#modified[9] = modified[10] = True

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

print_program(instr)

# evaluated a couple of numbers, found that it found the binary representation of a number, found
# first number above 2572 (which instr 1 - 9 adds to the number) that repeats itself (ends with 0 and is 101010 etc.)
# and subtracted 2572
for x in [158]:
    pc = 0
    reg = {'a': x, 'b': 0, 'c': 0, 'd': 0}
    output = ''

    while pc < len(instr):
        if pc in skip:
            pc += 1
            continue

        inst = instr[pc]

        if inst[0] == 'add':
            v = reg[inst[2]] if inst[2] in reg else int(inst[2])
            reg[inst[1]] += v
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
        elif inst[0] == 'out':
            v = reg[inst[1]] if inst[1] in reg else inst[1]
            output += str(v)
            print(output)

            #if len(output) > 1 and output != '01':
            #    break
            #elif len(output) > 1:
            #    print("THIS IS IT", x)

            pc += 1
        else:
            print("INVALID INSTRUCTION", inst)

        if pc == 8:
            print(reg)

        if pc == 28:
            print('loop', reg)

        if pc == 29:
            print(x, bin(x), bin(x+2572), output)
            break

print(reg['a'])