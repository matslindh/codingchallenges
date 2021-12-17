from bitarray import bitarray
from bitarray.util import hex2ba, ba2int
from functools import reduce
from operator import mul


def program_decoder(hex_instruction):
    bits = hex2ba(hex_instruction)
    return instruction_decoder(bits)


def instruction_decoder(bits):
    instr = {'version': None, 'type': None, 'value': None}
    version, type_ = ba2int(bits[0:3]), ba2int(bits[3:6])
    instr['version'] = version
    instr['type'] = type_

    remaining = bits[6:]

    if instr['type'] == 4:
        remaining, value = decode_literal(remaining)
        instr['value'] = value
    else:
        length_type = bits[6]
        bits = bits[7:]
        instr['value'] = []

        if not length_type & 1:
            read_bits = ba2int(bits[:15])
            bits = bits[15:]
            actual_read_bits = bits[:read_bits]
            remaining = bits[read_bits:]

            while read_bits >= 0:
                orig_length = len(actual_read_bits)
                value, actual_read_bits = instruction_decoder(actual_read_bits)
                instr['value'].append(value)

                if actual_read_bits is None:
                    break

                eaten = orig_length - len(actual_read_bits)
                read_bits -= eaten
        else:
            packets = ba2int(bits[:11])
            bits = bits[11:]

            for _ in range(packets):
                value, bits = instruction_decoder(bits)
                instr['value'].append(value)

            remaining = bits

    if not remaining or len(remaining) == 0 or ba2int(remaining) == 0:
        return instr, None

    return instr, remaining


def decode_literal(ba):
    value = bitarray()
    while ba[0] == 1:
        value += ba[1:5]
        ba = ba[5:]

    value += ba[1:5]
    return ba[5:], ba2int(value)


def execute_program(program):
    if program['type'] == 4:
        return program['value']

    values = [execute_program(prog) for prog in program['value']]

    if program['type'] == 0:
        return sum(values)
    elif program['type'] == 1:
        return reduce(mul, values)
    elif program['type'] == 2:
        return min(values)
    elif program['type'] == 3:
        return max(values)
    elif program['type'] == 5:
        return int(values[0] > values[1])
    elif program['type'] == 6:
        return int(values[0] < values[1])
    elif program['type'] == 7:
        return int(values[0] == values[1])
    else:
        print("DET ER KRISE")


def version_summer(packet):
    version_sum = packet['version']
    try:
        for instr in packet['value']:
            version_sum += version_summer(instr)
    except TypeError:
        pass

    return version_sum


def version_summer_from_program(program):
    return version_summer(program_decoder(program)[0])


def test_instructions_decoder():
    assert program_decoder('D2FE28') == ({'type': 4, 'version': 6, 'value': 2021}, None)


def test_instructions_decoder_with_operator_packet_length_type_0():
    assert program_decoder('38006F45291200') == ({'type': 6, 'version': 1, 'value': [{'type': 4, 'value': 10, 'version': 6},
                                                                                     {'type': 4, 'value': 20, 'version': 2},
                                                                                    ]}, None)


def test_instructions_decoder_with_operator_packet_length_type_1():
    assert program_decoder('EE00D40C823060') == ({'type': 3, 'version': 7, 'value': [{'type': 4, 'value': 1, 'version': 2},
                                                                                     {'type': 4, 'value': 2, 'version': 4},
                                                                                     {'type': 4, 'value': 3, 'version': 1},
                                                                                    ]}, None)


def test_version_number_summer_from_program():
    assert version_summer_from_program('8A004A801A8002F478') == 16
    assert version_summer_from_program('620080001611562C8802118E34') == 12
    assert version_summer_from_program('C0015000016115A2E0802F182340') == 23
    assert version_summer_from_program('A0016C880162017C3686B18A3D4780') == 31


def test_version_summer():
    assert version_summer({'type': 3, 'version': 7, 'value': [{'type': 4, 'value': 1, 'version': 2},
                                                              {'type': 4, 'value': 2, 'version': 4},
                                                              {'type': 4, 'value': 3, 'version': 1},
                                                             ]}) == 6
    assert version_summer({'type': 6, 'version': 1, 'value': [{'type': 4, 'value': 10, 'version': 6},
                                                              {'type': 4, 'value': 20, 'version': 2},
                                                             ]}) == 30


def test_execute_program():
    assert execute_program(program_decoder('C200B40A82')[0]) == 3
    assert execute_program(program_decoder('04005AC33890')[0]) == 54
    assert execute_program(program_decoder('880086C3E88112')[0]) == 7
    assert execute_program(program_decoder('CE00C43D881120')[0]) == 9
    assert execute_program(program_decoder('D8005AC2A8F0')[0]) == 1
    assert execute_program(program_decoder('F600BC2D8F')[0]) == 0
    assert execute_program(program_decoder('9C005AC2F8F0')[0]) == 0
    assert execute_program(program_decoder('9C0141080250320F1802104A08')[0]) == 1


if __name__ == '__main__':
    print(version_summer_from_program(open('input/16').read()))
    print(execute_program(program_decoder(open('input/16').read())[0]))