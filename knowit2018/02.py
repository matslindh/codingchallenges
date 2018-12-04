slopes = {}

for row in open('input/02').readlines():
    start, end = row.strip().split(';')
    sx, sy = [float(n) for n in start[1:-1].split(',')]
    ex, ey = [float(n) for n in end[1:-1].split(',')]

    slope = (sy - ey) / (sx - ex)

    if slope not in slopes:
        slopes[slope] = 0

    slopes[slope] += 1

print(max(slopes.values()))
