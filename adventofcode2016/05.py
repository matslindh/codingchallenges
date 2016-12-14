from hashlib import md5

prefix = 'reyedfim'
password = ''
found = 0
i = 0

while found < 8:
    k = prefix + str(i)
    h = md5(k.encode('ascii')).hexdigest()

    if h.startswith('00000'):
        print("Found one: " + h[5])
        password += h[5]
        found += 1

    i += 1

print(password)


