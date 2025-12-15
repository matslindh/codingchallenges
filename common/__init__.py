from collections import defaultdict
from itertools import pairwise


def as_2d_ints(path):
    return [
        list(map(int, row))
        for row in rs(path)
    ]


def as_1d_ints(path):
    return list(map(int, rs(path)[0].split(' ')))


def rs(path):
    return open(path, encoding='utf-8').read().splitlines()


def as_board(path):
    lines = rs(path)
    ret = []

    for line in lines:
        ret.append(list(line))

    return ret


def lines_with_individual_digits(path):
    return tuple(
        map(
            lambda line: tuple(map(int, line)),
            rs(path)
        )
    )


class OrthogonalPolygon:
    def __init__(self, coords):
        self.lines = []

        for p1, p2 in pairwise(coords):
            self.lines.append((p1, p2))

        self.lines.append((coords[-1], coords[0]))

        x_lookup = defaultdict(set)
        y_lookup = defaultdict(set)

        for idx, (p1, p2) in enumerate(self.lines):
            prev_line = self.lines[(idx - 1) % len(self.lines)]
            next_line = self.lines[(idx + 1) % len(self.lines)]

            if p1[1] == p2[1]:
                arrival_vector = 'u' if prev_line[0][1] < p1[1] else 'd'
                left_vector = 'd' if next_line[1][1] < p2[1] else 'u'

                # if arrival_vector == left_vector:
                y_lookup[p1[1]].add((min(p1[0], p2[0]), abs(p1[0] - p2[0]) + 1, arrival_vector == left_vector))

                for x in range(min(p1[0], p2[0]) + 1, max(p1[0], p2[0])):
                    x_lookup[x].add((p1[1], 1, True))

            elif p1[0] == p2[0]:
                arrival_vector = 'r' if prev_line[0][0] < p1[0] else 'l'
                left_vector = 'l' if next_line[1][0] < p2[0] else 'r'

                x_lookup[p1[0]].add((min(p1[1], p2[1]), abs(p1[1] - p2[1]) + 1, arrival_vector == left_vector))

                for y in range(min(p1[1], p2[1]) + 1, max(p1[1], p2[1])):
                    y_lookup[y].add((p1[0], 1, True))
            else:
                raise ValueError('lines are not orthogonal')

        self.x_lookup = {
            x: list(sorted(ys))
            for x, ys in x_lookup.items()
        }

        self.y_lookup = {
            y: list(sorted(xs))
            for y, xs in y_lookup.items()
        }

    def line_is_inside_polygon(self, p1, p2):
        """
        Test if a line crosses outside/inside barriers. Lines must be orthogonal.

        :param p1: tuple(x, y)
        :param p2: tuple(x, y)
        :return:
        """
        if p1[1] == p2[1]:  # horizontal line
            start = min(p1[0], p2[0])
            end = max(p1[0], p2[0])

            # see if our line intersects with any of the region changes in this line.
            if p1[1] not in self.y_lookup:  # no lines go through here, so we're outside the polygon
                return False

            return self._evaluate_line_against_lookups(lookup=self.y_lookup[p1[1]], start=start, end=end)
        elif p1[0] == p2[0]:  # vertical line
            start = min(p1[1], p2[1])
            end = max(p1[1], p2[1])

            # see if our line intersects with any of the region changes in this line.
            if p1[0] not in self.x_lookup:  # no lines go through here, so we're outside the polygon
                return False

            return self._evaluate_line_against_lookups(lookup=self.x_lookup[p1[0]], start=start, end=end)
        else:
            raise ValueError('line is not orthogonal')

    @staticmethod
    def _evaluate_line_against_lookups(lookup, start, end):
        # lookup is already sorted
        inside = False

        for v_start, d, cuts in lookup:
            v_end = v_start + d

            # if our line is kept entirely by this line, it doesn't matter about tracking outside/inside
            if end < v_end:
                if start < v_start:  # our line goes "into" this segment
                    return inside

                # otherwise we're covered by this segment
                return True

            if not cuts:
                continue

            if v_start > start:  # we have passed into the next segment
                return False

            inside = not inside

        return inside

    @staticmethod
    def _evaluate_point_against_lookups(lookup, start, end):
        # THIS MUST BE PROPERLY IMPLEMENTED - JUST A PLACEHOLDER BASED ON THE ABOVE BEFORE CHANGING IT
        inside = False

        for v_start, d, cuts in lookup:
            v_end = v_start + d

            # if our line is kept entirely by this line, it doesn't matter about tracking outside/inside
            if end < v_end:
                if start < v_start:  # our line goes "into" this segment
                    return inside

                # otherwise we're covered by this segment
                return True

            if not cuts:
                continue

            inside = not inside

        return inside
