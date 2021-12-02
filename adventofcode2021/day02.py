from typing import List


test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def move_submarine(instructions: List):
    position = 0
    depth = 0

    for instruction in instructions:
        operator, distance = instruction.split(' ')
        distance = int(distance)

        if operator == 'forward':
            position += distance
        elif operator == 'up':
            depth -= distance
        elif operator == 'down':
            depth += distance
        else:
            print(f'Unknown operator: {operator}')

    return position * depth


def move_submarine_with_aim(instructions: List):
    position = 0
    aim = 0
    depth = 0

    for instruction in instructions:
        operator, distance = instruction.split(' ')
        distance = int(distance)

        if operator == 'forward':
            position += distance
            depth += aim * distance
        elif operator == 'up':
            aim -= distance
        elif operator == 'down':
            aim += distance
        else:
            print(f'Unknown operator: {operator}')

    return position * depth


def test_move_submarine():
    assert move_submarine(test_data.split("\n")) == 150


def test_move_submarine_aim():
    assert move_submarine_with_aim(test_data.split("\n")) == 900


if __name__ == '__main__':
    with open("input/02") as f:
        submarine_movement = f.read().split("\n")
        print(move_submarine(submarine_movement))
        print(move_submarine_with_aim(submarine_movement))
