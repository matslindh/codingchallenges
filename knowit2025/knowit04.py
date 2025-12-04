from common import rs

path = rs('input/04.txt')[0]
cost = 5
energy = 3000

costs = {
    'S': cost,
    'B': cost * 2,
    'D': cost * 3,
}

for idx, c in enumerate(path):
    cost = costs.get(c, 0)
    energy -= cost

    if c == 'P':
        energy += costs.get(path[idx - 1], 0) + costs.get(path[idx - 2], 0)

    if energy <= 0:
        print(idx * 10)
        break
