from functools import lru_cache

def dolls_all_the_way_down(f):
    dolls = []

    for line in f.readlines():
        color, size = line.strip().split(',')

        dolls.append((int(size), color))

    dolls = sorted(dolls)
    dolls_len = len(dolls)

    @lru_cache(None)
    def doll_it_up(idx, prev_size, prev_color, level=0):
        m = level

        for i in range(idx + 1, dolls_len):
            size, color = dolls[i]

            if size > prev_size and color != prev_color:
                m = max(m, doll_it_up(i, size, color, level+1))

        return m

    return doll_it_up(0, 0, None, 0)


print(dolls_all_the_way_down(open('input/08')))
