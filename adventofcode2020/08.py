import copy

def parse(raw_instructions):
    instructions = []

    for r_i in raw_instructions:
        p = r_i.split(' ')

        instructions.append(
            [p[0], int(p[1])]
        )

    return instructions


def parse_and_execute(raw_instructions):
    instructions = parse(raw_instructions)
    return execute(instructions)[0]


def parse_modify_and_execute(raw_instructions):
    instructions = parse(raw_instructions)
    current = 0

    while current < len(instructions):
        if instructions[current][0] in ('nop', 'jmp'):
            modified = copy.deepcopy(instructions)
            modified[current][0] = 'jmp' if modified[current][0] == 'nop' else 'nop'
            acc, pc = execute(modified)

            if pc is None:
                return acc

        current += 1

    return None


def execute(instructions):
    acc = 0
    pc = 0

    while  pc < len(instructions) and instructions[pc] is not None:
        instr, mod = instructions[pc]
        instructions[pc] = None

        if instr == 'nop':
            pc += 1
        elif instr == 'acc':
            acc += mod
            pc += 1
        elif instr == 'jmp':
            pc += mod

    return acc, pc if pc < len(instructions) else None


def test_parse_and_execute():
    assert 5 == parse_and_execute([x.strip() for x in open('input/08.test').readlines()])


def test_parse_modify_and_execute():
    assert 8 == parse_modify_and_execute([x.strip() for x in open('input/08.test').readlines()])


if __name__ == '__main__':
    print(parse_and_execute([x.strip() for x in open('input/08').readlines()]))
    print(parse_modify_and_execute([x.strip() for x in open('input/08').readlines()]))