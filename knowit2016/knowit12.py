import string
import math

msg = "Your message was received with gratitude! We do not know about you, but Christmas is definitely our favourite holiday. The tree, the lights, all the presents to unwrap. Could there be anything more magical than that?! We wish you a happy holiday and a happy new year!"
#msg = "a!Bc.,"
encrypted = []
values = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']

for c in msg.lower():
    if c in string.ascii_lowercase:
        idx = (string.ascii_lowercase.index(c) + 1)
        v = math.floor(idx / 2)
        v2 = idx - v

        v, v2 = reversed(sorted([v, v2]))

        s_idx = math.floor(len(encrypted)/2)
        encrypted.insert(s_idx, values[v2])
        encrypted.insert(s_idx, values[v])

print(', '.join(encrypted))

