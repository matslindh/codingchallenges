import string

def react(inp):
    changed = True
    lookup = dict(zip(string.ascii_lowercase, string.ascii_uppercase))
    lookup.update(dict(zip(string.ascii_uppercase, string.ascii_lowercase)))

    while changed:
        output = ''
        skip = False

        for x in range(0, len(inp) - 1):
            if skip:
                skip = False
                continue

            if lookup[inp[x]] == inp[x + 1]:
                skip = True
                continue

            output += inp[x]

        if not skip:
            output += inp[x+1]

        changed = output != inp
        inp = output

    return output


def test_react():
    assert len(react('dabAcCaCBAcCcaDA')) == 10
    assert react('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'


if __name__ == '__main__':
    data = open('input/05').read().strip()
    print(len(react(data)))
    best = 999999999999

    for c in string.ascii_lowercase:
        print("Replacing " + c)
        res = len(react(data.replace(c, '').replace(c.upper(), '')))
        print('Result: ' + str(res))

        if res < best:
            print("!! New best")
            best = res

    print("Best with replacement: " + str(best))
