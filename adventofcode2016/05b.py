from hashlib import md5

prefix = 'reyedfim'
# prefix = 'abc'
password = ''
found = 0
i = 0
password = ['_']*8

while found < 8:
    k = prefix + str(i)
    h = md5(k.encode('ascii')).hexdigest()

    if h.startswith('00000'):
        print(h)
        idx = None

        try:
            idx = int(h[5])
        except ValueError:
            print("Skipped: " + h[5])
            pass

        if idx is not None and idx < 8 and password[idx] == '_':
            print("Found one: " + str(idx) + " - " + h[6])
            password[idx] = h[6]
            found += 1
            print(''.join(password))

    i += 1

print(''.join(password))