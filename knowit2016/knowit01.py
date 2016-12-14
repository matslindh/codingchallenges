x = 6

while True:
    x += 10
    x_4 = x*4
    x_s = str(x)
    x_4_s = str(x_4)

    s = '6' + x_s[:-1]

    if s == x_4_s:
        print(x)
        break

    print(x)