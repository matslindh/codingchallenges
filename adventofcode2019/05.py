def run(memory, inp):
    pc = 0
    output = []

    def resolve(val, immediate):
        if immediate:
            return val

        return memory[val]

    while memory[pc] != 99:
        decoded = '{:05d}'.format(memory[pc])
        op_code = int(decoded[3:])
        param_a_immediate = decoded[2] == '1'
        param_b_immediate = decoded[1] == '1'
        param_c_immediate = decoded[0] == '1'

        if op_code == 1:
            memory[memory[pc + 3]] = resolve(memory[pc + 1], param_a_immediate) + resolve(memory[pc + 2], param_b_immediate)
            pc += 4
        elif op_code == 2:
            memory[memory[pc + 3]] = resolve(memory[pc + 1], param_a_immediate) * resolve(memory[pc + 2], param_b_immediate)
            pc += 4
        elif op_code == 3:
            memory[memory[pc+1]] = inp
            pc += 2
        elif op_code == 4:
            output.append(resolve(memory[pc+1], param_a_immediate))
            pc += 2
        elif op_code == 5:
            if resolve(memory[pc + 1], param_a_immediate) != 0:
                pc = resolve(memory[pc + 2], param_b_immediate)
            else:
                pc += 3
        elif op_code == 6:
            if resolve(memory[pc + 1], param_a_immediate) == 0:
                pc = resolve(memory[pc + 2], param_b_immediate)
            else:
                pc += 3
        elif op_code == 7:
            dest = memory[pc + 3]
            memory[dest] = int(resolve(memory[pc + 1], param_a_immediate) < resolve(memory[pc + 2], param_b_immediate))
            pc += 4
        elif op_code == 8:
            dest = memory[pc+3]
            memory[dest] = int(resolve(memory[pc+1], param_a_immediate) == resolve(memory[pc+2], param_b_immediate))
            pc += 4

    return output


def load_and_execute(s, inp):
    memory = [int(r.strip()) for r in s.split(',')]
    return run(memory, inp)


def test_load_and_execute():
    assert [1] == load_and_execute('3,9,8,9,10,9,4,9,99,-1,8', 8)
    assert [0] == load_and_execute('3,9,8,9,10,9,4,9,99,-1,8', 9)

    assert [0] == load_and_execute('3,9,7,9,10,9,4,9,99,-1,8', 8)
    assert [1] == load_and_execute('3,9,7,9,10,9,4,9,99,-1,8', 7)

    assert [1] == load_and_execute('3,3,1108,-1,8,3,4,3,99', 8)
    assert [0] == load_and_execute('3,3,1108,-1,8,3,4,3,99', 9)

    assert [0] == load_and_execute('3,3,1107,-1,8,3,4,3,99', 8)
    assert [1] == load_and_execute('3,3,1107,-1,8,3,4,3,99', 7)


if __name__ == '__main__':
    print(load_and_execute(open('input/05').read(), inp=1))
    print(load_and_execute(open('input/05').read(), inp=5))