from common import rs, OrthogonalPolygon
from itertools import combinations, pairwise


def make_largest_rectangle(path):
    coords = []

    for line in rs(path):
        x, y = line.split(',')
        x = int(x)
        y = int(y)

        coords.append(
            (x, y)
        )

    polygon_resolver = OrthogonalPolygon(coords=coords)

    part_1 = 0
    part_2 = 0

    for p1, p2 in combinations(coords, r=2):
        a = (abs(p1[0] - p2[0]) + 1) * \
            (abs(p1[1] - p2[1]) + 1)

        if a > part_1:
            part_1 = a

        if a <= part_2:
            # won't get any better
            continue

        # check lines in rectangle against polygon_resolver
        p1_x_p2_y = (p1[0], p2[1])
        p2_x_p1_y = (p2[0], p1[1])

        if all(
            (
                polygon_resolver.line_is_inside_polygon(p1, p1_x_p2_y),
                polygon_resolver.line_is_inside_polygon(p1_x_p2_y, p2),
                polygon_resolver.line_is_inside_polygon(p2, p2_x_p1_y),
                polygon_resolver.line_is_inside_polygon(p1_x_p2_y, p1),
            )
        ):
            if a > part_2:
                print(p1, p2)
                part_2 = a

    return part_1, part_2


def make_svg(path, highlight=None):
    with open('output/day09.svg', 'w') as f:
        lines = rs(path)
        xs = []
        ys = []

        for line in lines:
            x, y = line.split(',')
            xs.append(int(x))
            ys.append(int(y))

        min_x = min(xs) * 0.9
        max_x = max(xs) * 1.1
        min_y = min(ys) * 0.9
        max_y = max(ys) * 1.1

        f.write(f'<svg viewBox="{min_x} {min_y} {max_x} {max_y}" xmlns="http://www.w3.org/2000/svg">')
        f.write(f'<polyline points="{' '.join(lines)} {lines[0]}" fill="none" stroke="black" stroke-width="100" />')

        if highlight is not None:
            f.write(f'<polyline points="{highlight[0][0]} {highlight[0][1]} {highlight[0][0]} {highlight[1][1]} {highlight[1][0]} {highlight[1][1]} {highlight[1][0]} {highlight[0][1]} {highlight[0][0]} {highlight[0][1]}" fill="red" stroke="black" stroke-width="100" />')

        f.write(f'</svg>')


def test_make_largest_rectangle():
    assert make_largest_rectangle('input/09.test') == (50, 24)


if __name__ == '__main__':
    print(make_largest_rectangle('input/09'))
    make_svg('input/09', highlight=((5301, 67727), (94865, 50110)))


