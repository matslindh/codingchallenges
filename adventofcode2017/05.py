def execute_list(program):
    pc = 0
    l = len(program)
    steps = 0

    while pc < l and pc > -1:
        npc = pc + program[pc]
        program[pc] += 1
        pc = npc
        steps += 1
    
    return steps

def execute_list_2(program):
    pc = 0
    l = len(program)
    steps = 0

    while pc < l and pc > -1:
        npc = pc + program[pc]

        if program[pc] > 2:
            program[pc] -= 1
        else:
            program[pc] += 1

        pc = npc
        steps += 1
    
    return steps
    
def test_execute_list():
    assert 5 == execute_list([0, 3, 0, 1, -3])

def test_execute_list():
    assert 10 == execute_list_2([0, 3, 0, 1, -3])

if __name__ == "__main__":
    print(execute_list([int(x) for x in open('input/dec05').readlines()]))
    print(execute_list_2([int(x) for x in open('input/dec05').readlines()]))
