def execute(program, iterations):
    state = 'A'
    tape = {}
    cursor = 0

    for i in range(0, iterations):
        if state not in program:
            print("Invalid state: " + str(state))
            return

        if not cursor in tape:
            tape[cursor] = 0

        ne = program[state][tape[cursor]]

        tape[cursor] = ne['write']
        cursor += ne['cursor']
        state = ne['new_state']

    checksum = 0

    for k in tape:
        checksum += tape[k]

    return checksum


def test_execute():
    program = {
        'A': {
            0: {
                'write': 1,
                'cursor': 1,
                'new_state': 'B',
            },
            1: {
                'write': 0,
                'cursor': -1,
                'new_state': 'B',
            }
        },
        'B': {
            0: {
                'write': 1,
                'cursor': -1,
                'new_state': 'A',
            },
            1: {
                'write': 1,
                'cursor': 1,
                'new_state': 'A',
            },
        },
    }

    assert 3 == execute(program, 6)


if __name__ == "__main__":
    program = {
        'A': {
            0: {
                'write': 1,
                'cursor': 1,
                'new_state': 'B',
            },
            1: {
                'write': 0,
                'cursor': 1,
                'new_state': 'C',
            }
        },
        'B': {
            0: {
                'write': 0,
                'cursor': -1,
                'new_state': 'A',
            },
            1: {
                'write': 0,
                'cursor': 1,
                'new_state': 'D',
            }
        },
        'C': {
            0: {
                'write': 1,
                'cursor': 1,
                'new_state': 'D',
            },
            1: {
                'write': 1,
                'cursor': 1,
                'new_state': 'A',
            }
        },
        'D': {
            0: {
                'write': 1,
                'cursor': -1,
                'new_state': 'E',
            },
            1: {
                'write': 0,
                'cursor': -1,
                'new_state': 'D',
            }
        },
        'E': {
            0: {
                'write': 1,
                'cursor': 1,
                'new_state': 'F',
            },
            1: {
                'write': 1,
                'cursor': -1,
                'new_state': 'B',
            }
        },
        'F': {
            0: {
                'write': 1,
                'cursor': 1,
                'new_state': 'A',
            },
            1: {
                'write': 1,
                'cursor': 1,
                'new_state': 'E',
            }
        },
    }

    print(execute(program, 12399302))
