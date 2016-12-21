

# the letters at indexes X and Y (counting from 0) should be swapped
# assumes that each character only appears once
def swap(s, x, y):
    return swap_letter(s, s[x], s[y])


# the letters X and Y should be swapped (regardless of where they appear in the string).
def swap_letter(s, l, l2):
    return s.replace(l, '%%%').replace(l2, '&&&').replace('%%%', l2).replace('&&&', l)


def rotate_right(s, steps):
    return s[len(s)-steps:] + s[:len(s)-steps]


def rotate_left(s, steps):
    return s[steps:] + s[:steps]


def rotate_based(s, l):
    idx = s.index(l)

    # plus one additional time if the index was at least 4
    if idx >= 4:
        idx += 1

    # rotate the string to the right one time, plus a number of times equal to that index
    return rotate_right(s, idx + 1)


def derotate_based(s, l):
    idx = s.index(l)

    # plus one additional time if the index was at least 4
    if idx >= 5:
        idx += 1

    # rotate the string to the right one time, plus a number of times equal to that index
    return rotate_left(s, idx + 1)


# reverse positions X through Y
def reverse_s(s, start, end_inc):
    return s[:start] + ''.join(reversed(s[start:end_inc+1])) + s[end_inc+1:]


# move position X to position Y
def move(s, x, y):
    t = s[x]
    s = s[:x] + s[x+1:]
    s = s[:y] + t + s[y:]
    return s

# test
encode_string = 'abcde'
decode_string = 'decab'
fname = 'dec21_test'

# real a
#encode_string = 'abcdefgh'
#decode_string = 'bdfhgeca'
#fname = 'dec21'

# real b
encode_string = 'abcdefgh'
decode_string = 'fbgdceah'
fname = 'dec21'

"""
def decode(input_string, fname):
    prev_instr = None
    for line in reversed(open("input/" + fname).readlines()):
        print("start instruction with", input_string)
        instr = line.strip().split()

        expected = None

        if instr[len(instr) - 1][0] == ':':
            expected = instr[len(instr) - 1][1:]

        # check expected before we do transformation - if fail, we failed on previous instr
        if expected is not None and expected != input_string:
            print(prev_instr)
            print("Expected differed - actual", input_string, "expected", expected)

        if instr[0] == 'swap' and instr[1] == 'position':
            input_string = swap(input_string, int(instr[5]), int(instr[2]))

        elif instr[0] == 'swap' and instr[1] == 'letter':
            input_string = swap_letter(input_string, instr[5], instr[2])

        elif instr[0] == 'rotate':
            if instr[1] == 'left':
                input_string = rotate_right(input_string, int(instr[2]))
            elif instr[1] == 'right':
                input_string = rotate_left(input_string, int(instr[2]))
            elif instr[1] == 'based':
                # we need fix here
                input_string = derotate_based(input_string, instr[6])
            else:
                print("invalid rotate instruction", instr[1])

        elif instr[0] == 'reverse':
            input_string = reverse_s(input_string, int(instr[2]), int(instr[4]))

        elif instr[0] == 'move':
            input_string = move(input_string, int(instr[2]), int(instr[5]))

        else:
            print("invalid instruction", instr[0])

        prev_instr = instr

    return input_string"""


def encode(input_string, instructions, ignore_expected=False):
    for instr in instructions:
        expected = None

        if instr[len(instr) - 1][0] == ':':
            expected = instr[len(instr) - 1][1:]

        if instr[0] == 'swap' and instr[1] == 'position':
            input_string = swap(input_string, int(instr[2]), int(instr[5]))

        elif instr[0] == 'swap' and instr[1] == 'letter':
            input_string = swap_letter(input_string, instr[2], instr[5])

        elif instr[0] == 'rotate':
            if instr[1] == 'left':
                input_string = rotate_left(input_string, int(instr[2]))
            elif instr[1] == 'right':
                input_string = rotate_right(input_string, int(instr[2]))
            elif instr[1] == 'based':
                input_string = rotate_based(input_string, instr[6])
            else:
                print("invalid rotate instruction", instr[1])

        elif instr[0] == 'reverse':
            input_string = reverse_s(input_string, int(instr[2]), int(instr[4]))

        elif instr[0] == 'move':
            input_string = move(input_string, int(instr[2]), int(instr[5]))

        else:
            print("invalid instruction", instr[0])

        if not ignore_expected and expected is not None and expected != input_string:
            print(instr)
            print("Expected differed - actual", input_string, "expected", expected)

    return input_string

instructions = []

for line in open("input/" + fname).readlines():
    instr = line.strip().split()
    instructions.append(instr)

print(encode(encode_string, instructions))

import itertools

for attempt in itertools.permutations(decode_string):
    encd = encode(''.join(attempt), instructions, ignore_expected=True)
    if encd == decode_string:
        print(''.join(attempt))
        print(encode('gdfcabeh', instructions))


