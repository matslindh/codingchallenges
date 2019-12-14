def expand_alphabet(alphabet, lim):
    a_idx = 1
    sequence = [] + [alphabet[0]]*alphabet[0]
    s_idx = 1
    sevens = 0
    l = len(sequence)
    l_alph = len(alphabet)
    
    while l < lim:
        c = alphabet[a_idx]
        cnt = sequence[s_idx]

        if c == 7:
            sevens += cnt

        sequence.extend([alphabet[a_idx]] * sequence[s_idx])

        s_idx += 1
        a_idx = (a_idx + 1) % l_alph

        if s_idx % 100000 == 0:
            print(l)

        l += cnt

    return sevens


if __name__ == '__main__':
    print("Go!")
    # seq = expand_alphabet((2, 3, 5, 7, 11), 21753200)
    seq = expand_alphabet((2, 3, 5, 7, 11), 217532235)
    print(seq * 7)
    print("Gone!")
    # print(sum(7 for x in seq if seq[x] == 7))

    #print(Counter(seq)[7])
     
    # expand_alphabet((2, 3), 217532235)
