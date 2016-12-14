import re, copy
import sys
sys.setrecursionlimit(50)

queue_max = 0
best = 999999999999999

initial_floors = [
    [],
    [],
    [],
    [],
]

best_so_far = {}


def checksum(elevator_on, floors):
    fidx = 0
    csum = ''

    for floor in floors:
        csum += str(fidx) + ':'

        entries = []
        already = {}

        for x in sorted(floor):
            x_ext = x[1:]
            x_key = x[0]

            if x_key == 'G' and ('M' + x_ext) in floor:
                if x_ext not in already:
                    already[x_ext] = True
                    entries.append('X-X')

                continue

            if x_key == 'M' and ('G' + x_ext) in floor:
                if x_ext not in already:
                    already[x_ext] = True
                    entries.append('X-X')

                continue

            entries.append(x)

        csum += '_'.join(entries) + '|'
        fidx += 1

    return csum + '_' + str(elevator_on)


def valid(floors):
    for floor in floors:
        has = {'generators': [], 'microchips': []}

        for obj in floor:
            if obj[0] == 'G':
                has['generators'].append(obj[2:])
            elif obj[0] == 'M':
                has['microchips'].append(obj[2:])

        if not has['generators']:
            continue

        for mc in has['microchips']:
            if mc not in has['generators']:
                return False

    return True


def print_floors(floors, lift_on, steps):
    idx = len(floors)

    for f in floors[::-1]:
        l = '    '

        if (idx - 1) == lift_on:
            l = 'E   '

        print(str(idx) + ': ' + l + '  '.join([x[:4] for x in f]))

        idx -= 1

    print('Steps to get here: ' + str(steps))
    print('----------')


def step(floors, lift_on=0, steps=0):
    queue = [(floors, lift_on, steps)]
    queue_entries = 0

    while queue:
        floors, lift_on, steps = queue.pop(0)

        cs = checksum(lift_on, floors)

        if cs.startswith('0:|1:|2:|3:'):
            print(steps)
            print("Queue entries: " + str(queue_entries))
            sys.exit()

        if cs in best_so_far:
            continue

        lowest_with = 0

        for e in range(0, len(floors)):
            if floors[e]:
                lowest_with = e
                break

        best_so_far[cs] = steps
        queue_entries += 1
        lqueue = len(queue)

        if lqueue % 1000 == 0:
            print(len(queue))

        lift_up = lift_on + 1
        lift_down = lift_on - 1

        for i in range(0, len(floors[lift_on])):
            for j in range(i+1, len(floors[lift_on])):
                # try to move stuff up
                if lift_up < 4:
                    new_floors = copy.deepcopy(floors)
                    new_floors[lift_up].append(new_floors[lift_on].pop(j))
                    new_floors[lift_up].append(new_floors[lift_on].pop(i))

                    if valid(new_floors):
                        queue.append((new_floors, lift_up, steps+1))

                # try to move stuff down
                if lift_down >= lowest_with and (floors[lift_on][i][0] == 'M' and floors[lift_on][j][0] == 'M'):
                    new_floors = copy.deepcopy(floors)
                    new_floors[lift_down].append(new_floors[lift_on].pop(j))
                    new_floors[lift_down].append(new_floors[lift_on].pop(i))

                    if valid(new_floors):
                        queue.append((new_floors, lift_down, steps+1))

        # move single elements as well..
        for i in range(0, len(floors[lift_on])):
            if lift_up < 4:
                new_floors = copy.deepcopy(floors)
                new_floors[lift_up].append(new_floors[lift_on].pop(i))

                if valid(new_floors):
                    queue.append((new_floors, lift_up, steps + 1))

            if lift_down >= lowest_with and floors[lift_on][i][0] == 'G':
                new_floors = copy.deepcopy(floors)
                new_floors[lift_down].append(new_floors[lift_on].pop(i))

                if valid(new_floors):
                    queue.append((new_floors, lift_down, steps + 1))

    print("Empty queue - didn't find a valid sequence.")

floor_idx = 0

for line in open("input/dec11_b").readlines():
    line = line.strip()

    mcs = re.findall(' ([a-z]+)-compatible', line)
    gens = re.findall(' ([a-z]+) generator', line)

    for mc in mcs:
        initial_floors[floor_idx].append('M-' + mc)

    for g in gens:
        initial_floors[floor_idx].append('G-' + g)

    floor_idx += 1

print(initial_floors)

step(initial_floors, 0, 0)

for b in best_so_far:
    if b.startswith('0:|1:|2:|3:'):
        print(best_so_far[b])