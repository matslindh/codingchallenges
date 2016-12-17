from hashlib import md5

max_x = 3
max_y = 3

passcode = 'yjjvjgan'
passcode_len = len(passcode)

queue = [(passcode, 0, 0)]
been_here = {}


def visited(x, y, next):
    if y not in been_here:
        been_here[y] = {}

    if x not in been_here[y]:
        been_here[y][x] = {}

    if next not in been_here[y][x]:
        been_here[y][x][next] = True
        return False
    else:
        return True


while queue:
    passcode, x, y = queue.pop(0)

    if x == max_x and y == max_y:
        print(passcode[passcode_len:])  # len(passcode[passcode_len:]) for b
        break  # continue for b

    up, down, left, right = [ord(x) > 97 for x in md5(passcode.encode('ascii')).hexdigest()[:4]]

    if up and y > 0:
        queue.append((passcode + 'U', x, y - 1))

    if down and y < max_y:
        queue.append((passcode + 'D', x, y + 1))

    if left and x > 0:
        queue.append((passcode + 'L', x - 1, y))

    if right and x < max_x:
        queue.append((passcode + 'R', x + 1, y))

    #print(up, down, left, right)

