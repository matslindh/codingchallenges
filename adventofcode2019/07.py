class Computer:
    def __init__(self, memory, input_queue):
        self.memory = memory
        self.input_queue = input_queue
        self.pc = 0

    def add_input(self, v):
        self.input_queue.append(v)

    def run(self):
        memory = self.memory

        while memory[self.pc] != 99:
            decoded = '{:05d}'.format(memory[self.pc])
            op_code = int(decoded[3:])
            param_a_immediate = decoded[2] == '1'
            param_b_immediate = decoded[1] == '1'
            param_c_immediate = decoded[0] == '1'

            if op_code == 1:
                memory[memory[self.pc + 3]] = self.resolve(memory[self.pc + 1], param_a_immediate) + self.resolve(memory[self.pc + 2], param_b_immediate)
                self.pc += 4
            elif op_code == 2:
                memory[memory[self.pc + 3]] = self.resolve(memory[self.pc + 1], param_a_immediate) * self.resolve(memory[self.pc + 2], param_b_immediate)
                self.pc += 4
            elif op_code == 3:
                memory[memory[self.pc + 1]] = self.input_queue.pop(0)
                self.pc += 2
            elif op_code == 4:
                output = self.resolve(memory[self.pc + 1], param_a_immediate)
                self.pc += 2
                return output
            elif op_code == 5:
                if self.resolve(memory[self.pc + 1], param_a_immediate) != 0:
                    self.pc = self.resolve(memory[self.pc + 2], param_b_immediate)
                else:
                    self.pc += 3
            elif op_code == 6:
                if self.resolve(memory[self.pc + 1], param_a_immediate) == 0:
                    self.pc = self.resolve(memory[self.pc + 2], param_b_immediate)
                else:
                    self.pc += 3
            elif op_code == 7:
                dest = memory[self.pc + 3]
                memory[dest] = int(self.resolve(memory[self.pc + 1], param_a_immediate) < self.resolve(memory[self.pc + 2], param_b_immediate))
                self.pc += 4
            elif op_code == 8:
                dest = memory[self.pc + 3]
                memory[dest] = int(self.resolve(memory[self.pc + 1], param_a_immediate) == self.resolve(memory[self.pc + 2], param_b_immediate))
                self.pc += 4

        return None

    def resolve(self, val, immediate):
        if immediate:
            return val

        return self.memory[val]


def load_and_execute_sequence(s, inp):
    computers = []

    for x in inp:
        computers.append(Computer(memory=[int(r.strip()) for r in s.split(',')], input_queue=[x]))

    previous_val = 0
    running = 0
    still_running = len(computers)

    while still_running:
        computer = computers[running]
        computer.add_input(previous_val)

        output = computer.run()

        if output is not None:
            previous_val = output

        if output is None:
            still_running -= 1

        running += 1
        running = running % len(computers)

    return previous_val


def best_permutation(s, phases=(4, 3, 2, 1, 0)):
    from itertools import permutations
    best = -1
    best_instr = None

    for instr in permutations(phases):
        result = load_and_execute_sequence(s, inp=list(instr))

        if result > best:
            best = result
            best_instr = instr

    return best, best_instr


def test_load_and_execute():
    assert 43210 == load_and_execute_sequence('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', inp=[4, 3, 2, 1, 0])
    assert 54321 == load_and_execute_sequence('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0', inp=[0, 1, 2, 3, 4])
    assert 65210 == load_and_execute_sequence('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0', inp=[1, 0, 4, 3, 2])


def test_best_permutation():
    bp = best_permutation('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0')
    assert 43210 == bp[0]
    assert (4, 3, 2, 1, 0) == bp[1]

    bp = best_permutation('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0')
    assert 54321 == bp[0]
    assert (0, 1, 2, 3, 4) == bp[1]

    bp = best_permutation('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0')
    assert 65210 == bp[0]
    assert (1, 0, 4, 3, 2) == bp[1]


def test_best_permutation_b():
    bp = best_permutation('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5', phases=[9, 8, 7, 6, 5])
    assert 139629729 == bp[0]
    assert (9, 8, 7, 6, 5) == bp[1]

    bp = best_permutation('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10', phases=[9, 8, 7, 6, 5])
    assert 18216 == bp[0]
    assert (9, 7, 8, 5, 6) == bp[1]


print(best_permutation('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'))

if __name__ == '__main__':
    s = open('input/07').read()
    print(best_permutation(s))
    print(best_permutation(s, phases=[9, 8, 7, 6, 5]))


