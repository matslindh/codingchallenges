import string

values = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']
msg = open("input/knowit05").read().strip('[]').split(', ')
decrypted = ''

for x in range(0, int(len(msg)/2)):
    idx = values.index(msg[x]) + values.index(msg[len(msg) - x - 1])
    decrypted += string.ascii_lowercase[idx-1]

print(decrypted)