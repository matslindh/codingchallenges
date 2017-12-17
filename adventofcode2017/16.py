def exec(programs, instructions):
    plen = len(programs)

    for instr in instructions:
        if instr[0] == 's':
            v = int(instr[1:])
            programs = programs[plen - v:] + programs[:plen - v]

        elif instr[0] == 'x':
            parts = instr[1:].split('/')
            p1 = int(parts[0])
            p2 = int(parts[1])

            programs[p1], programs[p2] = programs[p2], programs[p1]

        elif instr[0] == 'p':
            p1 = programs.index(instr[1])
            p2 = programs.index(instr[3]) 
            programs[p1], programs[p2] = programs[p2], programs[p1]

    return programs


def exec_jit(n, programs, instructions):
    lookup = {}
    iteration = 0
    repeats = 0
    
    while iteration < n:
        key = ''.join(programs)
        
        if key in lookup:
            iteration = n - (n % iteration)

        lookup[key] = True
        programs = exec(programs, instructions)
        
        iteration += 1
    
    return programs

def test_exec():
    assert 'baedc' == ''.join(exec(['a', 'b', 'c', 'd', 'e'], ['s1', 'x3/4', 'pe/b']))
    assert 'ceadb' == ''.join(exec(['b', 'a', 'e', 'd', 'c'], ['s1', 'x3/4', 'pe/b']))


if __name__ == "__main__":
    print(''.join(exec(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'], open("input/dec16").read().strip().split(','))))
    print(''.join(exec_jit(1000000000, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'], open("input/dec16").read().strip().split(','))))
