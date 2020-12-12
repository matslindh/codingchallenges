from collections import defaultdict

def level_counter(s):
    levels = defaultdict(int)
    level = 0
    
    for name in s.split(' '):
        if name[0] == '(':
            level += 1

        levels[level] += 1
        
        if name[-1] == ')':
            level -= len(name) - len(name.rstrip(')'))

    return levels

print(level_counter(open('input/12').read()))
