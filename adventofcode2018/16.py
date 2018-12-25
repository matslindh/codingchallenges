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


def execute(f):
    program = [line.strip() for line in f.readlines()]

    ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    match_over_three_count = 0
    matches_per_op = {}
    op_code_mapping = {}

    for i in range(0, len(program), 4):
        input = [int(x) for x in program[i][9:-1].split(', ')]
        op_code, in_a, in_b, out = [int(x) for x in program[i+1].split(' ')]
        output = [int(x) for x in program[i+2][9:-1].split(', ')]
        matches = 0

        for op in ops:
            registers = list(input)
            op(registers, in_a, in_b, out)

            if registers == output:
                if op_code not in matches_per_op:
                    matches_per_op[op_code] = {}

                if op.__name__ not in matches_per_op[op_code]:
                    matches_per_op[op_code][op.__name__] = 0
                # print(input, op.__name__, in_a, in_b, out, output)
                matches_per_op[op_code][op.__name__] += 1
                matches += 1

        if matches >= 3:
            match_over_three_count += 1

        if matches == 0:
            print(input, op_code, in_a, in_b, out, output)


    import pprint
    pprint.pprint(matches_per_op)
    while matches_per_op:
        for op_code in dict(matches_per_op):
            if len(matches_per_op[op_code]) == 1:
                op = list(matches_per_op[op_code].keys())[0]
                op_code_mapping[op_code] = op
                print(op_code, '==', op)

                for inner_op_code in dict(matches_per_op):
                    if op in matches_per_op[inner_op_code]:
                        del matches_per_op[inner_op_code][op]

                    if len(matches_per_op[inner_op_code]) == 0:
                        del matches_per_op[inner_op_code]
                break

    return match_over_three_count, op_code_mapping


def execute_2(f, mapping):
    program = [line.strip() for line in f.readlines()]
    registers = [0] * 4

    for i in range(0, len(program)):
        op_code, in_a, in_b, out = [int(x) for x in program[i].split(' ')]
        globals()[mapping[op_code]](registers, in_a, in_b, out)

    return registers


def test_execute():
    assert execute(open('input/16.test')) == 1


def test_ops():
    inp = [7, 2, 0, 0]
    banr(inp, 0, 1, 3)
    assert inp == [7, 2, 0, 2]

    inp = [4, 1, 0, 0]
    borr(inp, 0, 1, 3)
    assert inp == [4, 1, 0, 5]


if __name__ == '__main__':
    matches, mapping = execute(open('input/16'))
    print(execute_2(open('input/16.program'), mapping=mapping))


