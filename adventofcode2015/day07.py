from typing import List
from bitstring import BitArray


def run_circuit(lines: List[str], initial):
    instructions = []

    for line in lines:
        source, output = line.split(' -> ')
        instr = source.split()

        if len(instr) == 1:  # const
            if instr[0].isdigit():
                if output in initial:
                    continue

                instructions.append(('store_const', int(instr[0]), output))
            else:
                instructions.append(('mov', instr[0], output))
        elif len(instr) == 2:
            assert instr[0] == 'NOT'
            instructions.append(('not', instr[1], output))
        elif len(instr) == 3:
            if instr[1] == 'AND':
                if instr[0].isdigit():
                    instructions.append(('and_const_l', (int(instr[0]), instr[2]), output))
                elif instr[1].isdigit():
                    instructions.append(('and_const_r', (instr[0], int(instr[2])), output))
                else:
                    instructions.append(('and', (instr[0], instr[2]), output))
            elif instr[1] == 'OR':
                instructions.append(('or', (instr[0], instr[2]), output))
            elif instr[1] == 'LSHIFT':
                instructions.append(('lshift', (instr[0], int(instr[2])), output))
            elif instr[1] == 'RSHIFT':
                instructions.append(('rshift', (instr[0], int(instr[2])), output))
            else:
                print(f"Unknown instruction {instr}")

    wires = initial

    while instructions:
        kept_instructions = []

        for instruction in instructions:
            instr, ops, output = instruction

            if instr == 'store_const' and output not in wires:
                wires[output] = BitArray(uint=ops, length=16)
                continue

            if instr == 'mov' and ops in wires:
                wires[output] = wires[ops]
                continue

            if instr == 'and' and ops[0] in wires and ops[1] in wires:
                wires[output] = wires[ops[0]] & wires[ops[1]]
                continue

            if instr == 'and_const_l' and ops[1] in wires:
                wires[output] = BitArray(uint=ops[0], length=16) & wires[ops[1]]
                continue

            if instr == 'and_const_r' and ops[0] in wires:
                wires[output] = wires[ops[0]] & BitArray(uint=ops[1], length=16)
                continue

            if instr == 'or' and ops[0] in wires and ops[1] in wires:
                wires[output] = wires[ops[0]] | wires[ops[1]]
                continue

            if instr == 'lshift' and ops[0] in wires:
                wires[output] = wires[ops[0]] << ops[1]
                continue

            if instr == 'rshift' and ops[0] in wires:
                wires[output] = wires[ops[0]] >> ops[1]
                continue

            if instr == 'not' and ops in wires:
                wires[output] = ~wires[ops]
                continue

            kept_instructions.append(instruction)

        instructions = kept_instructions

    return wires


if __name__ == '__main__':
    wires = run_circuit(open("input/07").read().splitlines(), initial={})

    print(wires['a'].uint16)

    """for wire, value in wires.items():
        print(wire, value.uint16)"""

    wires2 = run_circuit(open("input/07").read().splitlines(), initial={'b': wires['a']})

    print(wires2['a'].uint16)
    """"for wire, value in wires2.items():
        print(wire, value.uint16)"""
