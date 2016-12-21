pyramid = []


def solve_pyramid(pyramid):
    maxes = [pyramid[len(pyramid) - 1]]

    for y in range(len(pyramid) - 2, -1, -1):
        row = []
        maxes_idx = len(pyramid) - 2 - y

        for x in range(0, len(pyramid[y])):
            row.append(max(maxes[maxes_idx][x], maxes[maxes_idx][x+1]) + pyramid[y][x])

        maxes.append(row)

    return maxes[len(maxes)-1][0]


def rotate_pyramid(pyramid):
    next = []

    for x in range(len(pyramid) - 1, -1, -1):
        row = []

        for y in range(x, len(pyramid)):
            row.append(pyramid[y][x])

        next.append(row)

    return next

for line in open("input/knowit21").readlines():
    pyramid.append([int(x) for x in line.strip().split()])


# A
print('A' + str(solve_pyramid(pyramid)))

# B
pyramid = rotate_pyramid(pyramid)
print('B' + str(solve_pyramid(pyramid)))


# C
pyramid = rotate_pyramid(pyramid)
print('C' + str(solve_pyramid(pyramid)))
