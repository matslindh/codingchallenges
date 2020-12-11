base = ord('a')

def base_it(c):
    return ord(c) - base

def ascii_it(n):
    return chr(n + base)

def process(inp):
    if len(inp) == 1:
        return ''

    new = inp[1:]
    s = ''

    for idx, char in enumerate(new):
        n = (base_it(char) + 1) % 26
        s += ascii_it((n + base_it(inp[idx])) % 26)
    
    return s

def passwords(inp):
    possible = []
    
    while inp:
        possible.append(inp)
        inp = process(inp)

    pws = []

    for i in range(0, len(possible[0])):
        s = ''
        
        for x in range(0, len(possible[0]) - i):
            s += possible[x][i]
    
        pws.append(s)

    return pws

def test_process():
    assert process('juletre') == 'egqylw'
    assert process('egqylw') == 'lxpki'


def test_passwords():
    assert passwords('juletre') == ['jeljxmw', 'ugxnoj', 'lqpau', 'eykt', 'tli', 'rw', 'e']


if __name__ == '__main__':
    for word in open('input/11'):
        for pw in passwords(word):
            if 'eamqia' in pw:
                print(word)
