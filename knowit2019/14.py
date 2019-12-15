def expand_alphabet(alphabet, lim):
    a_idx = 1
    sequence = [] + [alphabet[0]]*alphabet[0]
    s_idx = 1
    sevens = 0
    l = len(sequence)
    l_alph = len(alphabet)
    cache = {}
    
    while l < lim:
        c = alphabet[s_idx % l_alph]
        cnt = sequence[s_idx]

        if c == 7:
            sevens += cnt

        if not c in cache:
            cache[c] = {}

        if not cnt in cache[c]:
            cache[c][cnt] = [c] * cnt

        sequence.extend(cache[c][cnt])

        s_idx += 1

        if s_idx % 100000 == 0:
            print(l)

        l += cnt

    return sevens


if __name__ == '__main__':
    print("Go!")
    #seq = expand_alphabet((2, 3, 5, 7, 11), 2175320)
    seq = expand_alphabet((2, 3, 5, 7, 11), 217532235)
    print(seq * 7)
    print("Gone!")
    # print(sum(7 for x in seq if seq[x] == 7))

    #print(Counter(seq)[7])
     
    # expand_alphabet((2, 3), 217532235)
