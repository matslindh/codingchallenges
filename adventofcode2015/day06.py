from bitstring import BitArray
from typing import List


def instructions(lines):
    instr = []
    for line in lines:
        ins = []
        parts = line.split()

        if line.startswith('turn on'):
            ins.append('on')
            ins.append(tuple(int(i) for i in parts[2].split(',')))
        elif line.startswith('turn off'):
            ins.append('off')
            ins.append(tuple(int(i) for i in parts[2].split(',')))
        elif line.startswith('toggle'):
            ins.append('toggle')
            ins.append(tuple(int(i) for i in parts[1].split(',')))

        ins.append(tuple(int(i) for i in parts[-1].split(',')))
        instr.append(tuple(ins))

    return instr


def run_instructions(lines):
    bits: List[BitArray] = []

    for y in range(0, 1000):
        bits.append(BitArray(length=1000))

    for instr, start, end in instructions(lines):
        for y in range(start[1], end[1] + 1):
            if instr == 'on':
                bits[y].set(True, range(start[0], end[0] + 1))
            elif instr == 'off':
                bits[y].set(False, range(start[0], end[0] + 1))
            elif instr == 'toggle':
                bits[y].invert(range(start[0], end[0] + 1))

    return sum(
        ba.count(True)
        for ba in bits
    )


def run_instructions_brightness(lines):
    bits: List[List[int]] = []

    for y in range(0, 1000):
        bits.append([0]*1000)

    for instr, start, end in instructions(lines):
        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                if instr == 'on':
                    bits[y][x] += 1
                elif instr == 'off':
                    bits[y][x] -= 1

                    if bits[y][x] < 0:
                        bits[y][x] = 0
                elif instr == 'toggle':
                    bits[y][x] += 2

    return sum(
        sum(ba)
        for ba in bits
    )


def test_instructions():
    assert instructions(["turn on 0,0 through 999,999"]) == [('on', (0, 0), (999, 999))]
    assert instructions(["toggle 0,0 through 999,0"]) == [('toggle', (0, 0), (999, 0))]
    assert instructions(["turn off 499,499 through 500,500"]) == [('off', (499, 499), (500, 500))]


if __name__ == '__main__':
    print(run_instructions(open("input/06").read().splitlines()))
    print(run_instructions_brightness(open("input/06").read().splitlines()))
