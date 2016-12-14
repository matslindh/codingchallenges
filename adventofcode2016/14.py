from functools import lru_cache

import hashlib

salt = 'yjdafjpo'
#salt = 'abc'
hashes = {}


@lru_cache(None)
def first_with_three(s):
    cnt = 0
    prev_x = None

    for x in s:
        if prev_x != x:
            cnt = 0

        cnt += 1

        if cnt == 3:
            return x

        prev_x = x

    return None


@lru_cache(None)
def seq_count(s):
    prev_x = None
    cnt = 1
    cnts = {}

    for x in s:
        if prev_x and prev_x != x:
            if prev_x not in cnts or cnts[prev_x] < cnt:
                cnts[prev_x] = cnt

            cnt = 1
        elif prev_x:
            cnt += 1

        prev_x = x

    if prev_x not in cnts or cnts[prev_x] < cnt:
        cnts[prev_x] = cnt

    return cnts


@lru_cache(None)
def hash(s, i):
    h = s + str(i)

    # part 1
    # return hashlib.md5(h.encode('ascii')).hexdigest()

    for _ in range(0, 2017):
        h = hashlib.md5(h.encode('ascii')).hexdigest()

    return h

idx = 0
keys = 0
found = False

while not found:
    h = hash(salt, idx)
    t = first_with_three(h)

    if t:
        for x in range(idx+1, idx+1001):
            h_2 = hash(salt, x)
            cnts = seq_count(h_2)

            if t in cnts and cnts[t] > 4:
                keys += 1
                print("Found key " + str(keys) + " at index " + str(idx))

                if keys == 72:
                    found = True

                found_key = True
                break

    idx += 1