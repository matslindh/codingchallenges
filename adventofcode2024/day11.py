from common import as_1d_ints
from collections import defaultdict


def resolve_stones(path, steps_to_perform=26):
    stones = as_1d_ints(path)
    stone_results = defaultdict(defaultdict)
    stats = {'calls': 0}

    def explore_stone(stone, step=1, parents=None):
        stats['calls'] += 1
        if stone in stone_results and step in stone_results[stone]:
            return stone_results[stone][step]

        # MÅ LEGGE PÅ CACHING HER - DET GJØR VI VED Å VITE AT 1 BLIR TIL X BLIR TIL Y BLIR TIL Z
        # FOR HVERT NIVÅ NEDOVEr

        if not parents:
            parents = tuple()

        parents += ((stone, step), )

        if step == steps_to_perform:
            result = 1
        elif stone == 0:
            result = explore_stone(1, step + 1, parents)
        elif len(str(stone)) % 2 == 0:
            s_stone = str(stone)
            l = len(s_stone) // 2

            left = int(s_stone[:l])
            right = int(s_stone[l:])

            result = explore_stone(left, step + 1, parents) + explore_stone(right, step + 1, parents)
        else:
            result = explore_stone(stone * 2024, step + 1, parents)

        stone_results[stone][step] = result
        return result

    res = 0

    for start in stones:
        res += explore_stone(start)

    print("")
    print("calls", stats['calls'])
    return res

def test_resolve_stones():
    assert resolve_stones("input/11.test") == 55312


if __name__ == '__main__':
    print(resolve_stones("input/11"))
    print(resolve_stones("input/11", steps_to_perform=76))
