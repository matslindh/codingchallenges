def rotate(current, dir, num):
    seq = ['E', 'S', 'W', 'N']
    
    if dir == 'L':
        seq.reverse()
    
    num //= 90
    
    return seq[(seq.index(current) + num) % len(seq)]

def navigation_schmavigation(instructions):
    dir = 'E'
    x, y = 0, 0 
    
    for instr in instructions:
        inp = instr[0]
        op = int(instr[1:])

        if inp == 'F':
            inp = dir

        if inp in ('L', 'R'):
            dir = rotate(dir, inp, op)
        elif inp == 'E':
            x += op
        elif inp == 'S':
            y -= op
        elif inp == 'W':
            x -= op
        elif inp == 'N':
            y += op
        
    return abs(x) + abs(y)


def navigation_schmavigation_2(instructions):
    x_d, y_d = 10, 1
    x, y = 0, 0 
    
    for instr in instructions:
        inp = instr[0]
        op = int(instr[1:])

        if inp == 'F':
            x += x_d * op
            y += y_d * op

        if inp in ('L', 'R'):
            for _ in range(0, op, 90):
                if inp == 'L':
                    s = 1
                else:
                    s = -1

                x_d, y_d = -y_d * s, x_d * s
        elif inp == 'E':
            x_d += op
        elif inp == 'S':
            y_d -= op
        elif inp == 'W':
            x_d -= op
        elif inp == 'N':
            y_d += op
        
    return abs(x) + abs(y)


def test_navigation_schmavigation():
    assert navigation_schmavigation([l.strip() for l in open('input/12.test')]) == 25


def test_navigation_schmavigation_2():
    assert navigation_schmavigation_2([l.strip() for l in open('input/12.test')]) == 286


if __name__ == '__main__':
    print(navigation_schmavigation([l.strip() for l in open('input/12')]))
    print(navigation_schmavigation_2([l.strip() for l in open('input/12')]))
