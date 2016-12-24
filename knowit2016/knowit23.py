from functools import lru_cache
from math import floor, ceil

scount = 250
steps = [1, 2, 4]

for i in range(3, scount):
    steps.append(steps[i-1] + steps[i-2] + steps[i-3])

print(steps[scount-1])


memo = {}


def recurse(steps_left):
    if steps_left in memo:
        return memo[steps_left]

    if steps_left == 0:
        return 1

    moved = 0

    if steps_left:
        memo[steps_left - 1] = recurse(steps_left - 1)
        moved += memo[steps_left - 1]

    if steps_left > 1:
        memo[steps_left - 2] = recurse(steps_left - 2)
        moved += memo[steps_left - 2]

    if steps_left > 2:
        memo[steps_left - 3] = recurse(steps_left - 3)
        moved += memo[steps_left - 3]

    return moved

print(recurse(scount))