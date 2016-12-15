v = '1111321112321111'
iterations = 50

for _ in range(0, iterations):
    v_n = ''
    cnt = 0
    c_prev = None

    for c in v:
        if c_prev and c_prev != c:
            v_n += str(cnt) + c_prev
            cnt = 0

        cnt += 1
        c_prev = c

    v = v_n + str(cnt) + c_prev
    print(_)

print(len(v))
