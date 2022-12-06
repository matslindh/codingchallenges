def offset_to_unique_sequence(chars, size):
    for idx in range(len(chars) - size):
        if len(set(chars[idx:idx+size])) == size:
            return idx + size


def offset_to_start_of_packet(chars):
    return offset_to_unique_sequence(chars, 4)


def offset_to_start_of_message(chars):
    return offset_to_unique_sequence(chars, 14)


def test_offset_to_start_of_packet():
    assert offset_to_start_of_packet('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert offset_to_start_of_packet('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert offset_to_start_of_packet('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert offset_to_start_of_packet('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11


def test_offset_to_start_of_message():
    assert offset_to_start_of_message('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert offset_to_start_of_message('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert offset_to_start_of_message('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert offset_to_start_of_message('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26


if __name__ == '__main__':
    print(offset_to_start_of_packet(open('input/06').read()))
    print(offset_to_start_of_message(open('input/06').read()))