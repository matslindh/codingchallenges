from collections import deque
from itertools import permutations
import heapq

nodes = {}
map = []
y = 0

for line in open("input/dec24").readlines():
    row = []
    x = 0

    for c in line.strip():
        if c == '#':
            row.append(False)
        elif c == '.':
            row.append('open')
        else:
            row.append(c)
            nodes[c] = {
                'x': x,
                'y': y,
                'name': c,
                'distances': {
                }
            }

        x += 1

    map.append(row)
    y += 1


def bfs(n_n):
    visited = {}
    root = nodes[n_n]
    queue = deque([(root['x'], root['y'], 0)])

    while queue:
        x, y, steps = queue.popleft()

        if y not in visited:
            visited[y] = {}
        elif x in visited[y]:
            continue

        visited[y][x] = True

        if map[y][x] != 'open':
            root['distances'][map[y][x]] = steps

        if map[y - 1][x]:
            queue.append((x, y - 1, steps+1))

        if map[y + 1][x]:
            queue.append((x, y + 1, steps + 1))

        if map[y][x - 1]:
            queue.append((x - 1, y, steps + 1))

        if map[y][x + 1]:
            queue.append((x + 1, y, steps + 1))

# find shortest path between all nodes
for n in nodes:
    bfs(n)

best = None
best_seq = None
ks = list(nodes.keys())

# remove 0 first
del ks[0]

for permutation in permutations(nodes.keys()):
    permutation = ['0'] + list(permutation) + ['0']  # last ['0'] is b challenge

    d = 0

    for i in range(1, len(permutation)):
        d += nodes[permutation[i-1]]['distances'][permutation[i]]

    if best is None or d < best:
        best = d
        best_seq = permutation

print(best, ''.join(best_seq))