from common import as_1d_ints
from functools import cache

def resolve_stones(path, steps_to_perform=26):
    stones = as_1d_ints(path)
    stats = {'calls': 0}

    @cache
    def explore_stone(stone, step=1):
        if step == steps_to_perform:
            result = 1
        elif stone == 0:
            result = explore_stone(1, step + 1)
        elif len(str(stone)) % 2 == 0:
            s_stone = str(stone)
            l = len(s_stone) // 2

            left = int(s_stone[:l])
            right = int(s_stone[l:])

            result = explore_stone(left, step + 1) + explore_stone(right, step + 1)
        else:
            result = explore_stone(stone * 2024, step + 1)

        return result

    res = 0

    for start in stones:
        res += explore_stone(start)

    return res

def test_resolve_stones():
    assert resolve_stones("input/11.test") == 55312


if __name__ == '__main__':
    print(resolve_stones("input/11"))
    print(resolve_stones("input/11", steps_to_perform=76))
