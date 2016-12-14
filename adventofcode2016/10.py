bots = {}
outputs = {}

bot_responsibility = (17, 61)


def init_bot(idx):
    bots[idx] = {
        'stack': [],
        'high': None,
        'high_output': None,
        'low': None,
        'low_output': None,
    }


def output_outputs():
    for k in sorted(outputs.keys()):
        print(str(k) + ': ' + ', '.join(outputs[k]))


def output(idx, val):
    if idx not in outputs:
        outputs[idx] = []

    outputs[idx].append(str(val))


def set_instruction(idx, low=None, low_output=None, high=None, high_output=None):
    if idx not in bots:
        init_bot(idx)

    if low is not None:
        bots[idx]['low'] = low

    if low_output is not None:
        bots[idx]['low_output'] = low_output

    if high is not None:
        bots[idx]['high'] = high

    if high_output is not None:
        bots[idx]['high_input'] = high_output


def give_bot(idx, val):
    if idx not in bots:
        init_bot(idx)

    # print("bot " + str(idx) + " gots " + str(val))

    bots[idx]['stack'].append(val)

    if len(bots[idx]['stack']) == 2:
        v1, v2 = sorted(bots[idx]['stack'])

        if v1 == bot_responsibility[0] and v2 == bot_responsibility[1]:
            print("Found the bot: " + str(idx) + " (" + str(v1) + ", " + str(v2) + ")")

        # print(" - bot " + str(idx) + " giving away " + str(v1) + ", " + str(v2))

        if bots[idx]['low'] is not None:
            give_bot(bots[idx]['low'], v1)
        elif bots[idx]['low_output'] is not None:
            output(bots[idx]['low_output'], v1)
        else:
            print("BARFED INSTRUCTION SET")

        if bots[idx]['high'] is not None:
            give_bot(bots[idx]['high'], v2)
        elif bots[idx]['high_output'] is not None:
            output(bots[idx]['high_output'], v2)
        else:
            print("BARFED INSTRUCTION SET")

        bots[idx]['stack'] = []


for line in sorted(open("input/dec10").readlines()):
    instr = line.strip().split(' ')

    if instr[0] == 'value':
        give_bot(int(instr[5]), int(instr[1]))
    elif instr[2] == 'gives':
        params = {'idx': int(instr[1])}

        if instr[5] == 'output':
            params['low_output'] = int(instr[6])
        else:
            params['low'] = int(instr[6])

        if instr[10] == 'output':
            params['high_output'] = int(instr[11])
        else:
            params['high'] = int(instr[11])

        if instr[1] == '4':
            print(params)

        set_instruction(**params)

output_outputs()