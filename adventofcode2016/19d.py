import math
from collections import deque

inp = 3004953
inp = 9

left, right = deque(), deque()
left, right, merged = [], [], []
half = math.floor(inp/2) + 1

for i in range(0, inp):
    merged.append(i+1)
    right.append(i+1)
    left.append(half+i)

if inp % 2 == 1:
    left.append(inp)

len_c = len(left) + len(right)

while len(merged) > 1:
    right = merged[:math.floor(len(merged) / 2)]
    left = merged[math.floor(len(merged) / 2):]

    r_idx = 0
    l_idx = 0

    print(right, left)

    if len(left) > 1:
        left = [left[1]]
        print(math.floor(len(right) / 2))

    del right[math.floor(len(right) / 2)]
    """for r in range(0, len(right)):
        print(right, left, l_idx, r_idx, len_c)
        #print(right[r], 'takes', left[math.ceil(l_idx/2)])
        left.pop(math.ceil(l_idx/2))
        l_idx += 1

        if l_idx % 1000 == 0:
            print('+', l_idx)"""

    #print(left[0], 'takes', right[math.floor(len(right)/2)])

    merged = right + left

    if len(merged) % 1000 == 0:
        print(len(merged))

    print("NEW ")
    print(right, left)

print(merged)