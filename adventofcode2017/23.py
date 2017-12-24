from collections import deque
from math import sqrt

def execute(instructions, debug=True, b=None, c=None):
    program = [x.split() for x in instructions]
    registers = {}

    if not debug:
        registers['a'] = 1

    pc = 0

    if b:
        registers['b'] = b
        pc += 1
        
        if c:
            registers['c'] = c
            pc += 1
    
    muls = 0

    def op_value(p):
        try:
            return int(p)
        except:
            if p not in registers:
                registers[p] = 0
                
            return registers[p]
    
    while True:
        if pc >= len(program) or pc < 0:
            break

        instr = program[pc]
        cmd = instr[0]
        reg = instr[1]
        op = None
        
        op_value(reg)
        
        if len(instr) > 2:
            op = op_value(instr[2])

        if cmd == 'set':
            registers[reg] = op
        elif cmd == 'sub':
            registers[reg] -= op
        elif cmd == 'mul':
            muls += 1
            registers[reg] *= op
        elif cmd == 'jnz':
            if op_value(reg) != 0:
                print('jump', pc, pc  + op, registers)
                pc += op
                continue

        print(instr[0], pc, registers)
        pc += 1

    return muls, registers['h'] if 'h' in registers else None

def naive(b, c):
    cnt = 0
    
    for x in range(b, c + 1, 17):
        for y in range(2, int(sqrt(x)) + 1):
            if x % y == 0:
                cnt += 1
                break

    return cnt            

if __name__ == "__main__":
    #for b in range(4, 300):
    #print(execute(open("input/dec23").readlines(), b=12, c=97))
    #print(naive(12, 97))
    print(naive(105700, 122700))
    # print(execute(open("input/dec23").readlines(), debug=False))
