import copy
from hashlib import md5

nodes = {}
pairs = {}

for line in open("input/dec22").readlines()[2:]:
    node, _, used, avail, _ = line.split()
    
    nn = node.split('-')
    x = int(nn[1][1:])
    y = int(nn[2][1:])
    
    used = int(used[:-1])
    avail = int(avail[:-1])
    
    if y not in nodes:
        nodes[y] = {}
        
    nodes[y][x] = {'used': used, 'free': avail, 'has_data': False}


original = copy.deepcopy(nodes)
width = x + 1
height = y + 1
original[0][width-1]['has_data'] = True

cnt = 0

# calculate possible moves
for y in range(0, height):
    for x in range(0, width):
        if not nodes[y][x]['used']:
            continue

        for y2 in range(0, height):
            for x2 in range(0, width):
                if x == x2 and y == y2:
                    continue
            
                if nodes[y][x]['used'] <= nodes[y2][x2]['free']:
                    # print((x, y), (x2, y2))
                    cnt += 1
                    
# print(cnt)
import sys

def print_nodes(nodes):
    for y in nodes:
        for x in nodes[y]:
            if nodes[y][x]['has_data']:
                sys.stdout.write('G')
            elif x == 0 and y == 0:
                sys.stdout.write('e')
            else:
                # sys.stdout.write(str(nodes[y][x]['used']))
                if nodes[y][x]['used'] > 200:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write('_' if not nodes[y][x]['used'] else '.')

            x += 1
            
        sys.stdout.write("\n")

    sys.stdout.write("\n")

from collections import deque
queue = deque([])

# prod
queue.append((original, 35, 18, 0))
# test
# queue.append((original, 1, 1, 0))

#print(len(original[0]))
#for x in range(0, len(original[0])):
#    print(original[0][x]['free'], original[0][x]['used'])

seen = {}

def hash_dict(d):
    return md5(bytes(str(d), 'ascii')).hexdigest()


def move_content(nodes, from_x, from_y, to_x, to_y, move_data=False):
    if move_data:
        nodes[to_y][to_x]['has_data'] = nodes[from_y][from_x]['has_data']
        nodes[from_y][from_x]['has_data'] = False

    nodes[to_y][to_x]['free'] -= nodes[from_y][from_x]['used']
    nodes[to_y][to_x]['used'] += nodes[from_y][from_x]['used']

    nodes[from_y][from_x]['free'] = nodes[from_y][from_x]['free'] + nodes[from_y][from_x]['used']
    nodes[from_y][from_x]['used'] = 0

    if nodes[to_y][to_x]['has_data']:
        return (to_x, to_y)

    return None

import os.path
import pickle
import heapq
from math import sqrt
printed = {}

if not os.path.exists('input/22.pickle'):
    visited = {}

    # move stuff around
    while queue:
        nodes, x, y, steps = queue.popleft()

        if y not in visited:
            visited[y] = {}
        elif x in visited[y]:
            continue

        visited[y][x] = True

        if steps not in printed:
            print(steps)
            print_nodes(nodes)
            printed[steps] = True

        if nodes[y][x]['has_data']:
            print("got there", steps)
            break

        if y and nodes[y][x]['free'] >= nodes[y-1][x]['used']:
            n_nodes = copy.deepcopy(nodes)
            move_content(n_nodes, x, y-1, x, y)
            queue.append((n_nodes, x, y-1, steps + 1))

        if y < (height - 1) and nodes[y][x]['free'] >= nodes[y+1][x]['used']:
            n_nodes = copy.deepcopy(nodes)
            if nodes[y+1][x]['has_data']:
                # we got close to the actual data, abort here plz
                break
            move_content(n_nodes, x, y+1, x, y)
            queue.append((n_nodes, x, y+1, steps+1))

        if x and nodes[y][x]['free'] >= nodes[y][x-1]['used']:
            n_nodes = copy.deepcopy(nodes)
            move_content(n_nodes, x-1, y, x, y)
            queue.append((n_nodes, x-1, y, steps + 1))

        if x < (width - 1) and nodes[y][x]['free'] >= nodes[y][x+1]['used']:
            n_nodes = copy.deepcopy(nodes)
            if nodes[y][x+1]['has_data']:
                # we got close to the actual data, abort here plz
                print(steps)
                break
            move_content(n_nodes, x+1, y, x, y)
            queue.append((n_nodes, x+1, y, steps + 1))

    print_nodes(nodes)
    pickle.dump((nodes, x, y, x+1, y, steps), open('input/22.pickle', 'wb'))
    q = (nodes, x, y, x+1, y, steps)
else:
    print("skipped it")
    q = pickle.load(open('input/22.pickle', 'rb'))

queue = deque([q])

# we can live on the top for this, no need to get down dirty
height = min(2, height)
printed = {}
data_has_been_here = {}

# move data around
while queue:
    nodes, x, y, data_x, data_y, steps = queue.popleft()

    if nodes[y][x]['has_data']:
        if y in data_has_been_here and x in data_has_been_here[y]:
            continue

        if y not in data_has_been_here:
            data_has_been_here[y] = {}

        data_has_been_here[y][x] = True

    h = hash_dict(nodes)

    if h in seen:
        continue

    seen[h] = True

    if steps not in printed:
        print(steps)
        print_nodes(nodes)
        printed[steps] = True

    if nodes[0][0]['has_data']:
        print("got there again", steps)
        break

    if y < (height - 1) and nodes[y][x]['free'] >= nodes[y+1][x]['used']:
        n_nodes = copy.deepcopy(nodes)
        d = move_content(n_nodes, x, y+1, x, y, move_data=True)

        d_x = data_x
        d_y = data_y

        if d:
            d_x, d_y = d

        if abs(y + 1 - d_y) < 2:
            queue.append((n_nodes, x, y+1, d_x, d_y, steps+1))

    if y and nodes[y][x]['free'] >= nodes[y-1][x]['used']:
        n_nodes = copy.deepcopy(nodes)
        d = move_content(n_nodes, x, y-1, x, y, move_data=True)

        d_x = data_x
        d_y = data_y

        if d:
            d_x, d_y = d

        if abs(y - 1 - d_y) < 2:
            queue.append((n_nodes, x, y-1, d_x, d_y, steps + 1))

    if x and nodes[y][x]['free'] >= nodes[y][x-1]['used']:
        n_nodes = copy.deepcopy(nodes)
        d = move_content(n_nodes, x-1, y, x, y, move_data=True)

        d_x = data_x
        d_y = data_y

        if d:
            d_x, d_y = d

        if abs(x - 1 - d_x) < 2:
           queue.append((n_nodes, x-1, y, d_x, d_y, steps + 1))

    if x < (width - 1) and nodes[y][x]['free'] >= nodes[y][x+1]['used']:
        n_nodes = copy.deepcopy(nodes)
        d = move_content(n_nodes, x+1, y, x, y, move_data=True)

        d_x = data_x
        d_y = data_y

        if d:
            d_x, d_y = d

        if abs(x + 1 - d_x) < 2:
            queue.append((n_nodes, x+1, y, d_x, d_y, steps + 1))
