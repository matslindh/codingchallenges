def possible(returned, children):
    res = set()

    for i in range(1, 2001):
        res.add(returned + i * children)

    return res


print(possible(1854803357, 2424154637) & possible(2787141611, 2807727397) & possible(1159251923, 2537380333))

