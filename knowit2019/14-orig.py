def expand_alphabet(alphabet, lim):
    a_idx = 1
    sequence = [] + [alphabet[0]]*alphabet[0]
    s_idx = 1

    while len(sequence) < lim:
        sequence.extend([alphabet[a_idx]] * sequence[s_idx])
        s_idx += 1
        a_idx = (a_idx + 1) % len(alphabet)

        if s_idx % 100000 == 0:
            print(len(sequence))

    return sequence


if __name__ == '__main__':
    print("Go!")
    seq = expand_alphabet((2, 3, 5, 7, 11), 217532235)
    print("Gone!")
    print(sum(7 for x in seq if seq[x] == 7))

    # expand_alphabet((2, 3), 217532235)
