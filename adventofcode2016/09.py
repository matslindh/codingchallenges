import re


def expander(s):
    i = 0
    output = ''

    while True and i < len(s):
        m = re.search(r'\(([0-9]+)x([0-9]+)\)', s[i:])

        if not m:
            break

        # output everything from last hit to our current match start
        output += s[i:i+m.start()]

        # set up parameters from match
        chars = int(m.group(1))
        repeats = int(m.group(2))

        # start repeating from the end of the string
        i += m.end()

        for _ in range(0, repeats):
            output += s[i:i+chars]

        # move instruction pointer to after repeat instruction
        i += chars

    output += s[i:]
    return output

for line in open("input/dec09").readlines():
    print(len(expander(line.strip())))