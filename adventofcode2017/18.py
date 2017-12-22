from collections import deque

def execute(instructions):
    program = [x.split() for x in instructions]
    registers = {}
    pc = 0
    last_sound = None

    def op_value(p):
        try:
            return int(p)
        except:
            if p not in registers:
                registers[p] = 0
                
            return registers[p]
    
    while True:
        instr = program[pc]
        cmd = instr[0]
        reg = instr[1]
        op = None
        
        if reg not in registers:
            registers[reg] = 0
        
        if len(instr) > 2:
            op = op_value(instr[2])

        if cmd == 'snd':
            last_sound = registers[reg]
        elif cmd == 'set':
            registers[reg] = op
        elif cmd == 'add':
            registers[reg] += op
        elif cmd == 'mul':
            registers[reg] *= op
        elif cmd == 'mod':
            registers[reg] %= op
        elif cmd == 'rcv':
            if last_sound:
                return last_sound
        elif cmd == 'jgz':
            if registers[reg] > 0:
                pc += op
                continue

        pc += 1


def execute_multiple(instructions, program_id, input, output):
    program = [x.split() for x in instructions]
    registers = {'p': program_id}
    pc = 0
    last_sound = None

    def op_value(p):
        try:
            return int(p)
        except:
            if p not in registers:
                registers[p] = 0
                
            return registers[p]
    
    sent = 0
    
    while True:
        instr = program[pc]
        cmd = instr[0]
        reg = instr[1]
        op = None
        
        if reg not in registers:
            registers[reg] = 0
        
        if len(instr) > 2 and instr[2]:
            op = op_value(instr[2])

        if cmd == 'snd':
            output.append(op_value(reg))
            sent += 1
            # print(program_id, pc, "sending", reg, '=', registers[reg])
        elif cmd == 'set':
            registers[reg] = op
        elif cmd == 'add':
            registers[reg] += op
        elif cmd == 'mul':
            registers[reg] *= op
        elif cmd == 'mod':
            registers[reg] %= op
        elif cmd == 'rcv':
            if input:
                registers[reg] = input.popleft()
                #print(program_id, pc, "receiving", reg, '=', registers[reg])
            else:
                yield pc, sent
                pc -= 1
        elif cmd == 'jgz':
            if op_value(reg) > 0:
                pc += op
                continue

        pc += 1


def execute_parallel(instructions):
    buffer = deque()
    buffer2 = deque()
    pc_prev = None
    pc2_prev = None
    program1 = execute_multiple(instructions, 0, buffer, buffer2)
    program2 = execute_multiple(instructions, 1, buffer2, buffer)    
    lock_count = 0

    while True:
        print("Running 1")
        pc, sent = next(program1)
        print(len(buffer), len(buffer2), sent)
        print("Running 2")
        pc2, _ = next(program2)
        print(len(buffer), len(buffer2), sent)

        if pc == pc_prev and pc2 == pc2_prev and len(buffer) == 0 and len(buffer2) == 0:
            lock_count += 1

            if lock_count > 3:
                return sent
        else:
            lock_count = 0
            
        pc_prev = pc
        pc2_prev = pc2


def test_execute():
    assert 4 == execute(open("input/dec18_test").readlines())


def test_execute_parallel():
    assert 3 == execute_parallel(open("input/dec18_test_b").readlines())


if __name__ == "__main__":
    print(execute(open("input/dec18").readlines()))
    #print(execute_parallel(open("input/dec18_test_b").readlines()))
    print(execute_parallel(open("input/dec18").readlines()))
