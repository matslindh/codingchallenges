import string

out = open("input/knowit19_output.pgm", "w")
out_bin = open("input/knowit19_output.bin", "wb")
s = ''.join(open("input/knowit19").readlines()).replace("\n", '')

for i in range(0, len(s), 2):
    out_bin.write(chr(int(s[i:i + 2])).encode("ascii"))

height = 21
width = int(len(s) / (height * 2))

out.write("P2\n" + str(width) + ' ' + str(height) + "\n99\n")

for i in range(0, len(s), 2):
    letter = '99' if int(s[i:i+2]) % 2 == 0 else '0'

    if len(letter) < 2:
        letter = ' ' + letter

    out.write(letter + ' ')

    if (i + 2) % width == 0:
        out.write("\n")

for line in open("input/knowit19").readlines():
    line = line.strip()
    # print(int(line)&0xff)

str = ''.join(open("input/knowit19").readlines()).replace("\n", '')

freq = {}

for i in range(2, len(str), 2):
    v = int(str[i:i+2])
    v_diff = v - int(str[i-2:i])

    if v not in freq:
        freq[v] = 0

    freq[v] += 1

for k in freq:
    print(k, freq[k])


"""
v = int(str)

while v:
    x = v & 0xff
    print(chr(x))
    v >>= 8

print(v)"""