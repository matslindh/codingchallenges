input = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'
map = []
limit = 400000

for _ in range(0, limit):
    map.append(input)
    new = ''

    for i in range(0, len(input)):
        # safe?
        left = input[i-1] == '.' if i > 0 else True
        center = input[i] == '.'
        right = input[i+1] == '.' if i < (len(input) - 1) else True

        # trap!
        trap = (not left and not center and right) or (left and not center and not right) or (not left and center and right) or (left and center and not right)

        new += '.' if not trap else '^'

    if _ % 1000 == 0:
        print(_)

    input = new

safe_cnt = 0

for line in map:
    for c in line:
        if c == '.':
            safe_cnt += 1

    #print(''.join(line))

print(safe_cnt)