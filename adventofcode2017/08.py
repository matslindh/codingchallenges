import operator


def execute(program):
    registers = {}
    m = 0

    for instr in program:
        if instr['reg_check'] not in registers:
            registers[instr['reg_check']] = 0

        if instr['reg'] not in registers:
            registers[instr['reg']] = 0

        if instr['op_check'](registers[instr['reg_check']], instr['op_cmp']):
            registers[instr['reg']] = instr['op'](registers[instr['reg']], instr['val'])

            if registers[instr['reg']] > m:
                m = registers[instr['reg']]

    return registers, m


def parse_program(f):
    program = []
    operators = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '==': operator.eq,
        '!=': operator.ne,
        '<=': operator.le,
    }

    instructions = {
        'inc': operator.add,
        'dec': operator.sub,
    }

    for line in open(f).readlines():
        reg, op, val, _, reg_check, op_check, op_cmp = line.strip().split(' ')

        program.append({
            'reg': reg,
            'op': instructions[op],
            'val': int(val),
            'reg_check': reg_check,
            'op_check': operators[op_check],
            'op_cmp': int(op_cmp)
        })

    return program


def execute_program_file(f):
    program = parse_program(f)
    return execute(program)


def execute_and_get_largest_values(f):
    registers, max_at_any_time = execute_program_file(f)

    return max(registers.values()), max_at_any_time


def test_execute_and_get_largest_values():
    assert 1, 10 == execute_and_get_largest_values('input/dec08_test')


if __name__ == "__main__":
    print(execute_and_get_largest_values('input/dec08'))