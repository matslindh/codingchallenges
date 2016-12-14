import re

expanded_length = {}


def expander(s):
    i = 0
    l = 0

    while True and i < len(s):
        m = re.search(r'\(([0-9]+)x([0-9]+)\)', s[i:])

        if not m:
            break

        # output everything from last hit to our current match start
        l += m.start()

        # set up parameters from match
        chars = int(m.group(1))
        repeats = int(m.group(2))

        # start repeating from the end of the string
        i += m.end()

        expand = ''

        for _ in range(0, repeats):
            expand += s[i:i+chars]

        if expand not in expanded_length:
            expanded_length[expand] = expander(expand)

        l += expanded_length[expand]

        # move instruction pointer to after repeat instruction
        i += chars

    l += len(s) - i

    return l

for line in open("input/dec09").readlines():
    print(expander(line.strip()))