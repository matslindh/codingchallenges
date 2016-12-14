from collections import Counter, OrderedDict
import string

sector_sum = 0

for line in open("input/dec04").readlines():
    parts = line.split('-')
    sector, checksum = parts[-1].strip("]\n").split('[')
    letters = ''.join(parts[:-1])
    encrypted_name = '-'.join(parts[:-1])
    frequency = Counter(letters).most_common()
    frequencies = OrderedDict()

    for letter, cnt in frequency:
        if cnt not in frequencies:
            frequencies[cnt] = []

        frequencies[cnt].append(letter)

    for cnt in frequencies:
        frequencies[cnt] = sorted(frequencies[cnt])

    checksum_generated = ''

    for cnt in frequencies:
        done = False

        for el in frequencies[cnt]:
            checksum_generated += el

            if len(checksum_generated) == 5:
                done = True
                break

        if done:
            break

    if checksum == checksum_generated:
        # decrypt
        chars = string.ascii_lowercase
        decrypted = ''

        for c in encrypted_name:
            if c == '-':
                decrypted += ' '
            else:
                decrypted += chars[(chars.index(c) + int(sector)) % 26]

        if decrypted == 'northpole object storage':
            print(sector)




