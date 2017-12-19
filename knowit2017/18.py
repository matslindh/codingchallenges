from collections import Counter

alphabet = 'AÁBDÐEÉFGHIÍJKLMNOÓPRSTUÚVXYÝÞÆÖ'
bits = '1110010101000001011000000011101110100101010011011010101101100000010001111101000001010010001011101001100100100011010000110101111101010011100010110001100111110010'
message = int(bits, 2).to_bytes((len(bits) + 7) // 8, 'big')

keys = Counter(open("input/dec18", encoding='utf-8').read())

key = 0
c = 0

for k in keys.most_common():
    if not k[0].strip():
        continue

    key += alphabet.index(k[0])
    key <<= 5

key >>= 5

key_enc = key.to_bytes(int(len(keys) * 5 / 8), 'big')
result = bytearray()

for i in range(0, len(message)):
    result.append(message[i] ^ key_enc[i])

print(result)
