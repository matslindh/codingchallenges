possible_codes = []


def pattern_matcher_4000(start, max_length):
    def explore(current):
        if len(current) == max_length:
            possible_codes.append(current)
            return

        possible = {
            'A': {'direct': ('B', 'D', 'E', 'F', 'H'), 'conditional': {'G': 'D', 'I': 'E', 'C': 'B'}},
            'B': {'direct': ('A', 'C', 'D', 'E', 'F', 'G', 'I'), 'conditional': {'H': 'E'}},
            'C': {'direct': ('B', 'D', 'E', 'F', 'H'), 'conditional': {'A': 'B', 'G': 'E', 'I': 'F'}},
            'D': {'direct': ('A', 'B', 'C', 'E', 'G', 'H', 'I'), 'conditional': {'F': 'E'}},
            'E': {'direct': ('A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'), 'conditional': {}},
            'F': {'direct': ('A', 'B', 'C', 'E', 'F', 'G', 'H', 'I'), 'conditional': {'D': 'E'}},
            'G': {'direct': ('B', 'D', 'E', 'F', 'H'), 'conditional': {'A': 'D', 'C': 'E', 'I': 'H'}},
            'H': {'direct': ('A', 'C', 'D', 'E', 'F', 'G', 'I'), 'conditional': {'B': 'E'}},
            'I': {'direct': ('B', 'D', 'E', 'F', 'H'), 'conditional': {'A': 'E', 'C': 'F', 'G': 'H'}},
        }

        instructions = possible[current[-1]]

        for next_node in instructions['direct']:
            if next_node in current:
                continue

            explore(current + next_node)

        for next_node, depends in instructions['conditional'].items():
            if next_node in current:
                continue

            if depends not in current:
                continue

            explore(current + next_node)

    explore(start)


pattern_matcher_4000('D', max_length=8)
print(len(possible_codes))
