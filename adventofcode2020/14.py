from collections import defaultdict
from itertools import product


def parse_bitmask(mask):
    rules = {}

    for bit in range(0, 36):
        if mask[bit] != 'X':
            rules[35 - bit] = int(mask[bit])

    return rules


def parse_bitmask_v2(mask):
    rules = {}
    mangle_rules = []

    for bit in range(0, 36):
        if mask[bit] == '1':
            rules[35 - bit] = int(mask[bit])
        elif mask[bit] == 'X':
            mangle_rules.append([(35 - bit, 0), (35 - bit, 1)])

    return rules, mangle_rules


def masked_value(parsed_mask, inp):
    for bit, val in parsed_mask.items():
        if val:
            inp |= 1 << bit
        else:
            inp &= ~(1 << bit)

    return inp


def masked_value_v2(parsed_mask, inp):
    for bit, val in parsed_mask.items():
        if val:
            inp |= 1 << bit
        else:
            inp &= ~(1 << bit)

    return inp


def execute(commands):
    memory = defaultdict(int)
    mask = None

    for cmd in commands:
        if cmd.startswith('mask'):
            mask = parse_bitmask(cmd[7:])
        elif cmd.startswith('mem'):
            memstr, value = cmd.split(' = ')
            addr = int(memstr[4:-1])
            value = int(value)

            memory[addr] = masked_value(mask, value)

    return sum(memory.values())


def execute_v2(commands):
    memory = defaultdict(int)
    mask = None
    mangle_rules = None

    for cmd in commands:
        if cmd.startswith('mask'):
            mask, mangle_rules = parse_bitmask_v2(cmd[7:])
        elif cmd.startswith('mem'):
            memstr, value = cmd.split(' = ')
            value = int(value)
            src_addr = masked_value_v2(mask, int(memstr[4:-1]))

            for mangle_instr in product(*mangle_rules):
                mangled_mask = mask

                for instr in mangle_instr:
                    mangled_mask[instr[0]] = instr[1]

                addr = masked_value_v2(mangled_mask, src_addr)
                memory[addr] = value

    return sum(memory.values())


def execute_file(f, evaluator=execute):
    return evaluator([line.strip() for line in open(f)])


def test_parse_bitmask():
    assert parse_bitmask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == {6: 1, 1: 0}


def test_masked_value():
    bm = parse_bitmask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')

    assert masked_value(bm, 11) == 73
    assert masked_value(bm, 101) == 101
    assert masked_value(bm, 0) == 64


def test_execute():
    assert execute_file('input/14.test') == 165


def test_execute_v2():
    assert execute_file('input/14-2.test', evaluator=execute_v2) == 208


if __name__ == '__main__':
    print(execute_file('input/14'))
    print(execute_file('input/14', evaluator=execute_v2))
