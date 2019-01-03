def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]


def addi(registers, a, b, c):
    registers[c] = registers[a] + b


def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]


def muli(registers, a, b, c):
    registers[c] = registers[a] * b


def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]


def bani(registers, a, b, c):
    registers[c] = registers[a] & b


def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]


def bori(registers, a, b, c):
    registers[c] = registers[a] | b


def setr(registers, a, b, c):
    registers[c] = registers[a]


def seti(registers, a, b, c):
    registers[c] = a


def gtir(registers, a, b, c):
    registers[c] = int(a > registers[b])


def gtri(registers, a, b, c):
    registers[c] = int(registers[a] > b)


def gtrr(registers, a, b, c):
    registers[c] = int(registers[a] > registers[b])


def eqir(registers, a, b, c):
    registers[c] = int(a == registers[b])


def eqri(registers, a, b, c):
    registers[c] = int(registers[a] == b)


def eqrr(registers, a, b, c):
    registers[c] = int(registers[a] == registers[b])


def noop(registers, a, b, c):
    pass


def execute(f, start_0=0):
    program = [line.strip() for line in f.readlines()]
    registers = [0] * 6
    registers[0] = start_0
    pc = 0
    bound_to = None

    while pc < len(program):
        if program[pc].startswith('#ip'):
            bound_to = int(program[pc][4:])
            del program[pc]
        else:
            pre_pc = pc

            if bound_to is not None:
                registers[bound_to] = pc

            #if pc == 13:
            #    registers[3] = 2
            #if pc == 29:
                #registers[2] =

            registers_pre = list(registers)
            op_code, in_a, in_b, out, *_ = program[pc].split(' ')

            globals()[op_code](registers, int(in_a), int(in_b), int(out))

            print(pc, registers_pre, op_code, in_a, in_b, out, registers)

            if bound_to is not None:
                pc = registers[bound_to]

            if pre_pc != pc:
                print(" pc was changed from ", pre_pc, "to", pc)
                #print("")
                pass

            pc += 1

            input('enter')

    return registers[0]


if __name__ == '__main__':
    print(execute(open('input/21'), start_0=8765139))


