from hashlib import md5

idx = 1

while True:
    if md5(f"bgvyzdsv{idx}".encode('ascii')).hexdigest().startswith('000000'):
        print(idx)
        break

    idx += 1